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

## Description

DiscordWebhookSender is a simple tool to send messages to a specified Discord webhook URL. It is containerized using Docker to ensure ease of deployment and use.

## How to Use

### Build the Docker Image

To build the Docker image, run the following command:

```sh
make docker-build
```

### Run the Docker Container

To run the Docker container, use the following command, replacing `<YOUR_WEBHOOK_URL>` and `<YOUR_MESSAGE>` with your actual values:

```sh
docker run --rm -e DISCORD_WEBHOOK_URL="<YOUR_WEBHOOK_URL>" -e DISCORD_MESSAGE="<YOUR_MESSAGE>" discord-webhook-sender
```

## Environment Variables

- `DISCORD_WEBHOOK_URL`: The URL of the Discord webhook.
- `DISCORD_MESSAGE`: The message to be sent.

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