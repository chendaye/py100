from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


# 利用多进程
def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


"""
通过`Process`类创建了进程对象，
通过`target`参数我们传入一个函数来表示进程启动后要执行的代码，
后面的`args`是一个元组，它代表了传递给函数的参数
`Process`对象的`start`方法用来启动进程，而`join`方法表示等待进程执行结束
"""


def main1():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


# 进程间的通信
counter = 0

# 启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个
def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main2():
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main2()