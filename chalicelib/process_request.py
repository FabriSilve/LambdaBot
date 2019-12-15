import requests
import os

TOKEN = os.environ.get('TOKEN', 'token')
ENV = os.environ.get('ENV', 'test')

BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def process_request(body):
    message = str(body["message"]["text"])
    chat_id = body["message"]["chat"]["id"]
    first_name = body["message"]["chat"]["first_name"]

    response = "Please /start, {}".format(first_name)

    if "start" in message:
        response = "Hello {}".format(first_name)

    data = {"text": response.encode("utf8"), "chat_id": chat_id}
    url = BASE_URL + "/sendMessage"

    if ENV == 'local':
        print('LOG:', data)
    else:
        requests.post(url, json=data)

    return {"statusCode": 200, "body": "ok"}
