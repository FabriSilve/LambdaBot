from unittest import TestCase
from unittest.mock import Mock

from chalicelib.Handler import Handler


class HandlerTest(TestCase):

    def test_initialization_save_values(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = Handler(answer_mock)

        self.assertIs(answer_mock, handler.answer)

    def test_abstract_handler_match(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = Handler(answer_mock)

        text = 'not triggered'

        self.assertFalse(handler.match(text))

        answer_mock.send.assert_not_called()

    def test_send_answer_response(self):
        answer_mock = Mock()
        answer_mock.send.return_value = None

        handler = Handler(answer_mock)

        text = 'test parameter'

        handler.send(text)

        answer_mock.send.assert_called_with(text)

    def test_raise_error_if_answer_is_none(self):
        self.assertRaises(AssertionError, Handler, None)

    def test_raise_error_if_answer_not_passed(self):
        self.assertRaises(AssertionError, Handler)
