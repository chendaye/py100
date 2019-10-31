"""
完美数(自身以外的因子)
6=1+2+3
28=1+2+4+7+14
"""

for num in range(1, 10000):
    sum = 0
    tmp = num
    for m in range(1, tmp - 1):
        if tmp % m == 0:
            sum += m
    if sum == num:
        print(num)



