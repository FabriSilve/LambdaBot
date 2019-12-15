from unittest import TestCase

from chalicelib.Message import Message


class MessageTest(TestCase):

    def test_initialization_save_values(self):
        request = {
            "message": {
                "text": "ciao",
                "chat": {
                    "id": "123",
                    "first_name": "Test"
                }
            }
        }
        message = Message(request)

        self.assertEqual(message.text, "ciao")
        self.assertEqual(message.chat_id, "123")
        self.assertEqual(message.first_name, "Test")
