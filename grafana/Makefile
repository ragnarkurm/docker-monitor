BASE = /www/monitor/grafana
CONTAINER = grafana
USERFILE = user.txt
PASSFILE = pass.txt

start: stop
	docker \
	run \
	-d \
	-p 3000:3000 \
	-e INFLUXDB_HOST=influxsrv \
	-e INFLUXDB_PORT=8086 \
	-e INFLUXDB_NAME=cadvisor \
	-e INFLUXDB_USER="`cat $(USERFILE)`" \
	-e INFLUXDB_PASS="`cat $(PASSFILE)`" \
	--link influxsrv:influxsrv \
	-v "$(BASE)/data:/var/lib/grafana" \
	-v "$(BASE)/logs:/var/log/grafana" \
	--name "$(CONTAINER)" \
	grafana/grafana
	./waitbuild "$(CONTAINER)"

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

console:
	docker logs -f "$(CONTAINER)"
