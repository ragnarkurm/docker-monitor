BASE = /www/monitor/custom
CONTAINER = monitor-custom

start: stop
	docker \
		run \
		--detach=true \
		--link influxsrv:influxsrv \
		-v "$(BASE)/load:/load" \
		--name "$(CONTAINER)" \
		monitoring-custom-pkg \
		/load

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

console:
	docker logs -f "$(CONTAINER)"