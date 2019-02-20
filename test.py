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
    neo.digitalWrite(pinNum[0], 1)
    neo.digitalWrite(pinNum[1], 0)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 0)
    sleep(1)
    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    v = raw * scale
    t = (v - 590)/10

    temp = (t * 1.8) + 32
    print(temp)

#     neo.digitalWrite(pinNum[0], 0)
#     neo.digitalWrite(pinNum[1], 1)
#     neo.digitalWrite(pinNum[2], 0)
#     neo.digitalWrite(pinNum[3], 0)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c2 = raw * scale
#
#     neo.digitalWrite(pinNum[0], 1)
#     neo.digitalWrite(pinNum[1], 1)
#     neo.digitalWrite(pinNum[2], 0)
#     neo.digitalWrite(pinNum[3], 0)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c3 = raw * scale
#
#     SN1 = ((c2 - 286) - 0.75 * (c3 - 292)) / 0.258
#     print(SN1)
#
#     # Alphasense SN2
#     neo.digitalWrite(pinNum[0], 0)
#     neo.digitalWrite(pinNum[1], 0)
#     neo.digitalWrite(pinNum[2], 1)
#     neo.digitalWrite(pinNum[3], 0)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c4 = raw * scale
#
#     neo.digitalWrite(pinNum[0], 1)
#     neo.digitalWrite(pinNum[1], 0)
#     neo.digitalWrite(pinNum[2], 1)
#     neo.digitalWrite(pinNum[3], 0)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c5 = raw * scale
#
#     SN2 = ((c4 - 417) - 0.5 * (c5 - 402)) / 0.393
#     print(SN2)
#
#     # Alphasense SN3
#     neo.digitalWrite(pinNum[0], 0)
#     neo.digitalWrite(pinNum[1], 1)
#     neo.digitalWrite(pinNum[2], 1)
#     neo.digitalWrite(pinNum[3], 0)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c6 = raw * scale
#
#     neo.digitalWrite(pinNum[0], 1)
#     neo.digitalWrite(pinNum[1], 1)
#     neo.digitalWrite(pinNum[2], 1)
#     neo.digitalWrite(pinNum[3], 0)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c7 = raw * scale
#
#     SN3 = ((c6 - 265) - 0.44 * (c7 - 281)) / 0.292
#     print(SN3)
#
#     # Alphasense SN4
#     neo.digitalWrite(pinNum[0], 0)
#     neo.digitalWrite(pinNum[1], 0)
#     neo.digitalWrite(pinNum[2], 0)
#     neo.digitalWrite(pinNum[3], 1)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c8 = raw * scale
#
#     neo.digitalWrite(pinNum[0], 1)
#     neo.digitalWrite(pinNum[1], 0)
#     neo.digitalWrite(pinNum[2], 0)
#     neo.digitalWrite(pinNum[3], 1)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c9 = raw * scale
#
#     SN4 = ((c8 - 275) - 0.6 * (c9 - 295))
#     print(SN4)
#
#     # PM2.5
#     neo.digitalWrite(pinNum[0], 1)
#     neo.digitalWrite(pinNum[1], 1)
#     neo.digitalWrite(pinNum[2], 0)
#     neo.digitalWrite(pinNum[3], 1)
#     sleep(0.05)
#
#     raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
#     scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
#     c11 = (raw * scale) / 1000
#
#     hppcf = (240.0 * pow(c11, 6) - 2491.3 * pow(c11, 5) + 9448.7 * pow(c11, 4) - 14840.0 * pow(c11, 3) + 10684.0 * pow(
#         c11, 2) + 2211.8 * (c11) + 7.9623)
#     PM25 = 0.518 + .00274 * hppcf
#     print(PM25)
#
# # neo.digitalWrite(pinNum[0], 1)
# # neo.digitalWrite(pinNum[1], 0)
# # neo.digitalWrite(pinNum[2], 0)
# # neo.digitalWrite(pinNum[3], 0)
# #
# # neo.digitalWrite(pinNum[0], 0)
# # neo.digitalWrite(pinNum[1], 1)
# # neo.digitalWrite(pinNum[2], 0)
# # neo.digitalWrite(pinNum[3], 0)
# #
# # neo.digitalWrite(pinNum[0], 1)
# # neo.digitalWrite(pinNum[1], 1)
# # neo.digitalWrite(pinNum[2], 0)
# # neo.digitalWrite(pinNum[3], 0)
# #
# # neo.digitalWrite(pinNum[0], 0)
# # neo.digitalWrite(pinNum[1], 0)
# # neo.digitalWrite(pinNum[2], 1)
# # neo.digitalWrite(pinNum[3], 0)
# #
# # neo.digitalWrite(pinNum[0], 1)
# # neo.digitalWrite(pinNum[1], 0)
# # neo.digitalWrite(pinNum[2], 1)
# # neo.digitalWrite(pinNum[3], 0)
# #
# # neo.digitalWrite(pinNum[0], 0)
# # neo.digitalWrite(pinNum[1], 1)
# # neo.digitalWrite(pinNum[2], 1)
# # neo.digitalWrite(pinNum[3], 0)
# #
# # neo.digitalWrite(pinNum[0], 1)
# # neo.digitalWrite(pinNum[1], 1)
# # neo.digitalWrite(pinNum[2], 1)
# # neo.digitalWrite(pinNum[3], 0)
# #
# # neo.digitalWrite(pinNum[0], 0)
# # neo.digitalWrite(pinNum[1], 0)
# # neo.digitalWrite(pinNum[2], 0)
# # neo.digitalWrite(pinNum[3], 1)
# #
# # neo.digitalWrite(pinNum[0], 1)
# # neo.digitalWrite(pinNum[1], 0)
# # neo.digitalWrite(pinNum[2], 0)
# # neo.digitalWrite(pinNum[3], 1)
# #
# # neo.digitalWrite(pinNum[0], 0)
# # neo.digitalWrite(pinNum[1], 1)
# # neo.digitalWrite(pinNum[2], 0)
# # neo.digitalWrite(pinNum[3], 1)
# #
# # neo.digitalWrite(pinNum[0], 1)
# # neo.digitalWrite(pinNum[1], 1)
# # neo.digitalWrite(pinNum[2], 0)
# # neo.digitalWrite(pinNum[3], 1)
# #
# # neo.digitalWrite(pinNum[0], 0)
# # neo.digitalWrite(pinNum[1], 0)
# # neo.digitalWrite(pinNum[2], 1)
# # neo.digitalWrite(pinNum[3], 1)
# #
# # neo.digitalWrite(pinNum[0], 1)
# # neo.digitalWrite(pinNum[1], 0)
# # neo.digitalWrite(pinNum[2], 1)
# # neo.digitalWrite(pinNum[3], 1)
# #
# # neo.digitalWrite(pinNum[0], 0)
# # neo.digitalWrite(pinNum[1], 1)
# # neo.digitalWrite(pinNum[2], 1)
# # neo.digitalWrite(pinNum[3], 1)
# #
# # neo.digitalWrite(pinNum[0], 1)
# # neo.digitalWrite(pinNum[1], 1)
# # neo.digitalWrite(pinNum[2], 1)
# # neo.digitalWrite(pinNum[3], 1)
#
#
#
