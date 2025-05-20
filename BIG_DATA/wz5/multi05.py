import threading
import time     
import random
import multiprocessing 
from multiprocessing import Queue

def job(n, queue):
    queue.put(n)
    v=0
    for i in range(10000):
        for j in range(2000):
            v*=i*j
    print(f"Worker number: {n}")


def test():
    queue=Queue()
    workers=[]
    begin = time.time()
    for i in range(24):
        worker=multiprocessing.Process(target=job,args=(i,queue))
        workers.append(worker)
        worker.start() 
        
    for worker in workers:
        worker.join()

    mylist=[]
    while not queue.empty():
        mylist.append(queue.get())
    print(mylist)

    end=time.time()
    print("DONE")
    print(f"Working time {end-begin} s")
   

if __name__=="__main__":
    test()