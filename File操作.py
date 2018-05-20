import os
os.getcwd()  #得到当前脚本工作的目录
os.listdir() #得到指定目录下的我所有文件和目录名
os.remove()  #删除文件，不能删除目录
os.removedirs()  #删除多个目录
os.path.isfile() #判断文件
os.path.isdir()  #判断目录
os.path.isabs()  #判断是否是绝对路径
os.path.exists() #判断给出的路径是否真的存在
os.path.split()  #D:\Github  ('D:\\','Github')
os.path.splitext() #D:\Github.py ('D:\\Github','.py')
os.path.dirname()   #返回当前文件位置的目录 D:\\Github   D:\\
os.path.basename()  #返回当前文件名 D:\\Github Github
os.system()         #cmd命令
os.rename(old, new) #重命名
os.makedirs()       #创建多级目录
os.mkdir()          #创建单级目录
os.stat()           #获取文件的属性
os.chmod('位置','权限')      #这里的权限要用stat模块中的参数
os.path.getsize()            #获取文件的大小
shutil.copyfile( src, dst)   #从源src复制到dst中去
shutil.move( src, dst)       #移动文件或重命名
shutil.copymode( src, dst)   #只是会复制其权限其他的东西是不会被复制的
shutil.rmtree( src )         #递归删除一个目录以及目录内的所有内容
shutil.copy( src, dst)       #复制到dst
shutil.copytree( olddir, newdir, True/Flase)'''把olddir拷贝一份newdir，如果
第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参
数是False，则将在复制的目录下生成物理副本来替代符号连接'''

