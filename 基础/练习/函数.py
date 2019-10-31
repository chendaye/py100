"""
函数与变量作用域
"""
def long(num = 3):
    return num + 6
#m = int(input('m= '))
print(long(2))


"""
可变参数 *args
"""
def add(*many):
    sum = 0
    for val in many:
        sum += val
    return sum
print(add(1,2,3,4,5))


"""
文件模块
"""
from 基础.module import long as long1
from 基础.module.module2 import long as long2

long1()
long2()


"""
变量作用域
"""





