from chalice import Chalice

from chalicelib.process_request import process_request

app = Chalice(app_name='lambda-bot')


@app.route('/', methods=['POST'])
def index():
    body = app.current_request.json_body
    return process_request(body)
