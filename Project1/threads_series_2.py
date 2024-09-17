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


import threading
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "--------------", time.time())

def print_cube(num):
    print("Cube = {}".format(num*num*num))

def print_square(num):
    print("Square = {}".format(num*num))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube, args=(2, ))
    t2 = threading.Thread(target=print_square, args=(2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")
