'''
Created on 2017年1月4日

@author: 08669
'''
import time


def hanoi(n,x,y,z,total=0):
    if total==0 :
        total=n
    if n==1:
        print('只有一个盘子：%s(%d)-->%s'%(x,n,z))
    else:
        hanoi(n-1,x,z,y,total)
        print('%s(%d)-->%s'%(x,n,z))
        hanoi(n-1, y, x, z,total)

if __name__ == '__main__':
    passTime = time.clock()
    hanoi(5,'X','Y','Z')
    print('耗时：',time.clock()-passTime)