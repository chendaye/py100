# getter  setter

class Test(object):
    # 限定自定义类型的对象只能绑定某些属性
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, name):
        self._name = name

    # 静态方法 直接调用
    @staticmethod
    def is_static():
        return True

    # 在类中定义类方法，类方法的第一个参数约定名为cls。 通过类方法创建当前类的对象
    @classmethod
    def instance(cls):
        return cls('long', 12)


def main():
    if Test.is_static(): # 直接调用 不用实例化类
        cla = Test('chendaye', 18)
        print(cla.name)
        # 类方法获取类的实例
        cla2 = Test.instance()
        print(cla2.name)


if __name__ == '__main__':
    main()