import re


class Handler:
    def __init__(self, key, answer):
        self.key = key
        self.answer = answer

    def match(self, text):
        search_result = re \
            .compile(
                r'\b({0})\b'.format(self.key),
                flags=re.IGNORECASE
            ) \
            .search(text)
        return False if search_result is None else True

    def getAnswer(self, args=None):
        return self.answer.get(args)
