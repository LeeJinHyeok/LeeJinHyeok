# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can do

# digitalWriting/Reading - Soon to come PWM

from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks

neo = Gpio()  # create new Neo object


pinNum = [0,1,2,3]

for i in pinNum:
    neo.pinMode(pinNum[i], neo.OUTPUT)
    while 1 :
        for x in range(16):
            num = [0,0,0,0]
            t = x
            for y in range(4):
                num[y] = t%2
                t = t/2

            neo.digitalWrite(pinNum[3], num[3])
            neo.digitalWrite(pinNum[2], num[2])
            neo.digitalWrite(pinNum[1], num[1])
            neo.digitalWrite(pinNum[0], num[0])
            sleep(1)