#!/usr/bin/python3 -uB

import os
import json
import google.auth.transport.requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from datetime import datetime, timedelta

# Specify the scopes required
SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read']

# Path to the credentials.json file
CLIENT_SECRETS_FILE = 'credentials.json'
# Path to the token.json file where the credentials will be stored
TOKEN_FILE = 'token.json'

# Authenticate and create the API client
def authenticate():
    credentials = None

    # Load credentials from the token file if it exists
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as token:
            token_data = json.load(token)
            credentials = Credentials.from_authorized_user_info(token_data, SCOPES)

    # If there are no valid credentials available, authenticate with Google
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(google.auth.transport.requests.Request())
        else:
            # Create the flow using the client secrets file
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(credentials.to_json())

    return credentials

# Function to get the time in nanoseconds since epoch
def get_time_ns(days_ago=0):
    time = datetime.utcnow() - timedelta(days=days_ago)
    return int(time.timestamp() * 1e9)

def main():
    # Authenticate and get the API client
    credentials = authenticate()
    service = googleapiclient.discovery.build('fitness', 'v1', credentials=credentials)

    # Get the list of data sources for the user
    data_sources = service.users().dataSources().list(userId='me').execute()

    # Print all data sources for debugging
    print("Data Sources:")
    for data_source in data_sources.get('dataSource', []):
        print(data_source['dataStreamId'])

    # Iterate over the data sources to find step count data
    for data_source in data_sources.get('dataSource', []):
        if 'derived:com.google.step_count.delta' in data_source['dataStreamId']:
            # Define the time range for the data set (last 7 days)
            start_time_ns = get_time_ns(days_ago=7)
            end_time_ns = get_time_ns()
            dataset_id = f'{start_time_ns}-{end_time_ns}'

            # Fetch the dataset for the specified data source and time range
            dataset = service.users().dataSources().datasets().get(
                userId='me',
                dataSourceId=data_source['dataStreamId'],
                datasetId=dataset_id
            ).execute()

            # Print the step count data
            for point in dataset.get('point', []):
                if 'value' in point:
                    print(f"Steps: {point['value'][0]['intVal']}")

if __name__ == '__main__':
    main()

