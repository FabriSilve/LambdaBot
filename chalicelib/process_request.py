import requests
import os

TOKEN = os.environ.get('TOKEN', 'token')


BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def process_request(body, can_send=True):
    message = str(body["message"]["text"])
    chat_id = body["message"]["chat"]["id"]
    first_name = body["message"]["chat"]["first_name"]

    response = "Please /start, {}".format(first_name)

    if "start" in message:
        response = "Hello {}".format(first_name)

    data = {"text": response.encode("utf8"), "chat_id": chat_id}
    url = BASE_URL + "/sendMessage"

    if can_send:
        requests.post(url, json=data)
    else:
        print('LOG:', data)

    return {"statusCode": 200, "body": "ok"}
