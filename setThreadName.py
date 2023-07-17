from threading import Thread, current_thread

def disp():
    # print('Default Child Thread', current_thread().name)
    # current_thread().name = "Flying Thread"
    # print('New Child Thread', current_thread().name)
    pass

# #Child Thread
# t= Thread(target=disp())   
# t.start()   
# print(t.getName())
# t.setName('Doc Thread')
# print(t.getName())

t=Thread(target=disp(), name='Raj Thread')
print(t.name)