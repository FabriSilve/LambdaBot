from chalice import Chalice

from source.RequestManager import manager

app = Chalice(app_name='lambda-bot')

@app.route('/', methods=['POST'])
def index():
    try:
        body = app.current_request.json_body
        manager.process(body)
    finally:
        return {"statusCode": 200, "body": "ok"}
