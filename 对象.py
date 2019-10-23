class Test:

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(self.name)


def main():
    test = Test('chendaye hello')
    test.hello()


if __name__ == '__main__':
    main()
