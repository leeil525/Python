import threading
import time
# def threadfun(x,y):
#     for i in range(x,y):
#         time.sleep(1)
#         print(i)
# ta=threading.Thread(target=threadfun,args=(1,6))
# tb=threading.Thread(target=threadfun,args=(100,110))
# ta.start()
# tb.start()
# ta.join()  #等待线程完成再继续
# print('退出')
class Mythread(threading.Thread):
    def __init__(self,x,y):
        threading.Thread.__init__(self)
        self.x=x
        self.y=y
    def run(self):
        for i in range(self.x, self.y):
            time.sleep(1)
            print(i)
        print('子完成')


# def main():
#     a = Mythread(1, 6)
#     a.daemon=True
#     a.start()
#     time.sleep(2)
#     print('主完成')
# main()



'''锁'''
# lock=threading._RLock()
# class mythread(threading.Thread):
#     def run(self):
#         global x
#         lock.acquire()
#         x+=10
#         print('%s:%d'%(self.name,x))
#         lock.release()
# x=0
#
# def main():
#     l=[]
#     for i in range(5):
#         l.append(mythread())
#     for i in l:
#         i.start()
# main()

class Mon(threading.Thread):
    def run(self):
        Dinner.clear()
        print('Cooking dinner')
        time.sleep(3)
        Dinner.set()  # 标志设置为True
        print(self.name, ':dinner is OK!')


class Son(threading.Thread):
    def run(self):
        while True:
            if Dinner.isSet():  # 判断标志位是否被设置为True
                break
            else:
                print('dinner isnot ready!')
                Dinner.wait(1)

        print(self.name, ':Eating Dinner')


def main():
    mon = Mon()
    son = Son()
    mon.name = 'Mon'
    son.name = 'Son'
    mon.start()
    son.start()


if __name__ == '__main__':
    Dinner = threading.Event()
    main()





