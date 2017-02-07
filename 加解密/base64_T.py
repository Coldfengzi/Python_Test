'''
Created on 2017年1月17日

@author: 08669
'''

import base64
import sys

from pyDes import CBC, PAD_PKCS5
import pyDes


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
if __name__=='__main__':
    sBase='字符串'
    sEncode=base64.b64encode(sBase.encode(encoding='utf-8'))
    print('原字符串：%s,base64后：%s'%(sBase,sEncode))
    sBase2 = base64.b64decode(sEncode).decode()
    print(sBase2)
    
    KEY = "hi%$so78"    #密钥
    IV = "12up56^&"     #偏转向量    
    k = pyDes.des(KEY, CBC, IV, pad=None, padmode=PAD_PKCS5)
    print(base64.b64encode(k.encrypt('111111')))
    