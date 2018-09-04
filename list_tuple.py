#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
classmates=['郭总','刘总','黄总']
import json
for x in classmates:
	print u'你好！'
	print u'我是', json.dumps(x, encoding='UTF-8', ensure_ascii=False)

'''	
'''
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum
'''
classmates=['hqy','ghb','lwb']
for name in classmates:
   print name
print 'len=',len(classmates)	
print classmates[-1]
#在列表元素后边追加
classmates.append('Adam')
print classmates[-1]
#在列表指定位置插入元素
classmates.insert(1,'jack')
print classmates[1]
#删除列表末尾的元素
classmates.pop()
print classmates[-1]
#删除列表指定位置的元素
classmates.pop(1)
print classmates[1]
#把某元素直接替换
classmates[1]='Sarah'
print classmates[1]
#列表中的元素数据类型可以不同
L=['Apple',123,True]
print L
#列表中元素也可以是另外一个列表
S=['python','jave',L,'c']
print S
#列表中有列表可以看做是多维数组，下标法来调用
print S[2]
print S[2][2]

#元组合列表很相似，区别在于列表用的是方括号，可删除，插入，修改。而元组用都是圆括号，一旦初始化不可修改。

name=('Michael','Bob','Tracy')
print name
#为了消除歧义，只有一个元素时应该这样定义
t=(1,)
print t
#在元组初始化的时候定义个列表元素，虽然元组不可变，但元组中的元素是一个列表就可以变了
b=('a','b',['A','B'])
print b
b[2][0]=1
b[2][1]=2
print b