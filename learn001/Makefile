.PHONY: up
up:
	docker-compose up -d
	docker-compose logs -f

.PHONY: down
down:
	docker-compose down

.PHONY: build
build:
	docker-compose build

.PHONY: debug
debug:
	docker-compose logs -f worker
