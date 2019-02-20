from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks

neo =Gpio()

S0 = 2 # pin to use
S1 = 3
S2 = 4
S3 = 5

pinNum = [S0, S1, S2, S3]

num = [0,0,0,0]

# Blink example
for i in range(4):
    neo.pinMode(pinNum[i], neo.OUTPUT)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 0)
neo.digitalWrite(pinNum[2], 0)
neo.digitalWrite(pinNum[3], 0)

while True:
    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    v = raw * scale
    # t = (v - 590)/10
    # sleep(1)
    print(v)

# neo.digitalWrite(pinNum[0], 1)
# neo.digitalWrite(pinNum[1], 0)
# neo.digitalWrite(pinNum[2], 0)
# neo.digitalWrite(pinNum[3], 0)
#
# neo.digitalWrite(pinNum[0], 0)
# neo.digitalWrite(pinNum[1], 1)
# neo.digitalWrite(pinNum[2], 0)
# neo.digitalWrite(pinNum[3], 0)
#
# neo.digitalWrite(pinNum[0], 1)
# neo.digitalWrite(pinNum[1], 1)
# neo.digitalWrite(pinNum[2], 0)
# neo.digitalWrite(pinNum[3], 0)
#
# neo.digitalWrite(pinNum[0], 0)
# neo.digitalWrite(pinNum[1], 0)
# neo.digitalWrite(pinNum[2], 1)
# neo.digitalWrite(pinNum[3], 0)
#
# neo.digitalWrite(pinNum[0], 1)
# neo.digitalWrite(pinNum[1], 0)
# neo.digitalWrite(pinNum[2], 1)
# neo.digitalWrite(pinNum[3], 0)
#
# neo.digitalWrite(pinNum[0], 0)
# neo.digitalWrite(pinNum[1], 1)
# neo.digitalWrite(pinNum[2], 1)
# neo.digitalWrite(pinNum[3], 0)
#
# neo.digitalWrite(pinNum[0], 1)
# neo.digitalWrite(pinNum[1], 1)
# neo.digitalWrite(pinNum[2], 1)
# neo.digitalWrite(pinNum[3], 0)
#
# neo.digitalWrite(pinNum[0], 0)
# neo.digitalWrite(pinNum[1], 0)
# neo.digitalWrite(pinNum[2], 0)
# neo.digitalWrite(pinNum[3], 1)
#
# neo.digitalWrite(pinNum[0], 1)
# neo.digitalWrite(pinNum[1], 0)
# neo.digitalWrite(pinNum[2], 0)
# neo.digitalWrite(pinNum[3], 1)
#
# neo.digitalWrite(pinNum[0], 0)
# neo.digitalWrite(pinNum[1], 1)
# neo.digitalWrite(pinNum[2], 0)
# neo.digitalWrite(pinNum[3], 1)
#
# neo.digitalWrite(pinNum[0], 1)
# neo.digitalWrite(pinNum[1], 1)
# neo.digitalWrite(pinNum[2], 0)
# neo.digitalWrite(pinNum[3], 1)
#
# neo.digitalWrite(pinNum[0], 0)
# neo.digitalWrite(pinNum[1], 0)
# neo.digitalWrite(pinNum[2], 1)
# neo.digitalWrite(pinNum[3], 1)
#
# neo.digitalWrite(pinNum[0], 1)
# neo.digitalWrite(pinNum[1], 0)
# neo.digitalWrite(pinNum[2], 1)
# neo.digitalWrite(pinNum[3], 1)
#
# neo.digitalWrite(pinNum[0], 0)
# neo.digitalWrite(pinNum[1], 1)
# neo.digitalWrite(pinNum[2], 1)
# neo.digitalWrite(pinNum[3], 1)
#
# neo.digitalWrite(pinNum[0], 1)
# neo.digitalWrite(pinNum[1], 1)
# neo.digitalWrite(pinNum[2], 1)
# neo.digitalWrite(pinNum[3], 1)



