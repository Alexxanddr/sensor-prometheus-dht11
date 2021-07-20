import subprocess,re,os,time
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
import board
import adafruit_dht


INFLUXDB_HOST="influxdb.internal.south.dns-cloud.net"
INFLUXDB_PORT="80"
INFLUXDB_USERNAME=""
INFLUXDB_PASSWORD=""
INFLUXDB_DATABASE="temperature"
points=[]

dhtDevice = adafruit_dht.DHT22(board.D2)
temperature = dhtDevice.temperature
humidity = dhtDevice.humidity

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    client.create_database(INFLUXDB_DATABASE)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    print("InfluxDB connection failed: %s" % (err))
    sys.exit()

json_body = [{
            "measurement": "temperature",
            "tags": {
                "room": "alexxanddr"
            },
            "fields": {
                "value": temperature
            }
        },
        {
            "measurement": "humidity",
            "tags": {
                "room": "alexxanddr"
            },
            "fields": {
                "value": humidity
            }
        }]

client.write_points(json_body)
