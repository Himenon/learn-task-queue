.PHONY: up
up:
	docker-compose up -d

.PHONY: htop
htop:
	docker-compose run inspector

.PHONY: conn
conn:
	docker exec -it $(shell docker ps --filter name=learn002_worker -q) bash
