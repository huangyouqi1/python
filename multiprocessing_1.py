#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
#linux
import os
print 'Process (%s)start...' % os.getpid()
pid=os.fork()
if pid==0:
	print 'I am child process(%s)and my parent is %s.' % (os.getpid(),os.getppid())
else:
	print 'I(%s)just created a child process (%s).' % (os.getpid(),pid)
'''
from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
	n=10
	while n>0:
		print '%d Run child process %s(%s)...' % (n,name,os.getpid())
		n=n-1
if __name__=='__main__':
	print 'Parent process %s.' % os.getpid()
	p=Process(target=run_proc,args=('test',))
	print 'Process will start.'
	p.start()
	p.join()
	print 'Process end.'
	
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print 'Run task %s (%s)...' % (name,os.getpid())
	start=time.time()
	time.sleep(random.random()*3)
	end=time.time()
	print 'Task %s rans %0.2f seconds.' % (name,(end-start))

if __name__=='__main__':
	print 'Parent process %s.' % os.getpid()
	p=Pool()
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print 'waiting for all subprocesses done...'
	p.close()
	p.join()
	print 'All subprocesses done.'

from multiprocessing import Queue
import os,time,random
def write(q):
		for value in ['A','B','C']:
			print 'Put %s to queue...' % value
			q.put(value)
			time.sleep(random.random())
			
def read(q):
	while True:
		value=q.get(True)
		print 'Get %s from queue' % value
		
if __name__=='__main__':
	q=Queue()
	pw=Process(target=write,args=(q,))
	pr=Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
	
	
	
	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			