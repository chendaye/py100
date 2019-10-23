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


# 继承
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s玩耍.' % self._name)

    def av(self):
        if self._age > 18 :
            print('%s看av.' % self._name)
        else:
            print('%s看光头强.' % self._name)


# Student 继承 Person
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(age, name)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def play(self):
        print('重写父类的play方法；这就是多态')


# Teacher 继承 Person
class Teacher(Person):
    def __init__(self, name, age, course):
        super().__init__(age, name)
        self._course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        self._course = course


#抽象类
from abc import ABCMeta, abstractmethod

class Pet(object, mateclass=ABCMeta):
    def __init__(self, nick):
        self._nick = nick

    @abstractmethod
    def voice(self):
        pass


class Cat(Pet):
    def voice(self):
        print('%scat.' % self._nick)


class Dog(Pet):
    def voice(self):
        print('%sdog.' % self._nick)


if __name__ == '__main__':
    main()