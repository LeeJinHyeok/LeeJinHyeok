num = [0, 0, 0, 0]
for x in range(0,16):
    t = x
    for y in range(0,4):
        num[y] = t%2
        t = t//2
    print(num)



