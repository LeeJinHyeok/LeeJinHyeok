# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can do

# digitalWriting/Reading - Soon to come PWM

from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks

neo = Gpio()  # create new Neo object

pinTwo = 24  # pin to use
pinFour = 25
pinFive = 26
pinSix = 27



neo.pinMode(pinTwo, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
neo.pinMode(pinFour, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
neo.pinMode(pinFive, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
neo.pinMode(pinSix, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
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

            neo.digitalWrite(pinNum[pinSix], num[pinSix])
            neo.digitalWrite(pinNum[pinFive], num[pinFive])
            neo.digitalWrite(pinNum[pinFour], num[pinFour])
            neo.digitalWrite(pinNum[pinTwo], num[pinTwo])
            sleep(1)