#3
import math 
x = 3.74*10**-2
y = float(input('Введите значение y: '))
z = 0.16 * 10 ** 2
s = (( 1 + math.sin(x + y)**2)/ abs(x - (2*y/1+x**2+y**2)))* (x**abs(y)) + math.cos(math.atan(1/z)**2)
print('s = {0:3f}'.format(s))
