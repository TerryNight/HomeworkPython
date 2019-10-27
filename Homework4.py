n = int(input("Пожалуйста, введите целое положительное число: "))
mx = n % 10
while n != 0:
    n = n // 10
    b = n % 10
    if b > mx:
        mx = b
print(f"{mx}")