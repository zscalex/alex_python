import os
import datetime
print(os.path.abspath("."))
print(os.environ)

L = [x for x in os.listdir(".") if os.path.isfile(x)]
print(L)

'''
url = os.path.abspath(".")
os.path.join(url,"test.txt")
os.mkdir(os.path.abspath("./test.txt"))
'''
now = datetime.datetime.now()

f=open(os.path.abspath(".")+"/test.txt",'a')
f.write("\nhello writting file    ")
f.write(now.strftime('%Y-%m-%d %H:%M:%S') )
f.close()