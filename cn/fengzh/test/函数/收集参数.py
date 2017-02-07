'''
Created on 2016年12月23日

@author: 08669
'''

def test(*params,extra='extra'):
    print('收集参数是：',params)
    print('有%d个参数' % len(params))
    print('extra参数:\t',extra)

def funX(x):
    print(x)
    def funY(y):
        x *= 2
        return x
    return funY

def test2(x):
    print(x)
    

if __name__ == '__main__':
    i = funX(8)
    print(i)
    print(i(5))    
#     a=[1,2,3,4,5,6,7,8]
#     test(*a,'asd')
#     test(*a,extra='asd')
