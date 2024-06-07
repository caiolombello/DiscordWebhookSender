import requests
import sys
import os
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)

def send_webhook(webhook_url: str, content: Optional[str] = None, embed_title: Optional[str] = None, embed_description: Optional[str] = None, embed_color: Optional[int] = None) -> None:
    data = {}
    if content:
        data["content"] = content
    if embed_title or embed_description or embed_color:
        data["embeds"] = [
            {
                "title": embed_title,
                "description": embed_description,
                "color": embed_color
            }
        ]
    
    response = requests.post(webhook_url, json=data, timeout=15)
    if response.status_code == 204:
        logging.info("Message sent successfully")
    else:
        logging.error(
            f"Failed to send message: {response.status_code}, {response.text}"
        )

if __name__ == "__main__":
    webhook_url: Optional[str] = os.getenv("DISCORD_WEBHOOK_URL")
    content: Optional[str] = os.getenv("DISCORD_MESSAGE")
    embed_title: Optional[str] = os.getenv("DISCORD_EMBED_TITLE")
    embed_description: Optional[str] = os.getenv("DISCORD_EMBED_DESCRIPTION")
    embed_color: Optional[str] = os.getenv("DISCORD_EMBED_COLOR")

    if embed_color:
        try:
            embed_color = int(embed_color, 16)  # Convert hex string to integer
        except ValueError:
            logging.error("Invalid color format. Use hexadecimal value without '#'")
            sys.exit(1)

    if not webhook_url:
        print(
            "Environment variable DISCORD_WEBHOOK_URL is required"
        )
        sys.exit(1)
    
    send_webhook(webhook_url, content, embed_title, embed_description, embed_color)
