'''
Created on 2016年12月2日

@author: wyoffice
'''
import random
from test.test_tools.test_unparse import try_except_finally

def GuessNum(realNum):
#     print("真实数字是：" + str(realNum))
    i=1
#     while (guessNum!= realNum) and (i<3):
    while i<4:        
        sNum=input("您还有" + str(4-i) + "次机会猜数字，不妨猜一下数字：")
        try:                   
            if sNum.isdigit():
                guessNum=int(sNum)
                if guessNum ==realNum :
                    print("对了")
                    print("pass")
                    break
                    #return true
                else:
                    i+=1
                    print("您输入的数字是：" + str(guessNum))
                    if guessNum>realNum:                
                        print("猜的数字大了")
                    else:
                        print("猜的数字小了")
                    if i==4:
                        print("您的次数已经用完，真实数字是:" + str(realNum))                
            else:
                print('请输入合法的正整数!!!')
                        

        except ValueError as reason:
            print ("请输入合法的正整数，   错误原因:\n  " + str(reason))
    
            

        

if __name__ == '__main__':
    GuessNum(random.randint(1,10))
    print("游戏结束")