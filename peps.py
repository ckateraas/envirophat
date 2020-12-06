#! /usr/bin/env python3

from prometheus_client import start_http_server, Summary, Gauge
import random
import time
from envirophat import weather, light

temp_gauge = Gauge('kitchen_temp', 'Temperature in the kitchen')
light_gauge = Gauge('kitchen_light', 'Light in the kitchen', ['color'])
pressure_gauge = Gauge('kitchen_pressure', 'Pressure in the kitchen')

# Unused envirophat functions
# motion.magnetometer()
# motion.heading()

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        temp_gauge.set(round(weather.temperature(), 1))
        light_gauge.labels('red').set(light.rgb()[0])
        light_gauge.labels('green').set(light.rgb()[1])
        light_gauge.labels('blue').set(light.rgb()[2])
        pressure_gauge.set(round(weather.pressure(), 1))
        time.sleep(5)
