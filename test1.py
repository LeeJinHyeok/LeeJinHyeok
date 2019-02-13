# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can
from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks

neo =Gpio()

pinTwo = 2 # pin to use
pinFour = 3
pinFive = 4
pinSix = 5


pinNum = [pinTwo,pinFour,pinFive,pinSix]
# Blink example
for i in range(0,4):
    neo.pinMode(pinNum[i], neo.OUTPUT)
    print(i)

while 1:
    for x in range(0,16):
        num = [0, 0, 0, 0]
        t = x
        for y in range(0,4):
            num[y] = t % 2
            t = t // 2

            neo.digitalWrite(pinNum[y], num[y])
        sleep(1)