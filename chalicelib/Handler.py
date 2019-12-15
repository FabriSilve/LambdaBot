class Handler():
    def __init__(self, answer=None):
        if answer is None:
            raise AssertionError
        self.answer = answer

    def match(self, message):
        if (message is None) or (not self.answer):
            return False
        return False

    def send(self, message):
        self.answer.send(message)
