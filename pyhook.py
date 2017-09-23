import pythoncom, pyHook

def OnMouseEvent(event):
    # called when mouse events are received
    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:',event.Time)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Position:',event.Position)
    print('Wheel:',event.Wheel)
    print('Injected:',event.Injected)
    print('---')
    return  True

def onKeyboardEvent(event):
    print("MessageName:", event.MessageName)
    print("Message:", event.Message)
    print("Time:", event.Time)
    print("Window:", event.Window)
    print("WindowName:", event.WindowName)
    print("Ascii:", event.Ascii, chr(event.Ascii))
    print("Key:", event.Key)
    print("KeyID:", event.KeyID)
    print("ScanCode:", event.ScanCode)
    print("Extended:", event.Extended)
    print("Injected:", event.Injected)
    print("Alt", event.Alt)
    print("Transition", event.Transition)
    print("---")

# return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()    #创建管理对象
# watch for all mouse events
hm.KeyDown=onKeyboardEvent   #传入函数,监听键盘
hm.HookKeyboard()  #设置钩子
hm.MouseAll = OnMouseEvent   #传入函数,监听鼠标
hm.HookMouse()  #设置钩子

# wait forever
pythoncom.PumpMessages()
