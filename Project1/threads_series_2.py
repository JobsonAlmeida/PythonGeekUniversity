"""

Series link:
https://www.youtube.com/playlist?list=PLS1QulWo1RIb5zGRu6GEej9odbh90hfM6
"""
#
# import _thread
# import time
# def print_epoch(nameOfThread, delay):
#     count = 0
#     while count < 3:
#         time.sleep(delay)
#         count += 1
#         print(nameOfThread, "--------------", time.time())
#
# try:
#     _thread.start_new_thread(print_epoch, ("thread 1", 2))
#     _thread.start_new_thread(print_epoch, ("thread 2", 4))
# except:
#     print("this is an error")
#
# while 1:
#     pass

#
# import threading
# import time
#
# def print_epoch(nameOfThread, delay):
#     count = 0
#     while count < 3:
#         time.sleep(delay)
#         count += 1
#         print(nameOfThread, "--------------", time.time())
#
# def print_cube(num):
#     print("Cube = {}".format(num*num*num))
#
# def print_square(num):
#     print("Square = {}".format(num*num))
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=print_cube, args=(2, ))
#     t2 = threading.Thread(target=print_square, args=(2,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("Done")
#
#
#
#
# import threading
# import time
#
# def print_epoch(nameOfThread, delay):
#     count = 0
#     while count < 3:
#         time.sleep(delay)
#         count += 1
#         print(nameOfThread, "--------------", time.time())
#
# class MyThread(threading.Thread):
#     def __init__(self, name, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#
#     def run(self):  # The start method of a thread runs this run method
#         print("start thread:", self.name)
#         print_epoch(self.name, self.delay)
#         print("end thread:", self.name)

# if __name__ == "__main__":
#
#     t1 = MyThread("Thread-1", 1)
#     t2 = MyThread("Thread-2", 2)
#
#     t1.start()
#     t2.start()
#
#     print(t1.name)
#     print(t2.name)
#     print(threading.active_count())
#     print(threading.current_thread())
#     print(threading.enumerate())
#
#     t1.join()
#     t2.join()
#
#     print("Done")

import threading
x = 0

def thread_task(lock):
    global x
    for i in range(100000000):
        lock.acquire()
        x += 1
        lock.release()

def main_task():

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args= (lock, ))
    t2 = threading.Thread(target=thread_task, args= (lock, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main_task()
    print("{0}".format(x))