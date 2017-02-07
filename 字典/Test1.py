'''
Created on 2017年1月4日

@author: 08669
'''
import os
import random


if __name__ == '__main__':
    a={1:"one",2:"two",3:"three"}
#     a.save()
    b=a.copy()
    
    c=b.copy()
    
    print(b)
    a.clear()
    print(b)
    
    print(os.getcwd())
    
    
