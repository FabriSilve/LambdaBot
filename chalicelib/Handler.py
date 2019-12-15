class Handler():
    def __init__(self, answer=None):
        if answer is None:
            raise AssertionError
        self.answer = answer

    def match(self, message=None):
        pass

    def send(self, message=None):
        self.answer.send(message)
