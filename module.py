#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import unicode_literals
'a test module'
__author__='huangyouqi'

import sys
def test():
	args=sys.argv
	if len(args)==1:
		print 'hello world!'
	elif len(args)==2:
		print 'hello %s!' % args[1]
	else:
		print 'too many arguments!'
'''		
if __name__=='__main__':
	test()
	'''
try:
	import cStringIO as StringIO
except ImportError:
	import StringIO
try:
	import json
except ImportError:
	import simplejson as json
	
'''在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量
'''
def _private_1(name):
	print 'hello,%s' %name 
def _private_2(name):
	print 'hi,%s' % name 
def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)
greeting('hyq')		

import PIL.Image
im=PIL.Image.open('kebi.JPG')
print im.format,im.size,im.mode
im.show()
im.save("save.gif","GIF")
im.thumbnail((400,300))
im.save('thumb.jpg','JPEG')
import sys
sys.path.append('E:/python/mycompany')
print sys.path
import xyz
#这里要先添加路径再包涵，否则或报错
xyz.xyz(1)

'''从Python 2.7到Python 3.x就有不兼容的一些改动，比如2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode，而在3.x中，所有字符串都被视为unicode，因此，写u'xxx'和'xxx'是完全一致的，而在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串”。
'''

print '\'xxx\' is unicode?',isinstance('xxx',unicode)
print 'u\'xxx\' is unicode?',isinstance(u'xxx',unicode)
print '\'xxx\' is str?',isinstance('xxx',str)
print 'b\'xxx\' is str?',isinstance(b'xxx',str)




















