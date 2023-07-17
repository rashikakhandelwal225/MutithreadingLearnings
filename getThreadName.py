from threading import Thread, current_thread

def disp():
    print("Child Thread Name:", current_thread().getName())

t1=Thread(target=disp)
t2=Thread(target=disp)
t1.start()
t2.start()

print("Main Thread Name:",current_thread().getName())

