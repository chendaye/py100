import time
from math import sqrt
import json


def main():
    f = None
    try:
        f = open('F:/Coding/file.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


"""
不愿意在`finally`代码块中关闭文件对象释放资源，也可以使用上下文语法，通过**`with`关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
"""


def main2():
    try:
        with open('F:/Coding/file.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


# `for-in`循环逐行读取或者用`readlines`方法将文件按行读取到一个列表容器中
def main3():
    # 一次性读取整个文件内容
    with open('F:/Coding/file.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('F:/Coding/file.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('F:/Coding/file.txt') as f:
        lines = f.readlines()
    print(lines)


"""
将素数写入3个文件
"""


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main4():
    filenames = ('F:/Coding/a.txt', 'F:/Coding/b.txt', 'F:/Coding/c.txt')
    fs_list = []
    try:
        for filename in filenames:
            # 打开文件
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    # 写文件a
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    # 写文件b
                    fs_list[1].write(str(number) + '\n')
                else:
                    # 写文件c
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


# 读写二进制文件
def main5():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


# json
def main6():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()
    main2()
    main3()
    main4()
