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

.PHONY: register-task
register-task:
	curl http://localhost:5000/task?task_id=1
