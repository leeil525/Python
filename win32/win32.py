import os
import time
import win32gui
import win32ui
import win32api
import win32con
from PIL import ImageGrab
# win32gui.GetClassName(id) 输出类名 win32gui.GetWindowText(id)  输出标题
#left, top, right, bottom = win32gui.GetWindowRect(id)# 可以获取窗口位置
# w1hd=win32gui.FindWindow(类名,标题)    #获取窗体id  可以用spy++或者ViewWizard查看
# w2hd=win32gui.FindWindowEx(722150,None,None,None)#这个应该是查看子窗口 但是没弄懂
# win32gui.SetForegroundWindow(窗口id)   #设置为首窗口
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)#鼠标左键按下 右MOUSEEVENTF_RIGHTDOWN
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)#鼠标左键释放 右MOUSEEVENTF_RIGHTUP
#或者写成win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0 )
# win32api.keybd_event(86,0,0,0)  #例如v键位码是86 自己找键位码
# win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
# win32api.SetCursorPos([765,390])#鼠标定位
# win32gui.CloseWindow(id)#窗口缩小
# win32gui.SendMessage(id,win32con.WM_CLOSE)#窗口关闭









