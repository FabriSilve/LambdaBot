from unittest import TestCase

from chalicelib.Answer import Answer


class AnswerTest(TestCase):

    def test_initialization_save_values(self):
        value = 'some answer text'
        answer = Answer(Answer.TEXT, value)

        self.assertEqual(answer.answer_type, Answer.TEXT)
        self.assertEqual(answer.value, value)
