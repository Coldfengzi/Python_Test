'''
@author: wyoffice
'''
# import pywinauto.application
# 
# #     def run(self, tool_name):
# #         """
# #         启动应用程序
# #         """
# #         self.app.start_(tool_name)
# #         time.sleep(1)
# 
# # app = pywinauto.application.Application().start('calc.exe')
# # app.CalcFrame.MenuSelect(u'帮助(H)->关于计算器')
# # about_dlg = app.window_(title_re = u'关于“记事本”').window_(title_re = u'确定')
# # about_dlg.print_control_identifiers()
# 
# app = pywinauto.application.Application().start('notepad.exe')
# app.Notepad.TypeKeys(u"杨彦星")


"""----第一个游戏---"""
temp=input("不妨猜一下数字：")
guess=int(temp)
if guess ==8 :
    print("对了")
    print("pass")
else:
    print("错了")
print("游戏结束")
    