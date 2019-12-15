import re

from chalicelib.Handler import Handler


class CommandHandler(Handler):
    REGEX = r"(^\/{}$|^\/{}\s.*$)"

    def __init__(self, key, answer):
        if key is None:
            raise AssertionError

        if answer is None:
            raise AssertionError

        self.key = key
        self.regex = re.compile(self.REGEX.format(key, key), re.IGNORECASE)
        super().__init__(answer)

    def match(self, message):
        if message is None:
            return False
        return self.regex.match(message.text) is not None
