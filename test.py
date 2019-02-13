# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can do

# digitalWriting/Reading - Soon to come PWM

from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks

neo = Gpio()  # create new Neo object

pinTwo = 0  # pin to use
pinFour = 1
pinFive = 2
pinSix = 3




pinNum = [pinTwo,pinFour,pinFive,pinSix]
# Blink example
for i in pinNum:
    neo.pinMode(pinNum[i], neo.OUTPUT)
while 1 :
    for x in range(16):
        num = [0,0,0,0]
        t = x
        for y in range(4):
            num[y] = t%2
            t = t/2
        print(Num)

        neo.digitalWrite(pinNum[pinSix], num[pinSix])
        neo.digitalWrite(pinNum[pinFive], num[pinFive])
        neo.digitalWrite(pinNum[pinFour], num[pinFour])
        neo.digitalWrite(pinNum[pinTwo], num[pinTwo])
        sleep(1)

