v = [1, -2, -3, 4, -5, 6, 7, -8, -9, 10]
for i in range (len(v)-1):
    if v[i] < 0  and v[i+1] < 0:
        print(v[i], v[i+1])