import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print("La temperatura es en º % celsius" % temperature)
    time.sleep(3)
