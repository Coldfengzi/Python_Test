'''
Created on 2017年1月12日

@author: 08669
'''

class MyProperty(object):
    '''
    classdocs
    '''


    def __init__(self, fget=None,fset=None,fdel=None):
        '''
        Constructor
        '''
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        print('MyProperty __init__',fget,fset,fdel)
    def __get__(self,instance,owner):
        return self.fget(instance)
    def __set__(self,instance,value):
        print('MyProperty',value)
        self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)

class C:
    def getX(self):
        return self._x
    def setX(self,value):
        print('C class',value)
        self._x = value
    def delX(self):
        del self._x
    def __init__(self):
        self._x = None
        
    x = MyProperty(getX,setX,delX) 


if __name__ == '__main__':       
    c=C()
    c.x='X-man'
    print(c.x)
                