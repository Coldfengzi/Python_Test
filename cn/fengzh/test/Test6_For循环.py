'''
Created on 2016年12月5日

@author: wyoffice
'''
from pip._vendor.pyparsing import Each

if __name__ == '__main__':
    for i in range(10):
        if i%2 !=0:
            print(i)
            continue
        i+=2
        print(i,end="heihei\n")
    print(i,end="haha\n")
        
#     sList = 'FishC'
#     for x1 in sList:
#         print(x1,end=' ')
    