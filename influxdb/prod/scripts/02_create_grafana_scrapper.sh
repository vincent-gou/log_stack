#!/bin/sh

set -e
sleep 2
#influx config ls
TOKEN=$DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
GRAFANA_BUCKET_ID=$(influx bucket list -n grafana_metrics --hide-headers | awk '{print $1}')
GRAFANA_BUCKET_ORGID=$(influx bucket list -n grafana_metrics --hide-headers | awk '{print $5}')

#influx config ls

# port is set to 9999 since it's default while initializing before restart after user script execution
curl http://localhost:9999/api/v2/scrapers -X POST \
  -H 'Content-Type: application/json' -H 'Accept: application/json' \
  -H "Authorization: Token ${DOCKER_INFLUXDB_INIT_ADMIN_TOKEN}" \
  -d '{"allowInsecure":true,"bucketID":"'$GRAFANA_BUCKET_ID'","name":"grafana_scrapper","orgID":"'$GRAFANA_BUCKET_ORGID'","type":"prometheus","url":"http://grafana:3000/metrics"}'


