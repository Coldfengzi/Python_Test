'''
Created on 2017年1月5日

@author: 08669
'''

class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")

class B(A):
    def __init__(self):
        print("进入B…")
        A.__init__(self)
        print("离开B…")
        
class C(A):
    def __init__(self):
        print("进入C…")
        A.__init__(self)
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        B.__init__(self)
        C.__init__(self)
        print("离开D…")
class E(B, C):
    def __init__(self):
        print("进入E…")
        super(B,self).__init__()
        super(C,self).__init__()
        print("离开E…")        

if __name__=='__main__':
  d=D()
  print('使用super之后') 
  e=E() 
