#!/bin/sh

set -e
RETENTION_POLICY="90d"
BUCKET_NAME="muse_metrics"
TOKEN=$DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
ORG=$DOCKER_INFLUXDB_INIT_ORG
#influx bucket create -n $BUCKET_NAME -r $RETENTION_POLICY --org $ORG --token $TOKEN
#sleep 2
BUCKET_ID=$(influx bucket list -n $BUCKET_NAME --hide-headers --org $ORG --token $TOKEN | awk '{print $1}')
influx v1 dbrp create --db $BUCKET_NAME --rp $RETENTION_POLICY --bucket-id $BUCKET_ID --org $ORG --token $TOKEN


RETENTION_POLICY="30d"
BUCKET_NAME="muse_system_metrics"
TOKEN=$DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
ORG=$DOCKER_INFLUXDB_INIT_ORG
#influx bucket create -n $BUCKET_NAME -r $RETENTION_POLICY --org $ORG --token $TOKEN
#sleep 2
BUCKET_ID=$(influx bucket list -n $BUCKET_NAME --hide-headers --org $ORG --token $TOKEN | awk '{print $1}')
influx v1 dbrp create --db $BUCKET_NAME --rp $RETENTION_POLICY --bucket-id $BUCKET_ID --org $ORG --token $TOKEN