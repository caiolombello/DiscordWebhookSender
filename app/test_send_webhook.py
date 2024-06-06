import unittest
from unittest.mock import patch
from send_webhook import send_webhook


class TestSendWebhook(unittest.TestCase):

    @patch("requests.post")
    def test_send_webhook_success(self, mock_post: unittest.mock.Mock) -> None:
        mock_post.return_value.status_code = 204
        with self.assertLogs(level="INFO") as log:
            send_webhook("http://example.com", "test message")
            self.assertIn("Message sent successfully", log.output[0])

    @patch("requests.post")
    def test_send_webhook_failure(self, mock_post: unittest.mock.Mock) -> None:
        mock_post.return_value.status_code = 400
        mock_post.return_value.text = "Bad Request"
        with self.assertLogs(level="ERROR") as log:
            send_webhook("http://example.com", "test message")
            self.assertIn("Failed to send message", log.output[0])


if __name__ == "__main__":
    unittest.main()
