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
    	response1 = requests.post('https://[URL-PROMETHEUS-PUSHGW]:[PORT]/metrics/job/{j}/instance/{i}/provider/{p}'.format(j=job_name, i=instance_name, p=provider), data='{k} {v}\n'.format(k=temperature_key, v=temperature_value),auth=('[BASIC_AUTH_PUSHGW]', '[BASICPASS_AUH_PUSHGW]'))
    	response2 = requests.post('https://[URL-PROMETHEUS-PUSHGW]:[PORT]/metrics/job/{j}/instance/{i}/provider/{p}'.format(j=job_name, i=instance_name, p=provider), data='{k} {v}\n'.format(k=humidity_key, v=humidity_value),auth=('[BASIC_AUTH_PUSHGW]', '[BASICPASS_AUH_PUSHGW]'))
   

sendData()
