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
########################### N table ###################################
#array for calculate alph
#temp              -30,  -20   -10     0    10     20   30    40    50
#index               0,    1,    2,    3,    4,    5,    6,    7 ,   8
O3_tempArray  = [ 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 2.87]
SO2_tempArray = [ 0.85, 0.85, 0.85, 0.85, 0.85, 1.15, 1.45, 1.75, 1.95]
NO2_tempArray = [ 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 2.00, 2.70]
CO_tempArray  = [ 1.40, 1.03, 0.85, 0.62, 0.30, 0.03,-0.25,-0.48,-0.80]
#######################################################################

def get_alpha(temper, air): #air = NO2,O3, CO, SO2
    temper
    i=0 #index
    mulx=0 # multiple #times
    if(-30<=temper<-20):
        i = 0;
        mulx = temper + 30  # ex -28'C + 30 = 2 >> 2
    elif(-20<=temper<-10):
        i = 1;
        mulx = temper + 20
    elif (-10 <= temper < 0):
        i = 2;
        mulx = temper + 10
    elif (0 <= temper < 10):
        i = 3;
        mulx = temper
    elif (10 <= temper < 20):
        i = 4;
        mulx = temper -10
    elif (20 <= temper < 30):
        i = 5;
        mulx = temper -20
    elif (30 <= temper < 40):
        i = 6;
        mulx = temper -30
    elif (40 <= temper < 50):
        i = 7;
        mulx = temper - 40
    elif (50 <= temper):
        i = 8; # if temperature exceed 50 just give 50'C data

    N =0.0
    if(air == 'O3'):
        if(i==8):
            N=O3_tempArray[i]
        else:
            tmp=( O3_tempArray[i + 1] - O3_tempArray[i] ) / 10.0
            N=O3_tempArray[i] + (tmp * mulx)

    elif(air == 'CO'):
        if(i==8):
            N=CO_tempArray[i]
        else:
            tmp=( CO_tempArray[i + 1] - CO_tempArray[i] ) / 10.0
            N=CO_tempArray[i] + (tmp * mulx)

    elif(air == 'NO2'):
        if(i==8):
            N=NO2_tempArray[i]
        else:
            tmp=( NO2_tempArray[i + 1] - NO2_tempArray[i] ) / 10.0
            N=NO2_tempArray[i] + (tmp * mulx)

    elif (air == 'SO2'):
        if(i==8):
            N=SO2_tempArray[i]
        else:
            tmp=( SO2_tempArray[i + 1] - SO2_tempArray[i] ) / 10.0
            N=SO2_tempArray[i] + (tmp * mulx)

    return N



while True:
    neo.digitalWrite(pinNum[0], 0)
    neo.digitalWrite(pinNum[1], 0)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)
    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c0= raw * scale
    temp_celsius = (c0 - 630) / 10 -32
    temp = (temp_celsius * 1.8) + 32
    print(temp_celsius)
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

    SN1 = ((c2 - 286) - (get_alpha(temp_celsius, 'NO2')) * (c3 - 292)) * 3.876
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

    SN2 = ((c4 - 417) - (get_alpha(temp_celsius, 'O3')) * (c5 - 402)) * 2.5445
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

    SN3 = ((c6 - 265) - (get_alpha(temp_celsius, 'CO')) * (c7 - 281)) * 3.4246
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

    SN4 = ((c8 - 275) - (get_alpha(temp_celsius, 'SO2')) * (c9 - 295)) * 3.4722
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

    hppcf = (240.0 * pow(c11, 6) - (2491.3 * pow(c11, 5)) + 9448.7 * pow(c11, 4) - (14840.0 * pow(c11, 3)) + 10684.0 * pow(c11, 2) + 2211.8 * (c11) + 7.9623)
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
    print(AQI_NO2)
    print('')
    sleep(2.5)

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
