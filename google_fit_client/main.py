#!/usr/bin/python3 -uB

import os
import json
import google.auth.transport.requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
import datetime
import time

activity_codes = {
    0: "In Vehicle",
    1: "Biking",
    2: "On Foot",
    3: "Still (not moving)",
    4: "Unknown",
    5: "Tilting",
    6: "Exiting Vehicle",
    7: "Walking",
    8: "Running",
    9: "Aerobics",
    10: "Badminton",
    11: "Baseball",
    12: "Basketball",
    13: "Biathlon",
    14: "Handbiking",
    15: "Mountain Biking",
    16: "Road Biking",
    17: "Spinning",
    18: "Stationary Biking",
    19: "Utility Biking",
    20: "Boxing",
    21: "Calisthenics",
    22: "Circuit Training",
    23: "Cricket",
    24: "Dancing",
    25: "Elliptical",
    26: "Fencing",
    27: "American Football",
    28: "Australian Football",
    29: "Soccer",
    30: "Frisbee",
    31: "Gardening",
    32: "Golf",
    33: "Gymnastics",
    34: "Handball",
    35: "Hiking",
    36: "Hockey",
    37: "Horseback Riding",
    38: "Housework",
    39: "Jumping Rope",
    40: "Kayaking",
    41: "Kettlebell Training",
    42: "Kickboxing",
    43: "Kitesurfing",
    44: "Martial Arts",
    45: "Meditation",
    46: "Mixed Martial Arts",
    47: "P90X",
    48: "Paragliding",
    49: "Pilates",
    50: "Polo",
    51: "Racquetball",
    52: "Rock Climbing",
    53: "Rowing",
    54: "Rowing Machine",
    55: "Rugby",
    56: "Jogging",
    57: "Running on Sand",
    58: "Running (Treadmill)",
    59: "Sailing",
    60: "Scuba Diving",
    61: "Skateboarding",
    62: "Skating",
    63: "Cross Skating",
    64: "Indoor Skating",
    65: "Inline Skating",
    66: "Skiing",
    67: "Backcountry Skiing",
    68: "Cross-Country Skiing",
    69: "Downhill Skiing",
    70: "Kite Skiing",
    71: "Roller Skiing",
    72: "Sledding",
    73: "Sleeping",
    74: "Snowboarding",
    75: "Snowmobile",
    76: "Snowshoeing",
    77: "Squash",
    78: "Stair Climbing",
    79: "Stair-Climbing Machine",
    80: "Stand-Up Paddleboarding",
    81: "Strength Training",
    82: "Surfing",
    83: "Swimming",
    84: "Swimming (Open Water)",
    85: "Swimming (Pool)",
    86: "Table Tennis",
    87: "Team Sports",
    88: "Tennis",
    89: "Treadmill (Walking or Running)",
    90: "Volleyball",
    91: "Volleyball (Beach)",
    92: "Volleyball (Indoor)",
    93: "Wakeboarding",
    94: "Walking (Fitness)",
    95: "Nording Walking",
    96: "Walking (Treadmill)",
    97: "Waterpolo",
    98: "Weightlifting",
    99: "Wheelchair",
    100: "Windsurfing",
    101: "Yoga",
    102: "Zumba",
    103: "Diving",
    104: "Ergometer",
    105: "Ice Skating",
    106: "Indoor Skating",
    107: "Curling",
    108: "Other (Uncategorized)"
}

# Specify the scopes required
SCOPES = [
        'https://www.googleapis.com/auth/fitness.activity.read',
        'https://www.googleapis.com/auth/fitness.location.read',
        'https://www.googleapis.com/auth/fitness.body.read'
]

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

def get_my_activities(service, days=1):
    now = datetime.datetime.utcnow()
    start_time = now - datetime.timedelta(days=days)  # Extend to last 30 days
    dataset_id = f"{int(start_time.timestamp() * 1e9)}-{int(now.timestamp() * 1e9)}"

    data_source = "derived:com.google.activity.segment:com.google.android.gms:merge_activity_segments"
    request = service.users().dataSources().datasets().get(userId='me', dataSourceId=data_source, datasetId=dataset_id)
    response = request.execute()

    activities = {}
    n = 0
    for point in response.get('point', []):
        activity_type = point['value'][0]['intVal']
        activity_name = activity_codes[activity_type]
        if activity_name not in activities:
            activities[activity_codes[activity_type]] = []
        start_time = datetime.datetime.fromtimestamp(int(point['startTimeNanos']) / 1e9)
        end_time = datetime.datetime.fromtimestamp(int(point['endTimeNanos']) / 1e9)
        distance = get_distance(service, start_time, end_time)
        activities[activity_name].append({
            'activity': activity_name,
            'start_time': start_time.strftime("%Y/%m/%d, %H:%M:%S"),
            'end_time': end_time.strftime("%Y/%m/%d, %H:%M:%S"),
            'duration': (end_time - start_time).total_seconds() / 60.0,
            'distance': distance
        })
        time.sleep(2)
        n = n + 1
        print(f'Activities processed: {n}/{len(response.get("point", []))}')

    return activities

def get_distance(service, start_time, end_time):
    dataset_id = f"{int(start_time.timestamp() * 1e9)}-{int(end_time.timestamp() * 1e9)}"
    data_source = "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta"
    
    request = service.users().dataSources().datasets().get(userId='me', dataSourceId=data_source, datasetId=dataset_id)
    response = request.execute()

    total_distance = 0.0
    for point in response.get('point', []):
        for value in point['value']:
            total_distance += value['fpVal']

    return total_distance

def main():
    days = 365
    # Authenticate and get the API client
    credentials = authenticate()
    service = googleapiclient.discovery.build('fitness', 'v1', credentials=credentials)
    activities = get_my_activities(service, days)
    # Specify the file path
    file_path = 'activities.json'

    # Write the dictionary to the file as JSON
    with open(file_path, 'w') as json_file:
        json.dump(activities, json_file, indent=4)

    for activity_type in activities:
        sum_distance = 0
        for a in activities[activity_type]:
            sum_distance = sum_distance + a['distance']
        print(f'{activity_type} {days} {sum_distance / 1000.0} km')


if __name__ == '__main__':
    main()

