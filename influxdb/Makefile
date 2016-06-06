CONTAINER = influx-server
BASE = /monitoring/influxdb
IP = 127.0.0.1

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
	--detach=true \
	--publish="${IP}:8086:8086" \
	--expose 8086 \
	-e TERM=xterm \
	-v ~/.bash_history:/root/.bash_history \
	--restart=unless-stopped \
	--name "$(CONTAINER)" \
	--volume="$(BASE)/data:/data" \
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
	docker logs -f "$(CONTAINER)"
