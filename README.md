# DiscordWebhookSender

**Version:** 1.0.0

DiscordWebhookSender is a project designed to send messages to a Discord webhook using Python and Docker.

## Table of Contents

- [Description](#description)
- [How to Use](#how-to-use)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run the Docker Container](#run-the-docker-container)
- [Environment Variables](#environment-variables)
- [Development](#development)
  - [Installation](#installation)
  - [Commands](#commands)
- [Contribution](#contribution)
- [License](#license)
- [Pipeline Example](#pipeline-example)

## Description

DiscordWebhookSender is a simple tool to send messages to a specified Discord webhook URL. It is containerized using Docker to ensure ease of deployment and use.

## How to Use

### Build the Docker Image

To build the Docker image, run the following command:

```sh
make docker-build
```

### Run the Docker Container

To run the Docker container, use one of the following commands, replacing `<YOUR_WEBHOOK_URL>`, `<YOUR_MESSAGE>`, `<YOUR_EMBED_TITLE>`, `<YOUR_EMBED_DESCRIPTION>`, and `<YOUR_EMBED_COLOR>` with your actual values:

For a simple message:
```sh
docker run --rm -e DISCORD_WEBHOOK_URL="<YOUR_WEBHOOK_URL>" -e DISCORD_MESSAGE="<YOUR_MESSAGE>" discord-webhook-sender
```

For a message with embed:
```sh
docker run --rm \
  -e DISCORD_WEBHOOK_URL="<YOUR_WEBHOOK_URL>" \
  -e DISCORD_MESSAGE="<YOUR_MESSAGE>" \
  -e DISCORD_EMBED_TITLE="<YOUR_EMBED_TITLE>" \
  -e DISCORD_EMBED_DESCRIPTION="<YOUR_EMBED_DESCRIPTION>" \
  -e DISCORD_EMBED_COLOR="<YOUR_EMBED_COLOR>" \
  discord-webhook-sender
```

### Environment Variables

- `DISCORD_WEBHOOK_URL`: The URL of the Discord webhook.
- `DISCORD_MESSAGE`: The message to be sent.
- `DISCORD_EMBED_TITLE`: The title of the embed (optional).
- `DISCORD_EMBED_DESCRIPTION`: The description of the embed (optional).
- `DISCORD_EMBED_COLOR`: The color of the embed in hexadecimal format without `#` (optional).

## Development

### Installation

To set up the development environment, you need to have [Poetry](https://python-poetry.org/) installed. Then, run:

```sh
poetry install
```

### Commands

- **Run tests:**

  To run the test suite, use:

  ```sh
  poetry run make test
  ```

- **Lint and format code:**

  To lint and format the code, use:

  ```sh
  make lint
  ```

- **Build Docker image:**

  To build the Docker image, use:

  ```sh
  make docker-build
  ```

- **Run Docker container:**

  To run the Docker container, use:

  ```sh
  make docker-run
  ```

- **Clean the project:**

  To clean the project, use:

  ```sh
  make clean
  ```

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Pipeline Example

Here is an example of how to use DiscordWebhookSender in a pipeline:

```yaml
notify:
  stage: post-apply
  image: 
    name: caiolombello/discord-webhook-sender
  variables:
    DISCORD_WEBHOOK_URL: <YOUR_WEBHOOK_URL>
    DISCORD_MESSAGE: "Infrastructure deployment completed successfully."
    DISCORD_EMBED_TITLE: "Deployment Notification"
    DISCORD_EMBED_DESCRIPTION: "Your deployment was successful."
    DISCORD_EMBED_COLOR: "00FF00"
  script: /app/send_webhook
  dependencies:
    - apply
```

This example demonstrates how to use the DiscordWebhookSender image in a CI/CD pipeline to send a notification after successful infrastructure deployment.