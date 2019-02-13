from time import sleep
while True:
    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    v =  raw*(3300/4096)
    t =(v-500)/10
    sleep(1)
    print (t)
