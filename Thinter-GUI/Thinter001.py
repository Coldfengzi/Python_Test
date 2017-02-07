'''
Created on 2017年1月23日

@author: 08669
'''
from tkinter.messagebox import askokcancel

import tkinter as tk


class App:
    def __init__(self,root):
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame,text="打招呼",command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)
    def say_hi(self):
         askokcancel("FishC Demo","发射核弹", icon="error")
    


def main():
    root=tk.Tk()
    root.title("FishC Demo")
    theLabel = tk.Label(root,text="我的窗口程序")

    v = tk.IntVar()
    v.set(1)
    for i in range(3):
        tk.Radiobutton(root,variable = v,text = 'python%d' % i,value = i).pack()
    
#     tk.Radiobutton(root,text = 'python').pack()
#     tk.Radiobutton(root,text = 'tkinter').pack()
#     tk.Radiobutton(root,text = 'widget').pack()
    

    theLabel.pack()
    app=App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
   