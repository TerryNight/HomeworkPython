n = int(input("Enter you`re number: "))
mx = n % 10
b = 0
a = n // 10
while n == 0:
    a = a % 10
    if mx < a:
        mx = a
print(f"{mx}")