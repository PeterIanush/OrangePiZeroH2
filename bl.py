from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from w1thermsensor import W1ThermSensor

def temperature():
    for sensor in W1ThermSensor.get_available_sensors([W1ThermSensor.THERM_SENSOR_DS18B20]):
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

def blink():
    gpio.init()
    blink = port.PA13
    gpio.setcfg(blink, gpio.OUTPUT)

    gpio.output(blink, gpio.HIGH)

    sleep(0.1)
    gpio.output(blink, gpio.LOW)

def blink3():
    gpio.init()
    blink = port.PA7
    gpio.setcfg(blink, gpio.OUTPUT)

    gpio.output(blink, gpio.HIGH)

    sleep(0.03)
    gpio.output(blink, gpio.LOW)
    sleep(0.03)

def blink2():
    gpio.init()
    blink = port.PA10
    gpio.setcfg(blink, gpio.OUTPUT)
    gpio.output(blink, gpio.HIGH)
    sleep(1)
    gpio.output(blink, gpio.LOW)
temperature()
quant = 1
while quant < 20:
    quant = quant + 1
    print(quant)
    #blink()
    #blink2()
    blink3()
    
