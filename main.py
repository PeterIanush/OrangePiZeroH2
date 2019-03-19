import ctypes
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

mod = ctypes.cdll.LoadLibrary('/root/OneWire/onewire.so')
wire = mod.new_(15)

def getTemp(device):
    list = (ctypes.c_uint8 * 9)()

    while True:
        mod.setDevice(wire, ctypes.c_uint64(device))
        mod.writeByte(wire, 68) #CONVERTEMP
        sleep(1)
        mod.setDevice(wire, ctypes.c_uint64(device))
        mod.writeByte(wire, 16*11+14)

        for i in range(0, 9):
            list[i] = mod.readByte(wire)

        c_8 = mod.crc8_(wire, list, 8)

        if c_8 == list[8]:
            break


    return ((list[1] << 8) + list[0]) * 0.0625  

def blink3():
    gpio.init()
    blink = port.PA7
    gpio.setcfg(blink, gpio.OUTPUT)

    gpio.output(blink, gpio.HIGH)

    sleep(0.03)
    gpio.output(blink, gpio.LOW)
    sleep(0.03)


try:
    mod.oneWireInit(wire)
    therm = 0.0
    c_n = ctypes.c_int(100)
    list = (ctypes.c_uint64 * 100)()
    mod.searchRom(wire, list, ctypes.byref(c_n))
    print('----------------------')
    print('devices = %s' % c_n.value)
    print('----------------------')
    for i in range(0, c_n.value):
        print ('addr T[%s] = %s' % (i + 1, list[i]))    
    print('----------------------')
    while True:
      for i in range(0, c_n.value):
          temperature = getTemp(list[i])
          print("T[%s] = %s C" % (i + 1, temperature))
          blink3()
      sleep(1)

except:
   print("Incorect temperature")


 


