'''
Created on 2017年1月4日

@author: 08669
'''
import time


def fab(n):
    """ 迭代运算法"""
    a1 = 1
    a2 = 1
    a3 = 1
    if n < 1:
        print('输入有误')
        return -1
    while(n - 2) > 0:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        n -= 1
    return a3

def fab_2(n):
    """ 递归运算 """
    if n<=2:
        return 1
    else:
        return fab_2(n-1)+fab_2(n-2)
    
if __name__ == '__main__':
    passTime = time.clock()
    print("总共有 %d 对小兔子，耗时：%f秒"%(fab(20),time.clock()-passTime))
    passTime = time.clock()
    print("总共有 %d 对小兔子，耗时：%f秒"%(fab_2(20),time.clock()-passTime))