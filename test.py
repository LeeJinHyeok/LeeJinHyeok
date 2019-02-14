# from neo import Gpio  # import Gpio library
# from time import sleep  # import sleep to wait for blinks
#
# neo =Gpio()
#
# S0 = 24 # pin to use
# S1 = 25
# S2 = 26
# S3 = 27
#
# pinNum = [S0, S1, S2, S3]
#
# num = [0,0,0,0]
#
# # Blink example
# for i in range(4):
#     neo.pinMode(pinNum[i], neo.OUTPUT)
#
# neo.digitalWrite(pinNum[0], 1)
# # sleep(0.5)
# neo.digitalWrite(pinNum[1], 1)
# # sleep(0.5)
# neo.digitalWrite(pinNum[2], 1)
# # sleep(0.5)
# neo.digitalWrite(pinNum[3], 1)
# # sleep(0.5)
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
# raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
# scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
# print (raw * scale)
from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks


neo =Gpio()
column_pins = [2, 3, 4, 5]
row_pins = [11, 10, 9, 8]
for i in range(4):
    neo.pin_mode(column_pins[i], neo.OUTPUT)
    neo.digital_write(column_pins[i], neo.LOW)

for z in range(4):
    neo.pin_mode(column_pins[z], neo.OUTPUT)
    neo.digital_write(column_pins[z], neo.HIGH)

