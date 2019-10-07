#working with classes


class MyClass:
    x=5
    def __init__(self,x):
        self.x=x


class MyIterableElement:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a=1
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    def __iter__(self):
        self.a = 1
        return self



p1=MyClass
del p1.x
class MySecoundClass(MyClass):
    pass
p1==MyClass

p1(x=2).x

myclass = MyIterableElement()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))