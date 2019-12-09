from chalice import Chalice

from chalicelib.process_request import process_request

app = Chalice(app_name='lambda-bot')


@app.route('/', methods=['POST'])
def index():
    body = app.current_request.json_body
    process_request(body)
    return {"statusCode": 200, "body": "ok"}
