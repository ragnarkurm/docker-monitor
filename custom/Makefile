BASE = /monitoring/custom
CONTAINER = monitor-custom

start: stop
	docker \
		run \
		--detach \
		--link influx-server:influx-server \
		--env TERM=xterm \
		--restart unless-stopped \
		--volume ~/.bash_history:/root/.bash_history \
		--volume "$(BASE)/container-bin:/monitoring" \
		--volume /proc:/host/proc \
		--name "$(CONTAINER)" \
		python-influxdb-pkg \
		/monitoring/monitor /monitoring/monitor.conf

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

console:
	docker logs -f "$(CONTAINER)"
