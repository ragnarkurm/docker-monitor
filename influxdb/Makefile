CONTAINER = influxsrv
BASE = /www/monitor/influxdb
USERFILE = user.txt
PASSFILE = pass.txt

start_public:
	make start START_FLAGS='-p 8083:8083 -p 8086:8086'

build: stop
	echo -n "cadvisor" > "$(USERFILE)"
	pwgen -s 20 1 > "$(PASSFILE)"
	sudo rm -rf data
	mkdir data
	make start -e START_FLAGS="-e ADMIN_USER=\"`cat $(USERFILE)`\" -e INFLUXDB_INIT_PWD=\"`cat $(PASSFILE)`\" -v \"$(BASE)/build.influxql:/init_script.influxql:ro\""
	./waitbuild "$(CONTAINER)"
	make stop

start: stop
	docker run \
	--detach=true \
	$(START_FLAGS) \
	--expose 8083 \
	--expose 8086 \
	--expose 8090 \
	--expose 8099 \
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