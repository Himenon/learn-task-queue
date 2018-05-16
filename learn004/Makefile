.PHONY: setup
setup:
	docker-compose build

.PHONY: up
up:
	docker-compose up -d
	docker-compose logs -f

.PHONY: down
down:
	docker-compose down

.PHONY: client
client:
	docker-compose run client bash

.PYONY: scale-up
scale-up:
	# >=v2.2
	docker-compose up --scale worker=3 -d
