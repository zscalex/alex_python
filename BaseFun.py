

#@staticmethod:声明静态方法

class C(object):
    @staticmethod
    def f():
        print('runoob')


C.f()  # 静态方法无需实例化
cobj = C()
cobj.f()  # 也可以实例化后调用

#不可以调用C内的函数

#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
# 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。

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

#可调用A内的函数

# open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。

'''
file 对象方法
file.read([size]) size未指定则返回整个文件,如果文件大小>2倍内存则有问题.f.read()读到文件尾时返回""(空字串)

file.readline() 返回一行

file.readlines([size]) 返回包含size行的列表,size 未指定则返回全部行

for line in f: print line #通过迭代器访问

f.write("hello\n") #如果要写入字符串以外的数据,先将他转换为字符串.

f.tell() 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数).

f.seek(偏移量,[起始位置]) 用来移动文件指针.

偏移量:单位:比特,可正可负
起始位置:0-文件头,默认值;1-当前位置;2-文件尾
f.close() 关闭文件
'''

#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, seq[i])
#0 one
#1 two
#2 three

#any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，
# 如果不都为空、0、false，则返回 True。------->元素中只要不是全部由0，'',False元素构成的，返回值为True

#all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，
# 如果是返回 True，否则返回 False。------->元素中只要有0，'',False中的任意一个，返回值为False

#sum() 方法对系列进行求和计算。
#sum((2, 3, 4), 1)   --->10

#execfile() 函数可以用来执行一个文件。execfile(filename[, globals[, locals]])
#filename -- 文件名。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
#execfile('hello.py')

#issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。
#issubclass(class, classinfo)

#super() 函数用于调用下一个父类(超类)并返回该父类实例的方法。

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

#bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
# bin(10)--->'0b1010'

#iter() 函数用来生成迭代器。iter(object[, sentinel])
# object -- 支持迭代的集合对象。
# sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
# 此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。
lst = [1, 2, 3]
for i in iter(lst):
    print(i)

#property() 函数的作用是在新式类中返回属性值。

class C(object):
    def __init__(self):
        self._x = None

    @property#----->get:获得
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter#----->set:设置
    def x(self, value):
        self._x = value

    @x.deleter#---->del:删除
    def x(self):
        del self._x


#元组 tuple() 函数将列表转换为元组。   tuple( seq )
# seq -- 要转换为元组的序列。

#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，
# 序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# filter(function, iterable)
# function -- 判断函数。
# iterable -- 可迭代对象。

def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])#一定程度上和map一样
print(newlist)

#len() 方法返回对象（字符、列表、元组等）长度或项目个数。

# range() 函数可创建一个整数列表，一般用在 for 循环中。range(start, stop[, step])

#type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。

#bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256
# bytearray([source[, encoding[, errors]]])
# bytearray([1,2,3])--->bytearray(b'\x01\x02\x03')


#raw_input() 用来获取控制台的输入。
# raw_input() 将所有输入作为字符串看待，返回字符串类型。
# 除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。

#unichr() 函数 和 chr()函数功能基本一样， 只不过是返回 unicode 的字符。unichr(97)---->u'a'


#callable() 函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。

# str.format()，它增强了字符串格式化的功能。基本语法是通过 {} 和 : 来代替以前的 % 。
# format 函数可以接受不限个参数，位置可以不按顺序。

"{1} {0} {1}".format("hello", "world")  # 设置指定位置  ---->'world hello world'

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
#value 为: 6

print("{:.2f}".format(3.1415926))#---->3.14

#locals() 函数会以字典类型返回当前位置的全部局部变量。

#reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 function（有两个参数）
# 先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

#chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。chr(49)--->A

#frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
#a = frozenset(range(10))     # 生成一个新的不可变集合

#reload() 用于重新载入之前载入的模块。

#vars() 函数返回对象object的属性和属性值的字典对象。
# 返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。

#getattr() 函数用于返回一个对象属性值。getattr(object, name[, default])
#default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。

#map() 会根据提供的函数对指定序列做映射。map(function, iterable, ...)
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数

map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])# 提供了两个列表，对相同位置的列表数据进行相加

#repr() 函数将对象转化为供解释器读取的形式。repr(object)
# 返回一个对象的 string 格式。

dict = {'runoob': 'runoob.com', 'google': 'google.com'}
repr(dict)
#--->"{'google': 'google.com', 'runoob': 'runoob.com'}"

#xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器。

#cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。

#globals() 函数会以字典类型返回当前位置的全部全局变量。globals()

#max() 方法返回给定参数的最大值，参数可以为序列。max( x, y, z, .... )

#reverse() 函数用于反向列表中元素。list.reverse()

#zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。zip([iterable, ...])

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]

zipped = zip(a,b)     # 打包为元组的列表[(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式[(1, 2, 3), (4, 5, 6)]

#compile() 函数将一个字符串编译为字节代码。compile(source, filename, mode[, flags[, dont_inherit]])
# source -- 字符串或者AST（Abstract Syntax Trees）对象。。
# filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
# mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
# flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
# flags和dont_inherit是用来控制编译源码时的标志

#hasattr() 函数用于判断对象是否包含对应的属性。hasattr(object, name)

#memoryview() 函数返回给定参数的内存查看对象(Momory view)。
# 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。memoryview(obj)
v = memoryview('abcefg')
v[1]#--->'b'
v[1:4]#---><memory at 0x77ab28>
v[1:4].tobytes()#----->'bce'

#round() 方法返回浮点数x的四舍五入值。round( x [, n]  )
round(80.23456, 2) #--->80.23

#__import__() 函数用于动态加载类和函数, 如果一个模块经常变化就可以使用 __import__() 来动态载入。
#__import__('a')        # 导入 a.py 模块

#oct() 函数将一个整数转换成8进制字符串。

#exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。exec(object[, globals[, locals]])
#bject：必选参数，表示需要被指定的Python代码。它必须是字符串或code对象。如果object是一个字符串，该字符串会先被解析为一组Python语句，
# 然后在执行（除非发生语法错误）。如果object是一个code对象，那么它只是被简单的执行。
#globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象
#locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。
# 如果该参数被忽略，那么它将会取与globals相同的值。

#delattr 函数用于删除属性。delattr(x, 'foobar') 相等于 del x.foobar。

#hash() 用于获取取一个对象（字符串或者数值等）的哈希值。

#complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
# 如果第一个参数为字符串，则不需要指定第二个参数。。

# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
#complex("1+2j")

#slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。