"""
验证码
"""
import random


def code(length=4):
    strings = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pos = ''
    for _ in range(length):
        index = random.randint(0, len(strings) - 1)
        pos += strings[index]
    return pos


if __name__ == '__main__':
    print(code(5))
