import random

number = random.randint(1,10)

guess = int(input("猜1到10的数字: "))

if guess == number:
    print("猜对了!")
else:
    print("猜错了，答案是", number)
