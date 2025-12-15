VENV_DIR = .venv
ACTIVATE_VENV := . $(VENV_DIR)/bin/activate

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
	$(ACTIVATE_VENV) && pip install --upgrade pip
	$(ACTIVATE_VENV) && pip install --requirement requirements.txt

install: $(VENV_DIR)

# format and tests
black: $(VENV_DIR)
	$(ACTIVATE_VENV) && black .

ruff: $(VENV_DIR)
	$(ACTIVATE_VENV) && ruff check .

test: black ruff

BOT_IMAGE=drozhdinovdm/unn_pizza_bot
BOT_CONTAINER=pizza_bot

include .env
export $(shell sed 's/=.*//' .env)


build:
	docker build \
	  -t $(BOT_IMAGE) \
	  --platform linux/amd64 \
	  -f Dockerfile \
	  .

push:
	docker push $(BOT_IMAGE)

run:
	docker run -d \
	  --name $(BOT_CONTAINER) \
	  --restart unless-stopped \
	  -e TELEGRAM_TOKEN="$(TELEGRAM_TOKEN)" \
	  $(BOT_IMAGE)

stop:
	docker stop $(BOT_CONTAINER)
	docker rm $(BOT_CONTAINER)

logs:
	docker logs -f $(BOT_CONTAINER)