from unittest import TestCase

from chalicelib.Answer import Answer


class AnswerTest(TestCase):

    def test_initialization_save_values(self):
        value = 'some answer text'
        answer = Answer(Answer.TEXT, value)

        self.assertEqual(answer.answer_type, Answer.TEXT)
        self.assertEqual(answer.value, value)

    def test_throw_error_if_type_not_allowed(self):
        self.assertRaises(
            AssertionError,
            Answer,
            'test',
            'value',
        )

    def test_throw_error_if_type_not_defined(self):
        self.assertRaises(
            AssertionError,
            Answer,
            None,
            'value',
        )

    def test_throw_error_if_type_not_string(self):
        self.assertRaises(
            AssertionError,
            Answer,
            33,
            'value',
        )

    def test_throw_error_if_value_not_allowed(self):
        self.assertRaises(
            AssertionError,
            Answer,
            'test',
            'ciao',
        )

    def test_throw_error_if_value_not_defined(self):
        self.assertRaises(
            AssertionError,
            Answer,
            Answer.TEXT,
            None,
        )

    def test_throw_error_if_value_parameter_is_missing(self):
        self.assertRaises(
            AssertionError,
            Answer,
            Answer.TEXT,
        )

    def test_throw_error_if_value_not_string(self):
        self.assertRaises(
            AssertionError,
            Answer,
            Answer.TEXT,
            33,
        )

    def test_throw_error_if_value_is_empty_string(self):
        self.assertRaises(
            AssertionError,
            Answer,
            Answer.TEXT,
            '',
        )
