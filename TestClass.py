#Python中3种方式定义类方法, 常规方式, @classmethod修饰方式, @staticmethod修饰方式.

#声明了静态方法
#@staticmethod是把函数嵌入到类中的一种方式，函数就属于类，同时表明函数不需要访问这个类。通过子类的继承覆盖，能更好的组织代码。
#staticmethod相当于一个定义在类里面的函数，所以如果一个方法既不跟实例相关也不跟特定的类相关，推荐将其定义为一个staticmethod，
# 这样不仅使代码一目了然，而且似的利于维护代码
#可以通过实例与类来调用

class C(object):
    def func1(self):
        print('foo')
    @staticmethod
    def f():
        print('runoob')


C.f();  # 静态方法无需实例化
cobj = C()
cobj.f()  # 也可以实例化后调用

#f()中不能调用C内部函数

#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
# 可以来调用类的属性，类的方法，实例化对象等。
#可以通过实例与类来调用，用类调用、用实例则不需要传入类名
#这样编程的好处有：

#分解字符串操作可以重复使用，而我们只需要传入参数一次；
#1.OOP；
#2.cls是类本身，而不是类的实例，当我们将Date作为父类时，其子类也会拥有from_string方法
#和class method很相似的是staticmethod，但它不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。

class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法


A.func2()  # 不需要实例化