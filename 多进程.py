#from multiprocessing import Process
#import os
#import time
'''multiprocessing'''
# def run_proc(name):
#     time.sleep(3)
#     print('run child process %s(%s)...'%(name,os.getpid()))
#
# if __name__=='__main__':
#     print('parent process %s'%(os.getpid()))
#     processes=list()
#     for i in range(5):
#         p=Process(target=run_proc,args=('test',))
#         print('Process will start.')
#         p.start()
#         processes.append(p)
#     for p in processmes:
#         p.join()
#     print('Process end.')
'''Pool'''
# import multiprocessing
# import time
# def func1(msg,i):
#     print('msg:',msg)
#     time.sleep(i)
#     print('end123')
# if __name__=='__main__':
#     pool=multiprocessing.Pool(processes=4)
#     for i in range(5):
#         msg='hello %d'%(i)
#         pool.apply_async(func1,args=(msg,i,)) #apply阻塞 appy_async不阻塞
#     print('hhahahha~~~~')
#     pool.close()
#     pool.join() #在close后面

'''Queue'''
# from multiprocessing import Process,Queue
# import random,time
# def wt(q):
#     u=['1','2','3']
#     for i in u:
#         q.put(i)
#         time.sleep(random.random())
#
# def rt(q):
#     while(True):
#         print(q.get())
#
# if __name__== '__main__':
#     q=Queue()
#     pw=Process(target=wt,args=(q,))
#     pr = Process(target=rt, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()









