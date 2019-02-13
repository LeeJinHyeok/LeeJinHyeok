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

# Blink example
for a in range(0, 16):  # Do for five times
    if(a == 5):
        neo.digitalWrite(pinFour, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFive, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFour, neo.LOW)  # write low value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFive, neo.LOW)  # write low value to pin
        sleep(1)  # wait one second
    elif(a==11):
        neo.digitalWrite(pinTwo, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFive, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinSix, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinTwo, neo.LOW)  # write low value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFive, neo.LOW)  # write low value to pin
        sleep(1)
        neo.digitalWrite(pinSix, neo.LOW)  # write low value to pin
        sleep(1)  # wait one second
    elif(a==15):
        neo.digitalWrite(pinTwo, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFive, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinSix, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFour, neo.HIGH)  # write high value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFour, neo.LOW)  # write low value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinTwo, neo.LOW)  # write low value to pin
        sleep(1)  # wait one second
        neo.digitalWrite(pinFive, neo.LOW)  # write low value to pin
        sleep(1)
        neo.digitalWrite(pinSix, neo.LOW)  # write low value to pin
        sleep(1)  # wait one second
