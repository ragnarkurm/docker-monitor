BASE = /monitoring/custom
CONTAINER = monitoring-custom

start: stop
	docker run \
		--detach \
		--env TERM=xterm \
		--log-driver syslog \
		--log-opt "tag=$(CONTAINER)" \
		--name "$(CONTAINER)" \
		--privileged \
		--restart unless-stopped \
		--volume ~/.bash_history:/root/.bash_history \
		--volume "$(BASE)/app:/app" \
		--volume /proc:/host/proc \
		--volume /var/run/docker.sock:/var/run/docker.sock \
		python-influxdb-docker-pkg \
		/app/monitor /app/monitor.conf

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

ps:
	@docker ps --filter name="$(CONTAINER)"

console:
	docker logs \
		-f "$(CONTAINER)"

shell:
	docker exec \
		-it \
		"$(CONTAINER)"
		/bin/bash
