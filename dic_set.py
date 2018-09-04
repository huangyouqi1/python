#!/usr/bin/env python
#-*- coding: utf-8 -*-
#dic (key-value) 用花括号来定义
d={'Michael':95,'Bob':75,'Tracy':85}
for x in d:
	print x,d[x]
#把数据放入dic的方法，除了初始化时指定外，还可以通过key放入:
d['Michael']=67
d['Bob']=105
for x in d:
	print x,d[x]

#获取KEY的两种方法，一是通过in判断Key是否存在：

if 'Michael' in d :
	print 'True'
else:
	print 'False'
#二是通过dic提供的get方法,如果key不存在，返回None，或者自己指定的值	d.get('Michael'，-1)
if d.get('Michael'):
	print 'True'
else:
	print 'False'
#删除一个key值,可删除，插入，修改
d.pop('Bob')	
for x in d:
	print x,d[x]

'''
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而增加；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''	

#set和dict类似，也是一组key的集合，但不存储value，由于key不可重复，所有，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
s=set([1,2,3])
print s
s=set([1,1,2,2,3,3])
print s
#添加元素到set
s.add(4)
print s
#从set中移除某个元素
s.remove(2)
print s
for x in s:
	print x

'''
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
'''
s1=set([1,2,3,4])
s2=set([2,3,4,5])
print s1 & s2
print s1 | s2

#排序
a=['b','c','a']
a.sort()
print a

#替换
b='abcdefg'
c=b.replace('a','M')
print c























	
