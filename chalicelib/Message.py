class Message():
    def __init__(self, body):
        self.text = str(body['message']['text'])
        self.chat_id = str(body['message']['chat']['id'])
        self.first_name = str(body['message']['chat']['first_name'])
