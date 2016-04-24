start: stop
	make -C influxdb start
	make -C cadvisor start
	make -C custom start
	make -C grafana start

stop:
	make -C grafana stop
	make -C custom stop
	make -C cadvisor stop
	make -C influxdb stop
