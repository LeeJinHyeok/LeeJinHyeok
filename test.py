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



while True:
    neo.digitalWrite(pinNum[0], 0)
    neo.digitalWrite(pinNum[1], 0)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)
    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    v = raw * scale
    t = (v - 590)/10

    temp = (t * 1.8) + 32
    print(temp)

    # Alphasense SN1
    neo.digitalWrite(pinNum[0], 0)
    neo.digitalWrite(pinNum[1], 1)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c2 = raw * scale

    neo.digitalWrite(pinNum[0], 1)
    neo.digitalWrite(pinNum[1], 1)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c3 = raw * scale

    SN1 = ((c2 - 286) - (0.75 * (c3 - 292))) *3.876
    SN1 = SN1 if (SN1 >= 0) else -SN1
    print(SN1)

    # Alphasense SN2
    neo.digitalWrite(pinNum[0], 0)
    neo.digitalWrite(pinNum[1], 0)
    neo.digitalWrite(pinNum[2], 1)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c4 = raw * scale

    neo.digitalWrite(pinNum[0], 1)
    neo.digitalWrite(pinNum[1], 0)
    neo.digitalWrite(pinNum[2], 1)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c5 = raw * scale

    SN2 = ((c4 - 417) - (0.5 * (c5 - 402))) * 2.5445
    SN2 = SN2 if (SN2 >= 0) else -SN2
    print(SN2)

    # Alphasense SN3
    neo.digitalWrite(pinNum[0], 0)
    neo.digitalWrite(pinNum[1], 1)
    neo.digitalWrite(pinNum[2], 1)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c6 = raw * scale

    neo.digitalWrite(pinNum[0], 1)
    neo.digitalWrite(pinNum[1], 1)
    neo.digitalWrite(pinNum[2], 1)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c7 = raw * scale

    SN3 = ((c6 - 265) - (0.44 * (c7 - 281))) *3.4246
    SN3 = SN3 if (SN3 >= 0) else -SN3
    print(SN3)

    # Alphasense SN4
    neo.digitalWrite(pinNum[0], 0)
    neo.digitalWrite(pinNum[1], 0)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 1)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c8 = raw * scale

    neo.digitalWrite(pinNum[0], 1)
    neo.digitalWrite(pinNum[1], 0)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 1)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c9 = raw * scale

    SN4 = ((c8 - 275) - (0.6 * (c9 - 295)))*3.4722
    SN4 = SN4 if (SN4 >= 0) else -SN4
    print(SN4)

    # PM2.5
    neo.digitalWrite(pinNum[0], 1)
    neo.digitalWrite(pinNum[1], 1)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 1)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c11 = (raw * scale) / 1000

    hppcf = (240.0 * pow(c11, 6) - (2491.3 * pow(c11, 5)) + 9448.7 * pow(c11, 4) - (14840.0 * pow(c11, 3)) + 10684.0 * pow(
        c11, 2) + 2211.8 * (c11) + 7.9623)
    PM25 = 0.518 + (0.00274 * hppcf)
    print(PM25)

    # AQI Convesion for NO2_SN1
    if SN1 >= 0 and SN1 <= 53:
        AQI_NO2 = ((50 - 0) * (SN1 - 0)) / (53 - 0) + 0
    elif SN1 >= 54 and SN1 <= 100:
        AQI_NO2 = ((100 - 51) * (SN1 - 54)) / (100 - 54) + 51
    elif SN1 >= 101 and SN1 <= 360:
        AQI_NO2 = ((150 - 101) * (SN1 - 101)) / (360 - 101) + 101
    elif SN1 >= 361 and SN1 <= 649:
        AQI_NO2 = ((200 - 151) * (SN1 - 361)) / (649 - 361) + 151
    elif SN1 >= 650 and SN1 <= 1249:
        AQI_NO2 = ((300 - 201) * (SN1 - 650)) / (1249 - 650) + 201
    elif SN1 >= 1250 and SN1 <= 1649:
        AQI_NO2 = ((400 - 301) * (SN1 - 1250)) / (1649 - 1250) + 301
    elif SN1 >= 1650 and SN1 <= 2049:
        AQI_NO2 = ((500 - 401) * (SN1 - 1650)) / (2049 - 1650) + 401
    else:
        AQI_NO2 = 500
    print('')

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
