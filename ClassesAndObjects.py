class MyClass:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('__init__')

    def display(self):
        print("a: ", self.a)
        print("b: ", self.b)

obj = MyClass(10, 20)

obj.display()