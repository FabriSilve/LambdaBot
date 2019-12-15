from chalice import Chalice
import os

from chalicelib.process_request import process_request

app = Chalice(app_name='lambda-bot')

ENV = os.environ.get('ENV', 'test')


@app.route('/', methods=['POST'])
def index():
    body = app.current_request.json_body
    can_send = ENV == 'production'
    return process_request(body, can_send)
