userSecond = int(input("Please, enter you`re time in seconds: "))
hour = userSecond / 3600
minute = userSecond / 3600 % 60
second = userSecond / 3600 % 60 % 60

print(f"{hour:.0f}:{minute:.0f}:{second:.0f}")