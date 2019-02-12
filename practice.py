def maximum(x,y):
    if x>y:
       return x
    elif x==y:
        return 'The numbers are equal'
    else:
        return y
a = int(input('x를 입력하시오: '))
b = int(input('y를 입력하시오: '))
print(maximum(a,b))
