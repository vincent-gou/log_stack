#!/bin/sh

set -e
sleep 2
#influx config ls
TOKEN=$DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
INFLUXDB_BUCKET_ID=$(influx bucket list -n influxdb_metrics --hide-headers | awk '{print $1}')
INFLUXDB_BUCKET_ORGID=$(influx bucket list -n influxdb_metrics --hide-headers | awk '{print $5}')

#influx config ls

# port is set to 9999 since it's default while initializing before restart after user script execution
curl http://localhost:9999/api/v2/scrapers -X POST \
  -H 'Content-Type: application/json' -H 'Accept: application/json' \
  -H "Authorization: Token ${DOCKER_INFLUXDB_INIT_ADMIN_TOKEN}" \
  -d '{"allowInsecure":true,"bucketID":"'$INFLUXDB_BUCKET_ID'","name":"influxdb_scrapper","orgID":"'$INFLUXDB_BUCKET_ORGID'","type":"prometheus","url":"http://influxdb:8086/metrics"}'


