BASE = /monitoring/custom
CONTAINER = monitor-custom

start: stop
	docker \
		run \
		--detach=true \
		--link influx-server:influx-server \
		-e TERM=xterm \
		--restart=unless-stopped \
		-v ~/.bash_history:/root/.bash_history \
		-v "$(BASE)/container-bin:/usr/local/bin" \
		-v /proc:/host/proc \
		--name "$(CONTAINER)" \
		python-influxdb-pkg \
		/usr/local/bin/monitor

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

console:
	docker logs -f "$(CONTAINER)"
