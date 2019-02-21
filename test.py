from time import sleep, time
from neo import Gpio

########################### N table ###################################
# array for calculate alph
# temp              -30,  -20   -10     0    10     20   30    40    50
# index               0,    1,    2,    3,    4,    5,    6,    7 ,   8
O3_tempArray = [0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 2.87]
SO2_tempArray = [0.85, 0.85, 0.85, 0.85, 0.85, 1.15, 1.45, 1.75, 1.95]
NO2_tempArray = [1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 2.00, 2.70]
CO_tempArray = [1.40, 1.03, 0.85, 0.62, 0.30, 0.03, -0.25, -0.48, -0.80]


#######################################################################

def get_alpha(temper, air):  # air = NO2,O3, CO, SO2
    temper
    i = 0  # index
    mulx = 0  # multiple #times
    if (-30 <= temper < -20):
        i = 0;
        mulx = temper + 30  # ex -28'C + 30 = 2 >> 2
    elif (-20 <= temper < -10):
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
        mulx = temper - 10
    elif (20 <= temper < 30):
        i = 5;
        mulx = temper - 20
    elif (30 <= temper < 40):
        i = 6;
        mulx = temper - 30
    elif (40 <= temper < 50):
        i = 7;
        mulx = temper - 40
    elif (50 <= temper):
        i = 8;  # if temperature exceed 50 just give 50'C data

    N = 0.0
    if (air == 'O3'):
        if (i == 8):
            N = O3_tempArray[i]
        else:
            tmp = (O3_tempArray[i + 1] - O3_tempArray[i]) / 10.0
            N = O3_tempArray[i] + (tmp * mulx)

    elif (air == 'CO'):
        if (i == 8):
            N = CO_tempArray[i]
        else:
            tmp = (CO_tempArray[i + 1] - CO_tempArray[i]) / 10.0
            N = CO_tempArray[i] + (tmp * mulx)

    elif (air == 'NO2'):
        if (i == 8):
            N = NO2_tempArray[i]
        else:
            tmp = (NO2_tempArray[i + 1] - NO2_tempArray[i]) / 10.0
            N = NO2_tempArray[i] + (tmp * mulx)

    elif (air == 'SO2'):
        if (i == 8):
            N = SO2_tempArray[i]
        else:
            tmp = (SO2_tempArray[i + 1] - SO2_tempArray[i]) / 10.0
            N = SO2_tempArray[i] + (tmp * mulx)

    return N



############################ AQI table ##################################
#AQI              0-50,  51-100, 101-150, 151-200, 201-300, 301-400, 401-500
#index               0,       1,       2,       3,       4,       5,       6,
#MAX (038, O31, PM25, CO, SO2, NO2, AQI)
O3_8Max_AqiArray  = [54, 70, 85, 105, 200,  0,  0]
O3_1MaxAqiArray   = [ 0, 0, 164, 204, 404, 504, 604]
PM25_MaxAqiArray  = [12.0, 35.4, 55.4, 150.4, 250.4, 350.4, 500.4]
CO_MaxAqiArray    = [4.4, 9.4, 12.4, 15.4, 30.4, 40.4, 50.4]
SO2_MaxAqiArray   = [35, 75, 185, 304, 604, 804, 1004]
NO2_MaxAqiArray   = [53, 100, 360, 649, 1249, 1649, 2049]
Aqi_MaxAqiArray   = [50, 100, 150, 200, 300, 400, 500]

#MIN (038, O31, PM25, CO, SO2, NO2, AQI)
O3_8Min_AqiArray  = [0, 55, 71, 86, 106, 0, 0]
O3_1MinAqiArray   = [ 0, 0, 125, 165, 205, 405, 505]
PM25_MinAqiArray  = [0.0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5]
CO_MinAqiArray    = [0.0, 4.5, 9.5, 12.5, 15.5, 30.5, 40.5]
SO2_MinAqiArray   = [0, 36, 76, 186, 305, 605, 805]
NO2_MinAqiArray   = [0, 54, 101, 361, 650, 1250, 1650]
Aqi_MinAqiArray   = [0, 51, 101, 151, 201, 301, 401]
#######################################################################


def AQI_convert( c , air):
    c_low = 0.0
    c_high = 0.0
    i_low = 0.0
    i_high = 0.0
    I = 0.0

    if (air == 'PM25'):
        for i in range(0, 7):
            if(PM25_MaxAqiArray[6] < c):
                I=500
                break;

            elif ( PM25_MinAqiArray[i] <= c <= PM25_MaxAqiArray[i] ):
                c_low = PM25_MinAqiArray[i];
                c_high = PM25_MaxAqiArray[i];
                i_low = Aqi_MinAqiArray[i];
                i_high = Aqi_MaxAqiArray[i];
                break;

    elif (air == 'CO'):
        for i in range(0, 7):
            if (CO_MaxAqiArray[6] < c):
                I = 500
                break;

            elif ( CO_MinAqiArray[i] <= c <= CO_MaxAqiArray[i] ):
                c_low = CO_MinAqiArray[i];
                c_high = CO_MaxAqiArray[i];
                i_low = Aqi_MinAqiArray[i];
                i_high = Aqi_MaxAqiArray[i];
                break;
    elif (air == 'SO2'):
        for i in range(0, 7):
            if (SO2_MaxAqiArray[6] < c):
                I = 500
                break;

            elif ( SO2_MinAqiArray[i] <= c <= SO2_MaxAqiArray[i] ):
                c_low = SO2_MinAqiArray[i];
                c_high = SO2_MaxAqiArray[i];
                i_low = Aqi_MinAqiArray[i];
                i_high = Aqi_MaxAqiArray[i];
                break;
    elif (air == 'NO2'):
        for i in range(0, 7):
            if (NO2_MaxAqiArray[6] < c):
                I = 500
                break;

            if ( NO2_MinAqiArray[i] <= c <= NO2_MaxAqiArray[i] ):
                c_low = NO2_MinAqiArray[i];
                c_high = NO2_MaxAqiArray[i];
                i_low = Aqi_MinAqiArray[i];
                i_high = Aqi_MaxAqiArray[i];
                break;

    ###################computing AQI formula####################
    if(I!=500):
        I = (((i_high - i_low) / (c_high - c_low)) * (c - c_low)) + i_low
    ############################################################

    #not yet
    if (air == 'O3'):
        c_low = 0.0
        c_high = 0.0
        i_low = 0.0
        i_high = 0.0
        I = 0.0
        I_O3_8=0.0
        I_03_1=0.0
        for i in range(0, 7):
            if (O3_8Min_AqiArray[i] <= c <= O3_8Max_AqiArray[i]):
                c_low = PM25_MinAqiArray[i];
                c_high = PM25_MaxAqiArray[i];
                i_low = Aqi_MinAqiArray[i];
                i_high = Aqi_MaxAqiArray[i];
                I_O3_8 = (((i_high - i_low) / (c_high - c_low)) * (c - c_low)) + i_low
                break;
        for i in range(0, 7):
            if (O3_1MinAqiArray <= c <= O3_1MaxAqiArray[i]):
                c_low = PM25_MinAqiArray[i];
                c_high = PM25_MaxAqiArray[i];
                i_low = Aqi_MinAqiArray[i];
                i_high = Aqi_MaxAqiArray[i];
                I_O3_1 = (((i_high - i_low) / (c_high - c_low)) * (c - c_low)) + i_low
                break;

    return I;


# get_alpha example
# get_alpha(50,'O3')

while True:
    epoch_time = int(time())  # epoch time
    neo = Gpio()
    S0 = 2  # pin to use
    S1 = 3
    S2 = 4
    S3 = 5

    pinNum = [S0, S1, S2, S3]
    num = [0, 0, 0, 0]

    # Blink example
    for i in range(4):
        neo.pinMode(pinNum[i], neo.OUTPUT)

        # Temperature sensor
    neo.digitalWrite(pinNum[0], 0)
    neo.digitalWrite(pinNum[1], 0)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 0)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c0 = raw * scale
    temp_celsius = (c0 - 630) / 10 -8
    temp = (temp_celsius * 1.8) + 32

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

    SN1 = ((c2 - 286) - (get_alpha(temp, 'NO2')) * (c3 - 292)) * 3.876
    SN1 = SN1 if (SN1 >= 0) else -SN1
    AQI_SN1 = AQI_convert(SN1, 'NO2')

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

    SN2 = ((c4 - 417) - (get_alpha(temp, 'O3')) * (c5 - 402)) * 2.5445
    SN2 = SN2 if (SN2 >= 0) else -SN2
    #AQI_SN2 = AQI_convert(SN2, 'O3')

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

    SN3 = ((c6 - 265) - (get_alpha(temp, 'CO')) * (c7 - 281)) * 3.4246
    SN3 = SN3 if (SN3 >= 0) else -SN3
    AQI_SN3 = AQI_convert(SN3, 'CO')

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

    SN4 = ((c8 - 275) - (get_alpha(temp, 'SO2')) * (c9 - 295)) * 3.4722
    SN4 = SN4 if (SN4 >= 0) else -SN4
    AQI_SN4 = AQI_convert(SN4, 'SO2')

    # PM2.5
    neo.digitalWrite(pinNum[0], 1)
    neo.digitalWrite(pinNum[1], 1)
    neo.digitalWrite(pinNum[2], 0)
    neo.digitalWrite(pinNum[3], 1)
    sleep(0.05)

    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    c11 = (raw * scale) / 1000
    hppcf = (240.0 * pow(c11, 6) - 2491.3 * pow(c11, 5) + 9448.7 * pow(c11, 4) - 14840.0 * pow(c11, 3) + 10684.0 * pow(c11, 2) + 2211.8 * (c11) + 7.9623)
    PM25 = 0.518 + .00274 * hppcf
    AQI_PM25 = AQI_convert(PM25, 'PM25')

    print(temp_celsius)
    print(temp)

    print("SN1=",SN1)
    print(AQI_SN1)

    print("SN2=",SN2)

    print("SN3=",SN3)
    print(AQI_SN3)

    print("SN4=",SN4)
    print(AQI_SN4)

    print("PM25=",PM25)
    print(AQI_PM25)


    # #AQI Convesion for NO2_SN1
    # if SN1>=0 and SN1<=53 :
    #     AQI_NO2 = ((50-0)*(SN1 - 0))/(53-0)+0
    # elif SN1 >= 54 and SN1 <= 100 :
    #     AQI_NO2 = ((100-51)*(SN1-54))/(100-54) + 51
    # elif SN1 >= 101 and SN1 <= 360 :
    #     AQI_NO2 = ((150-101)*(SN1-101))/(360-101) + 101
    # elif SN1 >= 361 and SN1 <= 649 :
    #     AQI_NO2 = ((200-151)*(SN1-361))/(649-361) + 151
    # elif SN1 >= 650 and SN1 <= 1249 :
    #     AQI_NO2 = ((300-201)*(SN1-650))/(1249-650) + 201
    # elif SN1 >= 1250 and SN1 <= 1649 :
    #     AQI_NO2 = ((400-301)*(SN1-1250))/(1649-1250) + 301
    # elif SN1 >= 1650 and SN1 <= 2049 :
    #     AQI_NO2 = ((500-401)*(SN1-1650))/(2049-1650) + 401
    # else:
    #     AQI_NO2 = 500

    # # AQI Convesion for O3_SN2
    # if SN2 >= 0 and SN2 <= 53:
    #     AQI_NO2 = ((50 - 0) * (SN1 - 0)) / (53 - 0) + 0
    # elif SN2 >= 54 and SN2 <= 100:
    #     AQI_NO2 = ((100 - 51) * (SN1 - 54)) / (100 - 54) + 51
    # elif SN2 >= 101 and SN2 <= 360:
    #     AQI_NO2 = ((150 - 101) * (SN1 - 101)) / (360 - 101) + 101
    # elif SN2 >= 361 and SN2 <= 649:
    #     AQI_NO2 = ((200 - 151) * (SN1 - 361)) / (649 - 361) + 151
    # elif SN2 >= 650 and SN2 <= 1249:
    #     AQI_NO2 = ((300 - 201) * (SN1 - 650)) / (1249 - 650) + 201
    # elif SN2 >= 1250 and SN2 <= 1649:
    #     AQI_NO2 = ((400 - 301) * (SN1 - 1250)) / (1649 - 1250) + 301
    # elif SN2 >= 1650 and SN2 <= 2049:
    #     AQI_NO2 = ((500 - 401) * (SN1 - 1650)) / (2049 - 1650) + 401
    # else:
    #     AQI_NO2 = 500
    #
    # # AQI Convesion for CO_SN3
    # if SN3 >= 0 and SN3 <= 4.4:
    #     AQI_CO = ((50 - 0) * (SN3 - 0)) / (4.4 - 0) + 0
    # elif SN3 > 4.4 and SN3 <= 9.4:
    #     AQI_CO = ((100 - 51) * (SN3 - 4.4)) / (9.4 - 4.5) + 51
    # elif SN3 > 9.4 and SN3 <= 12.4:
    #     AQI_CO = ((150 - 101) * (SN3 - 9.4)) / (12.4 - 9.5) + 101
    # elif SN3 > 12.4 and SN3 <= 649:
    #     AQI_CO = ((200 - 151) * (SN3 - 12.4)) / (15.4 - 12.5) + 151
    # elif SN3 > 650 and SN3 <= 1249:
    #     AQI_CO = ((300 - 201) * (SN3 - )) / (1249 - 650) + 201
    # elif SN3 > 1250 and SN3 <= 1649:
    #     AQI_CO = ((400 - 301) * (SN3 - 1250)) / (1649 - 1250) + 301
    # elif SN3 > 1650 and SN3 <= 2049:
    #     AQI_CO = ((500 - 401) * (SN3 - 1650)) / (2049 - 1650) + 401
    # else:
    #     AQI_CO = 500
    sleep(2.5)

