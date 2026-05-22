import json

import requests
from utils.logger import Logger


class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def _send_request(self, method, path, data=None, headers=None):
        url = f"{self.base_url}{path}"
        headers = headers if headers is not None else self._headers()

        Logger.add_request(url=url, data=data, headers=headers, method=method)
        response = requests.request(method=method, url=url, data=data, headers=headers)
        Logger.add_response(response)

        return response

    def get_object(self, object_id):
        response = self._send_request("GET", f"/objects/{object_id}")
        return response

    def create_object(self, payload):
        response = self._send_request("POST", f"/objects", data=json.dumps(payload))
        return response

    def update_object(self, object_id, payload):
        response = self._send_request("PUT", f"/objects/{object_id}", data=json.dumps(payload))
        return response

    def delete_object(self, object_id):
        response = self._send_request("DELETE", f"/objects/{object_id}")
        return response

    @staticmethod
    def _headers():
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        return headers
