userSecond = int(input("Please, enter you`re time in seconds: "))
hour = userSecond / 3600
minute = userSecond / 3600 % 60
second = userSecond / 3600 % 60 % 60
if minute < 10 and second < 10:
    print(f"{hour:.0f}:0{minute:.0f}:0{second:.0f}")
else:
    if minute < 10:
        print(f"{hour:.0f}:0{minute:.0f}:{second:.0f}")
    else:
        if second < 10:
            print(f"{hour:.0f}:{minute:.0f}:0{second:.0f}")
        else:
            print(f"{hour:.0f}:{minute:.0f}:{second:.0f}")



