'''
Created on 2017年1月4日

@author: 08669
'''
import sys
import time


def recursion(n):
    """
       阶乘运算，普通方式
    """
    result = 1
    for i in range(1,n+1):
        result *= i
    time.sleep(0.001)
    return result

def factorial(n):
    """ 阶乘运算，递归方式    """    
    time.sleep(0.001)
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

    

def strict_time():
    if sys.platform == "win32":
        return time.clock()
    else:
        return time.time()


if __name__ == '__main__':
    number = int(input('请输入整数：'))
    timePass =strict_time()  
    print('%d的阶乘是：%d，耗时：%.3f'%(number,recursion(number),strict_time()-timePass))
    timePass =strict_time()    
    print('%d的阶乘是：%d，耗时：%.3f'%(number,factorial(number),strict_time()-timePass))

    
