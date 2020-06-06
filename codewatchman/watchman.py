import json
import requests
import asyncio

import codewatchman.watchmanlog as watchmanlog

def make_cwm_request(
    endpoint,
    json_data,
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
):
    try:
        # url = 'http://localhost:5001/codewatchman/us-central1'
        url = 'https://us-central1-codewatchman.cloudfunctions.net'
        final_url = '{}/{}'.format(url, endpoint)

        response = requests.post(
            final_url,
            json=json_data,
            headers=headers,
            timeout=10
        )
        print("Request complete.", response)

        response_data = response.content.decode('utf8').replace("'", '"')
        response_json = json.loads(response_data)

        return response_json
    except Exception as e:
        print("Error @ Code Watchman", e)

class watchman:
    def __init__(self, token_id, access_token):
        print(token_id, access_token)
        self.token_id = token_id
        self.access_token = access_token
        self.is_validated = False
        self.validation_message = None
        self.check_token_validity()

    def check_token_validity(self):
        if self.is_validated == True:
            return

        response = make_cwm_request(
            endpoint="validateToken",
            json_data={
                "tokenId": self.token_id,
                "accessToken": self.access_token
            }
        )
        print("Checking Validity", response)
        if response["status"] == "ok":
            self.is_validated = True


    def send_log(self, log_data):
        if self.is_validated is False:
            self.check_token_validity()

        if type(log_data) is not watchmanlog.watchmanlog:
            print("Use watchmanlog class to build log object")
            return
        else:
            self._sendlog(log_data)


    def _sendlog(self, log_data):
        if log_data.is_valid != True:
            print("Provided log data is not valid.")

        if type(log_data.payload) is dict:
            payload = json.dumps(log_data.payload)
        else:
            payload = json.dumps({})



        response = make_cwm_request(
            endpoint="makeLog",
            json_data={
                "tokenId": self.token_id,
                "accessToken": self.access_token,
                "message": log_data.message,
                "payload": payload,
                "logCode": log_data.log_code
            }
        )
        print("Data logged", response)