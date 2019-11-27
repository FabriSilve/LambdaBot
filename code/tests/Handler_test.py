import unittest
from code.source.Handler import Handler


class HandlerTest(unittest.TestCase):
    def test_returns_true_if_key_match_exactly(self):
        handler = Handler('test', [])
        text = 'test'
        self.assertEqual(handler.match(text), True)

    def test_returns_false_if_key_not_match(self):
        handler = Handler('test', [])
        text = 'dog'
        self.assertEqual(handler.match(text), False)

    def test_returns_true_if_key_in_sentence_same_case(self):
        handler = Handler('test', [])
        text = 'This is a test'
        self.assertEqual(handler.match(text), True)

    def test_returns_true_if_key_in_sentence_different_case(self):
        handler = Handler('test', [])
        text = 'This is a TEST'
        self.assertEqual(handler.match(text), True)
