from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks



while True:

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    v = raw * scale
    t = (v - 590)/10

    temp = (t * 1.8) + 32
    sleep(1)
    print(t)
    print(temp)
