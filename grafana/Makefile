BASE = /www/monitor/grafana
CONTAINER = grafana
USERFILE = user.txt
PASSFILE = pass.txt

start: stop
	docker run \
		--detach \
		--env INFLUXDB_HOST=influxsrv \
		--env INFLUXDB_NAME=cadvisor \
		--env INFLUXDB_PASS="`cat $(PASSFILE)`" \
		--env INFLUXDB_PORT=8086 \
		--env INFLUXDB_USER="`cat $(USERFILE)`" \
		--env TERM=xterm \
		--link influxsrv:influxsrv \
		--log-driver=syslog \
		--log-opt tag=$(WEB_CONTAINER) \
		--name "$(CONTAINER)" \
		--publish 3000:3000 \
		--restart unless-stopped \
		--volume "$(BASE)/data:/var/lib/grafana" \
		--volume "$(BASE)/logs:/var/log/grafana" \
		--volume ~/.bash_history:/root/.bash_history \
		grafana/grafana
		./waitbuild "$(CONTAINER)"

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

console:
	docker logs -f "$(CONTAINER)"
