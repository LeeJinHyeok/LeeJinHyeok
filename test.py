S0 = 2 # pin to use
S1 = 3
S2 = 4
S3 = 5
pinNum = [S0,S1,S2,S3]
# Blink example


num = [0, 0, 0, 0]
num2=[0, 0, 0, 0]
for x in range(0,16):
    t = x
    for y in range(0,4):
        num[y] = t%2
        t = t//2
    print(pinNum)
    print(num2)
    print(num)



