#!/bin/sh

set -e
influx bucket create -n loki_metrics -r 7d
influx bucket create -n influxdb_metrics -r 7d
influx bucket create -n grafana_metrics -r 7d
#influx config ls
