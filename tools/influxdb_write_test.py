# # from influxdb_client import InfluxDBClient
# from influxdb_client import InfluxDBClient, Point, WriteOptions
# # #from influxdb_client.client.write_api import SYNCHRONOUS
# from influxdb_client.client.write_api import ASYNCHRONOUS
# #
# client = InfluxDBClient(url="http://localhost:9999", token="3i3v9zbkdueLxSdsjHMEZOz4qtrAWw0Qe18wOWGCFK1Z_GAb5zGkQ6MQxkSPqSTd-tpIGjxyv88k2MEmEbw1nw==", org="a38482cc54f932aa")
# #
# # #  instantiate the WriteAPI
# write_api = client.write_api()
# #
# # # Specify Write Options
# #
# # #write_api = client.write_api(write_options=SYNCHRONOUS)
# write_api = client.write_api(write_options=ASYNCHRONOUS)
# write_api = client.write_api(write_options=WriteOptions(batch_size=500, flush_interval=10_000, jitter_interval=2_000, retry_interval=5_000))
# #
# write_api.write("python_test", "a38482cc54f932aa", [{"measurement": "h2o_feet", "tags": {"location": "coyote_creek"}, "fields": {"water_level": 1}, "time": 1}])
# #


########################

from influxdb_client import InfluxDBClient, Point, WriteOptions

org = "a38482cc54f932aa"
bucket = "python_test"
token = "3i3v9zbkdueLxSdsjHMEZOz4qtrAWw0Qe18wOWGCFK1Z_GAb5zGkQ6MQxkSPqSTd-tpIGjxyv88k2MEmEbw1nw=="
query = 'from(bucket: python_test)\
|> range(start: -10m)\
|> filter(fn: (r) => r._measurement == "h2o_level")\
|> filter(fn: (r) => r._field == "water_level")\
|> filter(fn: (r) => r.location == "coyote_creek")'

#establish a connection
client = InfluxDBClient(url="http://localhost:9999", token=token, org=org)

#instantiate the WriteAPI and QueryAPI
write_api = client.write_api()
query_api = client.query_api()
#create and write the point
p = Point("h2o_feet").tag("location", "coyote_creek").field("water_level", 1)
write_api.write(bucket=bucket,org=org,record=p)
#return the table and print the result
result = client.query_api().query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_value(), record.get_field()))
print(results)
