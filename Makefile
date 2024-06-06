.ONESHELL:
.PHONY: $(MAKECMDGOALS)
##
##    🚧 WebhookSender developer tools
##

##

help:           ## Show this help (default)
	@grep -F -h "##" $(MAKEFILE_LIST) | grep -F -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

all:            ## Run a whole CI pipeline: formatters, linters, tests
	make lint test

lint:           ## Lint with all tools
	make black ruff mypy

test:           ## Run test suite
	pytest app/test_send_webhook.py

##

black:          ## Format with black
	black app/

ruff:           ## Lint with ruff
	ruff check --fix --unsafe-fixes app/

mypy:           ## Lint with mypy
	mypy --strict app/

##

clean:          ## Remove all files from .gitignore except for `.venv`
	git clean -xdf --exclude=".venv"

docker-build:   ## Build the Docker image
	docker build -t discord-webhook-sender app

docker-run:     ## Run the Docker container
	docker run --rm -e DISCORD_WEBHOOK_URL="<YOUR_WEBHOOK_URL>" -e DISCORD_MESSAGE="<YOUR_MESSAGE>" discord-webhook-sender

