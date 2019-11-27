import unittest
from code.source.Answer import Answer


class AnswerTest(unittest.TestCase):
    def test_returns_true_if_key_match_exactly(self):
        handler = Answer('test', [])
        text = 'test'
        self.assertEqual(handler.match(text), True)