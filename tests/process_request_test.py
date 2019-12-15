import unittest
from unittest.mock import patch

import os

from chalicelib.process_request import process_request

TOKEN = os.environ.get('TOKEN', 'token')
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


class ProcessRequestTEstTest(unittest.TestCase):
    @patch('requests.post')
    def test_http_request_done_for_start(self, mock_requests):
        result = process_request({
            "message": {
                "text": "ciao",
                "chat": {
                    "id": "123",
                    "first_name": "Test"
                }
            }
        })
        mock_requests.assert_called()
        mock_requests.assert_called_once_with(
            BASE_URL + '/sendMessage',
            json={
                "text": "Please /start, Test".encode("utf8"),
                "chat_id": "123"
            },
        )
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], 'ok')

    @patch('requests.post')
    def test_http_request_done_for_hello(self, mock_requests):
        result = process_request({
            "message": {
                "text": "/start",
                "chat": {
                    "id": "123",
                    "first_name": "Test"
                }
            }
        })
        mock_requests.assert_called()
        mock_requests.assert_called_once_with(
            BASE_URL + '/sendMessage',
            json={
                "text": "Hello Test".encode("utf8"),
                "chat_id": "123"
            },
        )

        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], 'ok')
