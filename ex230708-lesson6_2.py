#!/usr/bin/python3.10.4

import random

min = 1
max = 100
count = 0
target = random.randint(min, max)
print("=============猜數字遊戲=============\n\n")

while True:
    keyin = int(input(f"猜數字範圍{min}~{max}:"))
    count += 1
    if(keyin == target):
        print(f"賓果！恭喜猜對了，答案是：{target}")
        print(f"您共猜了{count}次")
        break
    elif keyin > target:
        print(f"再小一點")
        max = keyin - 1
    elif keyin < target:
        min = keyin + 1
    print(f"您已經猜了{count}次")
print("遊戲結束")