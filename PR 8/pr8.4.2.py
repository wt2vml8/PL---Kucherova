n = int(input('Введите значение:'))
a = []
for i in range(n):
    b = []
    for j in range (n):
        print('Введите[', i,',' , j,'] элемент' )
        b.append(int(input()))
    a.append(b)

print('Исходный массив: ')
for i in range (n):
    for j in range (n):
        print(a[i][j],  end='')
    print()

for i in range (n):
    for j in range (n):
        if a[i][j]<0:
            a[i][j] = 0
        elif a[i][j] > 0:
            a[i][j] = 1

for i in range (n):
    for j in range (n):
        if i<=j:
            a[i][j] = 0
    
print('Измененный массив: ')
for i in range (n):
    for j in range (n):
        print(a[i][j], end='')
    print()


