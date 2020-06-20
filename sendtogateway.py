import board
import adafruit_dht
import time
import requests

job_name='sensor'
instance_name='raspberrypi'
provider='raspberry'
temperature_key='pihome_temperature'
humidity_key='pihome_humidity'

def sendData():
    dhtDevice = adafruit_dht.DHT22(board.D2)
    temperature_value=round(dhtDevice.temperature,2)
    humidity_value=round(dhtDevice.humidity,2)
    
    if humidity_value is not None and temperature_value is not None:
    	response1 = requests.post('https://pushgateway.sttfv.dns-cloud.net:9444/metrics/job/{j}/instance/{i}/provider/{p}'.format(j=job_name, i=instance_name, p=provider), data='{k} {v}\n'.format(k=temperature_key, v=temperature_value),auth=('asottile', 'iPod1993#'))
    	response2 = requests.post('https://pushgateway.sttfv.dns-cloud.net:9444/metrics/job/{j}/instance/{i}/provider/{p}'.format(j=job_name, i=instance_name, p=provider), data='{k} {v}\n'.format(k=humidity_key, v=humidity_value),auth=('asottile', 'iPod1993#'))
   

sendData()
