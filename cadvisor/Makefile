CONTAINER = cadvisor
USERFILE = user.txt
PASSFILE = pass.txt

start_public: stop
	make start START_FLAGS="--publish=8080:8080"

start: stop
	docker run \
	--volume=/:/rootfs:ro \
	--volume=/var/run:/var/run:rw \
	--volume=/sys:/sys:ro \
	--volume=/var/lib/docker/:/var/lib/docker:ro \
	--link influxsrv:influxsrv \
	-e TERM=xterm \
	$(START_FLAGS) \
	--detach=true \
	--name="$(CONTAINER)" \
	google/cadvisor:latest \
	--log_cadvisor_usage=false \
	-storage_driver=influxdb \
	-storage_driver_host=influxsrv:8086 \
	-storage_driver_db=cadvisor \
	-storage_driver_user="`cat $(USERFILE)`" \
	-storage_driver_password="`cat $(PASSFILE)`"
	./waitbuild "$(CONTAINER)"

stop:
	@echo "Stopping container: $(CONTAINER)"
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker stop
	@docker ps -a --filter name="$(CONTAINER)" --format '{{.ID}}' | xargs -r docker rm

shell:
	docker exec -it "$(CONTAINER)" /bin/bash

console:
	docker logs -f "$(CONTAINER)"
