f = int(input('Введите значение f:'))
k = int(input('Введите значение k:'))
if f < 5 and k > 2:
    print('R = ', f+k-1)
elif k < 2:
    print('R = ', k**2)
elif k == 2:
    print('R = 1')