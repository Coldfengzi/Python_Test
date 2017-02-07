'''
Created on 2017年1月4日

@author: 08669
'''
import pickle


if __name__ == '__main__':
    my_list=[123,3.14,'小甲鱼',['another list']]
    pickle_file = open('my_list.pickle','wb')
    pickle.dump(pickle_file,my_list)
    pickle_file.close()    