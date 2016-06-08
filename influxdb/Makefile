CONTAINER = influx-server
BASE = /monitoring/influxdb
IP = 194.204.13.108

start_public:
	make start START_FLAGS='-p 8083:8083 -p 8086:8086'

build: stop
	sudo rm -rf data
	mkdir data
	make start
	./waitbuild "$(CONTAINER)"
	make stop

start: stop
	docker run \
		--detach \
		--env TERM=xterm \
		--expose 8086 \
		--name "$(CONTAINER)" \
		--publish "${IP}:8086:8086" \
		--restart unless-stopped \
		--volume "$(BASE)/data:/data" \
		--volume ~/.bash_history:/root/.bash_history \
		tutum/influxdb

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

cli:
	docker exec \
		-ti \
		$(CONTAINER) \
		/usr/bin/influx

console:
	docker logs \
		-f "$(CONTAINER)"

shell:
	docker exec \
		-it \
		"$(CONTAINER)"
		/bin/bash
