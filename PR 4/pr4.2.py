a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
if a < b:
    while a <= b:
        print(a)
        a += 1
else:
    while a >= b:
        print(a)
        a -= 1