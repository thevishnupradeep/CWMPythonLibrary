import json
import requests

class watchman:
    def __init__(self, tokenId, accessToken):
        print(tokenId, accessToken)
        self.tokenId = tokenId
        self.accessToken = accessToken
        self.is_validated = False
        self.validation_message = None

        self.checkTokenValidity()

    def checkTokenValidity(self):
        url = 'https://us-central1-codewatchman.cloudfunctions.net/validateToken'

        response = requests.post(
            url,
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