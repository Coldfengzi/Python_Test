'''
Created on 2016年12月5日

@author: wyoffice
'''

if __name__ == '__main__':
    x=2
    y=1
    small=x if x<y else y
    print(small)
    
    if x<y:
        small=x
    elif x>y :
        small=y 
    print(small)
            