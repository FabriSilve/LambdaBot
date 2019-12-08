from chalice import Chalice

from chalicelib.RequestManager import manager

app = Chalice(app_name='lambda-bot')


@app.route('/', methods=['POST'])
def index():
    try:
        body = app.current_request.json_body
        manager.process(body)
    except:  # noqa: E722
        print('Error handling telegram message')
    finally:
        return {"statusCode": 200, "body": "ok"}
