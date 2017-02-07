'''
Created on 2017年1月4日

@author: 08669
'''

class Ball(object):
    '''
    classdocs
    '''
    def setName(self,name):
        self.name = name
    def kick(self):
        print('我叫%s，谁在踢我'%self.name)

#     def __init__(self, params):
#         '''
#         Constructor
#         '''
        