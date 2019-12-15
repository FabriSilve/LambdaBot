

class Answer():
    TEXT = 'text'
    AUDIO = 'audio'
    IMAGE = 'image'

    def __init__(self, answer_type=None, value=None):
        if answer_type is None:
            raise AssertionError
        if not isinstance(answer_type, str):
            raise AssertionError
        if answer_type not in [self.AUDIO, self.TEXT, self.IMAGE]:
            raise AssertionError

        if value is None:
            raise AssertionError
        if not isinstance(value, str):
            raise AssertionError
        if not value.strip() != '':
            raise AssertionError

        self.answer_type = answer_type
        self.value = value
