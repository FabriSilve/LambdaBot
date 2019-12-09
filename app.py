from chalice import Chalice

from chalicelib.RequestManager import manager

app = Chalice(app_name='lambda-bot')


@app.route('/', methods=['POST'])
def index():
    body = app.current_request.json_body
    manager.process(body)
    return {"statusCode": 200, "body": "ok"}
