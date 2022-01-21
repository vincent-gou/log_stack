# Informations

## Sources used

https://www.sqlpac.com/en/documents/influxdb-v2-getting-started-setup-preparing-migration-from-version-1.7.html

https://docs.influxdata.com/influxdb/v2.1/api/

# Administration commands

## Stop and purge all stack

project-dir$ docker-compose stop
project-dir$ docker-compose rm -f ; docker volume rm grafana-prod influxdb-prod loki-prod 

## connect container

docker exec -it influxdb-prod /bin/sh
docker exec -it grafana-prod /bin/sh
docker exec -it loki-prod /bin/sh


influx v1 dbrp create --db python_test --rp 7d --bucket-id a50b5e127deb4bce --default --org test --token 3i3v9zbkdueLxSdsjHMEZOz4qtrAWw0Qe18wOWGCFK1Z_GAb5zGkQ6MQxkSPqSTd-tpIGjxyv88k2MEmEbw1nw==


## Grafana

- [x] Autoprovision datasources
  - [x] Loki
  - [x] InfluxDB Flux
  - [x] InfluxDB influxQL

- [ ] Autoprovision Dashboards
- [ ] UI customizations


## InfluxDB
- [x] Create bucket on startup
- [x] Create scrapper from loki container
- [ ] Create alerts 
- [ ] Create Tasks
- [ ] Check InfluxDB internal metrics
- [ ] Create different users with different access rights on buckets

# To sort 
- [ ] Push promtail 
- [ ] config promtail labels by log files
- [ ] create promtail setup script by OS
   - [ ] Red-Hat / CentOS like OSes
   - [ ] Debian / Ubuntu like OSes
- [ ] Add Traefik container

# Security
- [ ] Do not expose influxDB listening port
- [ ] Do not expose
- [ ] Proxify request to Grafana through NGINX or Traefik
- [ ] Proxify request to LOKI through NGINX or Traefik


# InfluxDB write
## Python client

  `pip install influxdb-client`

Retrieve Auth token and OrgID

  
  `influx auth find`

  ID                      Description     Token                                                                                           User Name       User ID                 Permissions
  08c66ed39d1dc000        admin's Token   3i3v9zbkdueLxSdsjHMEZOz4qtrAWw0Qe18wOWGCFK1Z_GAb5zGkQ6MQxkSPqSTd-tpIGjxyv88k2MEmEbw1nw==        admin           08c66ed3799dc000        [read:/authorizations write:/authorizations read:/buckets write:/buckets read:/dashboards write:/dashboards read:/orgs write:/orgs read:/sources write:/sources read:/tasks write:/tasks read:/telegrafs write:/telegrafs read:/users write:/users read:/variables write:/variables read:/scrapers write:/scrapers read:/secrets write:/secrets read:/labels write:/labels read:/views write:/views read:/documents write:/documents read:/notificationRules write:/notificationRules read:/notificationEndpoints write:/notificationEndpoints read:/checks write:/checks read:/dbrp write:/dbrp read:/notebooks write:/notebooks read:/annotations write:/annotations]
  
  `influx org find`

  ID                      Name
  a38482cc54f932aa        test
