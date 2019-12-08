import requests
import os

TOKEN = os.environ.get('TOKEN', 'token')
ENV = os.environ.get('TOKEN', 'test')

BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)

class RequestManager:
    def __init__(self, handlers):
        self.handlers = handlers

    def process(self, body):
        message = str(body["message"]["text"])
        chat_id = body["message"]["chat"]["id"]
        first_name = body["message"]["chat"]["first_name"]

        response = "Please /start, {}".format(first_name)

        if "start" in message:
            response = "Hello {}".format(first_name)

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = BASE_URL + "/sendMessage"
        if ENV == 'production':
            requests.post(url, json=data)
        else:
            print('\nLOG:')
            print(data)
            print('')


manager = RequestManager([])