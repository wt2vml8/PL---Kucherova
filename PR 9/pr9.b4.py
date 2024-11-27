def sim(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = 2   
    if divisor * divisor > n:
        return True  
    if n % divisor == 0:
        return False  
    return sim(n, divisor + 1)  

number = int(input("Введите число: "))
if sim(number):
    print("YES")
else:
    print("NO")
    