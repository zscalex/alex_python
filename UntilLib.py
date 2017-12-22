#操作系统接口
#os模块提供了不少与操作系统相关联的函数。
import os
os.getcwd()      # 返回当前的工作目录
os.chdir('/server/accesslogs')   # 修改当前的工作目录
os.system('mkdir today')   # 执行系统命令 mkdir

#针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import shutil

shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

#文件通配符
# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:

import glob

glob.glob('*.py')#['primes.py', 'random.py', 'quote.py']


#命令行参数
# 通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
# 例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:

import sys
print(sys.argv)#['demo.py', 'one', 'two', 'three']

#错误输出重定向和程序终止
# sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。

#字符串正则匹配
#re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:

import re

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')#['foot', 'fell', 'fastest']
#如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:

'tea for too'.replace('too', 'two')

#数学
# math模块为浮点运算提供了对底层C函数库的访问:

#访问 互联网
#有几个模块用于访问互联网以及处理网络通信协议。
# 其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:

from urllib.request import urlopen

for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')  # Decoding the binary data to text.

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)

server.quit()

#日期和时间
#datetime模块为日期和时间处理同时提供了简单和复杂的方法。
# 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。

from datetime import date

now = date.today()

#数据压缩
# 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。

#性能度量
# 有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。

#测试模块
# 开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试

#doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。

#测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。