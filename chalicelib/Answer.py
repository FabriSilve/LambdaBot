

class Answer():
    TEXT = 'text'
    AUDIO = 'audio'
    IMAGE = 'image'

    def __init__(self, answer_type, value):
        assert answer_type is not None
        assert isinstance(answer_type, str)
        assert answer_type == self.AUDIO \
            or answer_type == self.TEXT \
            or answer_type == self.IMAGE

        assert value is not None
        assert isinstance(value, str)
        assert value.strip() != ''

        self.answer_type = answer_type
        self.value = value

    def send(self):
        pass
