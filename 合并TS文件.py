import os
import time
import shutil


os.chdir(r'D:\迅雷下载\合并')#自己修改
file=os.listdir()

def get_file():
    file_1=[]
    for o in range(len(file)):
        number=os.path.splitext(file[o])
        file_1.append(int(number[0]))
    file_1.sort()
    return file_1

file_1=get_file()
def Do_file(file_1):
    for i in range(len(file_1)-1):#len(file_1)
        shell_str='copy /b'+' '+str(file_1[0])+'.ts+'+str(file_1[i+1])+'.ts '+str(file_1[0])+'.ts'
        os.system(shell_str)
        del_str='del \Q {0}.ts'.format(str(file_1[i+1]))
        os.system(del_str)
        print('total'+str(len(file_1))+ 'finish'+str(i))
        time.sleep(0.4)
Do_file(file_1)
