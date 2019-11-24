import unittest
from code.source.Answer import Answer


class AnswerTest(unittest.TestCase):
    def test_returns_true_if_key_match_exactly(self):
        answer = Answer('test')
        text = 'test'
        self.assertEqual(answer.match(text), True)

    def test_returns_false_if_key_not_match(self):
        answer = Answer('test')
        text = 'dog'
        self.assertEqual(answer.match(text), False)

    def test_returns_true_if_key_in_sentence_same_case(self):
        answer = Answer('test')
        text = 'This is a test'
        self.assertEqual(answer.match(text), True)

    def test_returns_true_if_key_in_sentence_different_case(self):
        answer = Answer('test')
        text = 'This is a TEST'
        self.assertEqual(answer.match(text), True)
