import math
x = float(input('Введите переменную x: '))
y = float(input('Введите переменную y: '))
z = 3.25*10**-4
s = 5*math.atan(x)-(1/4)*math.acos(x)*((x+3*abs(x-y)+x**2)/(abs(x-y)*z+x**2))
print('s= {0:3f}'.format(s))