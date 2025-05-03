# import _thread
# import time

# def display(message):
#     count = 0
#     while count <= 5:
#         count += 1
#         time.sleep(2)
#         print("display", message)

# def display1(message):
#     count = 0
#     while count <= 5:
#         count += 1
#         time.sleep(2)
#         print("display1", message)

# try:
#     _thread.start_new_thread(display, ("thread1",))
#     _thread.start_new_thread(display1, ("thread2",))

# except:
#     print("An error occurred in the program")

# # Keep main thread alive
# while True:
#     time.sleep(1)



import threading
import time

def function(num):
    for i in range(1,num+1):
        time.sleep(2)
        print(i)

try:
    t=threading.Thread(target=function(10))
    t.start()
except:
    print("eror is occured")


