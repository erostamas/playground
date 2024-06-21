import unittest
from main import create_app


class TestMyFlaskApp(unittest.TestCase):

    def test_request_example(self):
        app = create_app()
        client = app.test_client()
        response = client.get("/")
        print(response.data)
        response = client.get("/")
        print(response.data)
        response = client.get("/")
        print(response.data)

if __name__ == '__main__':
    unittest.main()

