"""
计算点的距离
"""

from math import sqrt


class distance:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, x, y):
        self.x += x
        self.y += y

    def dis(self, x, y):
        return sqrt((self.x - x) ** 2 + (self.y - y) ** 2)


def main():
    cla = distance(2, 3)
    print(cla.dis(4, 8))
    cla.move_to(9, 5)
    print(cla.dis(4,9))


if __name__ == '__main__':
    main()
