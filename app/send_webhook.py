import requests
import sys
import os
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)


def send_webhook(webhook_url: str, message: str) -> None:
    data = {"content": message}
    response = requests.post(webhook_url, json=data, timeout=15)
    if response.status_code == 204:
        logging.info("Message sent successfully")
    else:
        logging.error(
            f"Failed to send message: {response.status_code}, {response.text}"
        )


if __name__ == "__main__":
    webhook_url: Optional[str] = os.getenv("DISCORD_WEBHOOK_URL")
    message: Optional[str] = os.getenv("DISCORD_MESSAGE")
    if not webhook_url or not message:
        print(
            "Environment variables DISCORD_WEBHOOK_URL and DISCORD_MESSAGE are required"
        )
        sys.exit(1)
    send_webhook(webhook_url, message)
