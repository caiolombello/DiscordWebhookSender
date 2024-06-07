import unittest
from unittest.mock import patch
from send_webhook import send_webhook

class TestSendWebhook(unittest.TestCase):

    @patch("requests.post")
    def test_send_webhook_success_simple_message(self, mock_post: unittest.mock.Mock) -> None:
        mock_post.return_value.status_code = 204
        with self.assertLogs(level="INFO") as log:
            send_webhook("http://example.com", "test message")
            self.assertIn("Message sent successfully", log.output[0])

    @patch("requests.post")
    def test_send_webhook_success_with_embed(self, mock_post: unittest.mock.Mock) -> None:
        mock_post.return_value.status_code = 204
        with self.assertLogs(level="INFO") as log:
            send_webhook(
                "http://example.com",
                content="test message",
                embed_title="Test Title",
                embed_description="Test Description",
                embed_color=0x00FF00
            )
            self.assertIn("Message sent successfully", log.output[0])

    @patch("requests.post")
    def test_send_webhook_failure_simple_message(self, mock_post: unittest.mock.Mock) -> None:
        mock_post.return_value.status_code = 400
        mock_post.return_value.text = "Bad Request"
        with self.assertLogs(level="ERROR") as log:
            send_webhook("http://example.com", "test message")
            self.assertIn("Failed to send message", log.output[0])

    @patch("requests.post")
    def test_send_webhook_failure_with_embed(self, mock_post: unittest.mock.Mock) -> None:
        mock_post.return_value.status_code = 400
        mock_post.return_value.text = "Bad Request"
        with self.assertLogs(level="ERROR") as log:
            send_webhook(
                "http://example.com",
                content="test message",
                embed_title="Test Title",
                embed_description="Test Description",
                embed_color=0x00FF00
            )
            self.assertIn("Failed to send message", log.output[0])

if __name__ == "__main__":
    unittest.main()
