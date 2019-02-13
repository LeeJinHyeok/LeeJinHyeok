# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can
from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks

neo =Gpio()

pinTwo = 0  # pin to use
pinFour = 1
pinFive = 2
pinSix = 3




pinNum = [pinTwo,pinFour,pinFive,pinSix]
# Blink example
for i in pinNum:
    neo.digitalWrite(pinNum[i], '0')
    neo.pinMode(pinNum[i], neo.OUTPUT)


while 1:
    for x in range(0,16):
        num = [0,0,0,0]
        t = x
        for y in range(0,4):
            num[y] = t % 2
            t = t // 2


        neo.digitalWrite(pinNum, num)
        # neo.digitalWrite(pinNum[pinFive], num[pinFive])
        # neo.digitalWrite(pinNum[pinFour], num[pinFour])
        # neo.digitalWrite(pinNum[pinTwo], num[pinTwo])
        sleep(1)