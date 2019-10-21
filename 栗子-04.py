"""
列表中最大和第二大的元素的值
"""


def max2(x):
    # 冒泡排序
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])  # 最初排序前面2个
    for index in range(2, len(x)):  # 从第三个开始
        if x[index] > m1:   # 找到更大的 把它赋值给m1，同时m1的旧值给m2
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:  # 如果小于m1 ,大于m2 赋值给m2
            m2 = x[index]
    return m1, m2

if __name__ == '__main__':
    print(max2([3,7,45,8,23,54,1,45]))