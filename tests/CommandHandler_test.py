from unittest import TestCase
from unittest.mock import Mock

from chalicelib.CommandHandler import CommandHandler
from chalicelib.Message import Message


class CommandHandlerTest(TestCase):

    def test_initialization_save_values(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        self.assertIs(answer_mock, handler.answer)
        self.assertIs('key', handler.key)

    def test_raise_error_if_answer_is_missing(self):
        self.assertRaises(TypeError, CommandHandler, 'key')

    def test_raise_error_if_key_is_none(self):
        answer_mock = Mock()
        self.assertRaises(AssertionError, CommandHandler, None, answer_mock)

    def test_raise_error_if_answer_is_none(self):
        self.assertRaises(AssertionError, CommandHandler, 'key', None)

    def test_command_handler_raise_error_with_no_message(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        self.assertRaises(TypeError, handler.match)
        answer_mock.send.assert_not_called()

    def test_command_handler_not_match_with_none_message(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        self.assertFalse(handler.match(None))
        answer_mock.send.assert_not_called()

    def test_command_handler_not_matching_key_in_text(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        message = Message({
            "message": {
                "text": "ciao",
                "chat": {"id": "123", "first_name": "Test"}
            }
        })

        self.assertFalse(handler.match(message))
        answer_mock.send.assert_not_called()

    def test_command_handler_matching_key_in_text(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        message = Message({
            "message": {
                "text": "/key",
                "chat": {"id": "123", "first_name": "Test"}
            }
        })

        print(message.text, handler.key, handler.regex, handler.match(message))
        self.assertTrue(handler.match(message))
        answer_mock.send.assert_not_called()

    def test_command_handler_not_matching_dirty_key_in_text(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        message = Message({
            "message": {
                "text": "/keyya",
                "chat": {"id": "123", "first_name": "Test"}
            }
        })

        self.assertFalse(handler.match(message))
        answer_mock.send.assert_not_called()

    def test_command_handler_matching_key_in_text_sentence(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        message = Message({
            "message": {
                "text": "/key is working",
                "chat": {"id": "123", "first_name": "Test"}
            }
        })

        self.assertTrue(handler.match(message))
        answer_mock.send.assert_not_called()

    def test_command_handler_not_matching_key_not_in_begining_of_text(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        message = Message({
            "message": {
                "text": "Hi /key command",
                "chat": {"id": "123", "first_name": "Test"}
            }
        })

        self.assertFalse(handler.match(message))
        answer_mock.send.assert_not_called()

    def test_command_handler_matching_key_ignoring_case_text(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = CommandHandler('key', answer_mock)

        message = Message({
            "message": {
                "text": "/KeY is working",
                "chat": {"id": "123", "first_name": "Test"}
            }
        })

        self.assertTrue(handler.match(message))
        answer_mock.send.assert_not_called()
