'''
Created on 2016年12月22日

@author: 08669
'''

if __name__ == '__main__':
    anumber=[1,2,3,4,5]
    anumber.extend(['6',7])
    anumber.insert(0, 0)
    anumber.insert(0, 0)
    bnumber=anumber[:9:2]
    bnumber *= 3
    print(anumber.pop(0))
    
#     anumber[1],anumber[3],anumber[4] = anumber[3],anumber[1],anumber[5]
    print(anumber)
    print(len(anumber))
    print(bnumber)
    cnumber=['小鸭','小鱼','小甲鱼']
    print('小' in cnumber)
    
    