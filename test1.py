# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can
from neo import Gpio  # import Gpio library
from time import sleep

neo = Gpio()

S0 = 2 # pin to use
S1 = 3
S2 = 4
S3 = 5


pinNum = [S0,S1,S2,S3]
# Blink example
for i in range(0, 4):
    neo.digitalWrite(pinNum[i], 0)
    neo.pinMode(pinNum[i], neo.OUTPUT)

num = [0, 0, 0, 0]
num2 = [0, 0, 0, 0]
while True:
    for x in range(0, 16):
        t = x
        for y in range(0, 4):
            num[y] = t % 2
            t = t // 2

        neo.digitalWrite(pinNum[], num)
        sleep(1)
        neo.digitalWrite(pinNum[],num2)
        sleep(1)

