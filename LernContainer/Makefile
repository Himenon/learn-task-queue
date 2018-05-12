.PHONY: docker-setup
docker-setup:
	docker build -t inspector . -f Dockerfile.inspect
	docker build -t looper . -f Dockerfile.python
	docker pull redis

.PHONY: run-redis
run-redis:
	docker run --name my-redis -d redis

.PHONY: run-looper
run-looper:
	docker run --name my-loop-ps -d looper

.PHONY: dev-looper
dev-looper:
	docker run -v $(shell pwd)/code:/code --name my-loop-ps -it --rm looper bash

.PHONY: run-loop-ps
run-loop-ps:
	docker run -v $(shell pwd)/code:/code --name my-loop-ps -it --rm looper bash

.PHONY: run-inspector-for-redis
run-inspector-for-redis:
	docker run --cap-add=SYS_PTRACE --security-opt seccomp:unconfined -it --pid=container:my-redis inspector bash

.PHONY: run-inspector-for-looper
run-inspector-for-looper:
	docker run -it --rm --pid=container:my-loop-ps inspector bash

.PHONY: clean
clean:
	docker rm -f my-redis my-loop-ps

.PHONY: vm-setup
vm-setup:
	sudo vagrant up --provision

.PHONY: vm-provision
vm-provision:
	sudo vagrant provision

.PHONY: vm-up
vm-up:
	sudo vagrant up

.PHONY: vm-ssh
vm-ssh:
	sudo vagrant ssh

.PHONY: vm-clean
vm-clean:
	sudo vagrant halt
	sudo vagrant destroy