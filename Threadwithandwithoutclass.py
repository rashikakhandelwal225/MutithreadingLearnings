from threading import Thread
# def disp():
    # for i in range(5):
    #     print("Child Thread is publishing video ")
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread is publishing video ")


# for i in range(5):
# t= Thread(target=disp)

t=Mythread()
t.start()
#join() is to let the child thread execute complete its loop / finish its task completely then next thread ie, Main thread will execute 
t.join()   

for i in range(5):
    print("Main Thread is publishing video ")

#Order of execution of child and main thread is unordered/ it executes randomly