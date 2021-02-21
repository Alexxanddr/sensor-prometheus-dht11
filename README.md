# sensor-prometheus-dht11

Simple python script to scrape and expose the metrics for the Temperature and Humidity from the Sensor Adafruit DHT22 with Prometheus syntax.

There are two files:
- sensor.py - Metrics exposed locally 
- sendtogateway.py - Push metrics to the Prometheus push GW

- Enable I2C on the raspberry
- Install required module with: `pip3 install -r requirements.txt`
- python3 sensor.py 
