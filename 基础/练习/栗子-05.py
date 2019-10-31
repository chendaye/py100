"""
打印杨辉三角
"""


def main():
    num = int(input('Number of rows: '))    # 几行
    yh = [[]] * num  # 初始化行数
    for row in range(len(yh)):  # 循环打印行
        yh[row] = [None] * (row + 1)    # 每一行的数字个数 = 行数 + 1
        for col in range(len(yh[row])):    # 遍历每一行
            if col == 0 or col == row:  # 每一行的第一和最后一个数 是 1
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]  # 
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
