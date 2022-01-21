import random
import os
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS


custom_bucket = "python_test"
url = os.getenv("INFLUXDB_URL", "http://localhost:8086")
token = os.getenv("INFLUXDB_TOKEN", "3i3v9zbkdueLxSdsjHMEZOz4qtrAWw0Qe18wOWGCFK1Z_GAb5zGkQ6MQxkSPqSTd-tpIGjxyv88k2MEmEbw1nw==")
org = os.getenv("INFLUXDB_ORGID", "a38482cc54f932aa")

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

clients = ["lighton", "ix-labs", "sony", "dassault", "babbar"]
models = ["orion-fr", "lyra-en", "orion-en", "orion-it"]
endpoints = ["create", "analyze", "summarize", "represent"]

random_tokens = random.randint(100,300)
random_client = random.randint(0,4)
random_model = random.randint(0,3)
random_endpoint = random.randint(0,3)
random_client_name = clients[random_client]
random_model_name = models[random_model]
random_endpoint_name = endpoints[random_endpoint]

print(f"{random_client_name} --> {random_model_name} --> {random_endpoint_name}")

_output = [
              f"token_count,client={random_client_name},model={random_model_name},endpoint={random_endpoint_name},skill=none token_count={random_tokens}i",
              f"requests,client={random_client_name},model={random_model_name},endpoint={random_endpoint_name},skill=none count=1i",
              f"batch_tiemout,client={random_client_name},model={random_model_name},endpoint={random_endpoint_name},skill=none count=0i"
              ]

write_api.write(bucket=custom_bucket, record=[_output])

client.close()

