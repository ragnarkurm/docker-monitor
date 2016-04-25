BASE = /www/monitor/custom
CONTAINER = monitor-custom

start: stop
	docker \
		run \
		--detach=true \
		--link influxsrv:influxsrv \
		-e TERM=xterm \
		-v ~/.bash_history:/root/.bash_history \
		--restart=unless-stopped \
		-v "$(BASE)/container-bin:/usr/local/bin" \
		-v /proc:/host/proc \
		--name "$(CONTAINER)" \
		monitoring-custom-pkg \
		/usr/local/bin/monitor

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

console:
	docker logs -f "$(CONTAINER)"
