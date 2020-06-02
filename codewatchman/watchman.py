import json
import requests
import asyncio

import codewatchman.watchmanlog as watchmanlog

class watchman:
    # url = 'http://localhost:5001/codewatchman/us-central1/makeLog'
    url = 'https://us-central1-codewatchman.cloudfunctions.net'

    watchmantasks = asyncio.Queue()

    def __init__(self, tokenId, accessToken):
        print(tokenId, accessToken)
        self.tokenId = tokenId
        self.accessToken = accessToken
        self.is_validated = False
        self.validation_message = None

    async def checkTokenValidity(self):
        if self.is_validated == True:
            return

        finalURL = '{}/validateToken'.format(self.url)
        response = requests.post(
            finalURL,
            json={
                "tokenId": self.tokenId,
                "accessToken": self.accessToken
            },
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        )

        response_data = response.content.decode('utf8').replace("'", '"')
        print("Checking Validity", response)

        try:
            response_json = json.loads(response_data)
            print("Final Check", response_json)
            self.is_validated = True
            self.validation_message = response_json["message"]
        except ValueError:
            print(response_data)
            self.is_validated = False
            self.validation_message = response_data

    async def send_log(self, log_data):
        if self.is_validated is False:
            await self.checkTokenValidity()
            return

        if type(log_data) is not watchmanlog.watchmanlog:
            print("Use watchmanlog class to build log object")
            return
        else:
            await self._sendlog(log_data)


    async def _sendlog(self, log_data):
        if type(log_data.payload) is dict:
            payload = json.dumps(log_data.payload)
        else:
            payload = json.dumps({})

        finalURL = '{}/makeLog'.format(self.url)
        response = requests.post(
            finalURL,
            json={
                "tokenId": self.tokenId,
                "accessToken": self.accessToken,
                "message": log_data.message,
                "payload": payload
            },
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        )

        response_data = response.content.decode('utf8').replace("'", '"')
        print("Checking log response", response)

        try:
            response_json = json.loads(response_data)
            print("Final Check", response_json)
            print("Data logged")
        except ValueError:
            print(response_data)

    async def stop(self):
        print("Stopping watchman")