import Adafruit_DHT
from flask import Flask

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 2

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        dht11_data = f"""pihome_temperature {round(temperature,2)} 
pihome_humidity {round(humidity,2)}"""

    return f"{dht11_data}", 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
