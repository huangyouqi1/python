#!/usr/bin/env python
#-*- coding: utf-8 -*-
age=20
if age >= 18:
	print 'your age is ',age
	print 'adult'
else:
	print 'you age is', age
	print 'teenager'
	
x=1
if x:
	print 'True'
#注意事项，冒号不能少，遵循缩进规则，遇到缩进结束模块

names=['Michael','Bob','Tracy']
print u'他们的名字分别是：'
for name in names:
	print name
	
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum+=x
print sum	
#注意事项，冒号不能少，遵循缩进规则，遇到缩进结束模块
sum2=0
for x in range(101):
	sum2+=x
print sum2	
#range(101)表示0到100 range(4,10)表示4到9
s=0
n=99
while n>0 :
	s+=n
	n-=1
print s	

#从raw_input()读取的内容永远以字符串的形式返回
birth=int(raw_input('birth:'))
if birth >2000:
	print '00'u'后'
else:	
	print '00'u'前'