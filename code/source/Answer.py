import re


class Answer:
    def __init__(self, key):
        self.key = key

    def match(self, text):
        search_result = re \
            .compile(
                r'\b({0})\b'.format(self.key),
                flags=re.IGNORECASE
            ) \
            .search(text)
        return False if search_result is None else True
