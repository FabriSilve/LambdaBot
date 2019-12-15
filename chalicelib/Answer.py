

class Answer():
    TEXT = 'text'
    AUDIO = 'audio'
    IMAGE = 'image'

    def __init__(self, answer_type, value):
        if not answer_type:
            raise AssertionError
        if not isinstance(answer_type, str):
            raise AssertionError
        if answer_type not in [self.AUDIO, self.TEXT, self.IMAGE]:
            raise AssertionError

        if not value:
            raise AssertionError
        if not isinstance(value, str):
            raise AssertionError
        if not value.strip() != '':
            raise AssertionError

        self.answer_type = answer_type
        self.value = value

    def send(self):
        pass
