'''
Created on 2017年1月5日

@author: 08669
'''
import random

class Fish(object):
    '''
    classdocs
    '''


    def __init__(self):#params
        '''
        Constructor
        '''
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)
    def move(self):
        #演示
        self.x -=1
        print("我的位置是: ", self.x,self.y)
        
        
        
class GoldFish(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        super(Shark, self).__init__()
        self.hungry = True
        
    def eat(self):
        if self.hungry:
            print('吃货的梦想就是每天都有得吃')
            self.hungry = False
        else:
            print("吃撑了，吃不下！")
    
        
        
if __name__ == '__main__':
    fish = Fish()
    fish.move()
    
    shark=Shark()
    shark.eat()
    shark.move()
    