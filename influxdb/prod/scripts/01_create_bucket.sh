#!/bin/sh

set -e
influx bucket create -n loki_metrics -r 7d
influx bucket create -n influxdb_metrics -r 7d
influx bucket create -n grafana_metrics -r 7d
#influx config ls

influx bucket create -n muse_metrics -r 90d
influx bucket create -n muse_system_metrics -r 30d
