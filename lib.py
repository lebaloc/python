class Base:
    def __init__(self, a=1, b=2):
        self.x = a
        self.y = b
    def f(self, a):
        import os
        return self.x + self.y + a
    def g(self):
        print(self.f(1))
    def h(a):
        print("return the object")
        return a
