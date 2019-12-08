from chalice import Chalice
import requests
import os

app = Chalice(app_name='lambda-bot')

TOKEN = os.environ.get('TOKEN', 'token')
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


@app.route('/', methods=['POST'])
def index():
    body = app.current_request.json_body

    try:
        message = str(body["message"]["text"])
        chat_id = body["message"]["chat"]["id"]
        first_name = body["message"]["chat"]["first_name"]

        response = "Please /start, {}".format(first_name)

        if "start" in message:
            response = "Hello {}".format(first_name)

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = BASE_URL + "/sendMessage"
        requests.post(url, json=data)
    except:  # noqa: E722
        print('Error handling telegram message')

    return {"statusCode": 200, "body": "ok"}
