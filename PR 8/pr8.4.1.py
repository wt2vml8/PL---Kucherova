m = int(input('Введите число: ')) 
n = int(input('Введите число отличное от m: '))
a = []
for i in range (m):
    b = []
    for j in range (n):
        print('Введите [', i, ', ', j, '] элемент')
        b.append(int(input()))
    a.append(b)

for i in range (m):
    for j in range (n):
        print(a[i][j], end='')
    print()

t = sum(a[0])
p = sum(a[1])
if t > p:
    print('Сумма первой строки:', t , '- наибольшая \nСумма второй строки:', p , '- наименьшая')
else:
    print('Сумма второй строки:', p , '- наибольшая \nСумма первой строки:', t , '- наименьшая' )


