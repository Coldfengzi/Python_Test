'''
Created on 2016年12月23日

@author: 08669
'''

if __name__ == '__main__':
    iformat = ('%s%04d')%('abc',5)
    iformat = '{2}:{0}'.format('2', '3','1')
    print(iformat)
    
    num1 = 1,2,3,4,5
    num2 = 6,7,8,9
    
    print(sum(num1)+sum(num2))
    
    
#     str1='FishC'
#     for each in enumerate(str1):
#         print(each)
        
    list1 = [1,3,5]
    list2 = 'FishC'
    for each in zip(list1,list2):
        print(each)