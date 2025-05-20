import threading
import time     
import random
import multiprocessing 
mylist=[]

def job(n):
    mylist.append(n)
    print(f"Worker number: {n}")

def test():
    workers=[]
    begin = time.time()
    for i in range(24):
        worker=threading.Thread(target=job,args=(i,))
        workers.append(worker)
        worker.start() 
        
    for worker in workers:
        worker.join()

    end=time.time()
    print("DONE")
    print(f"Working time {end-begin} s")
    print(mylist)
    print(len(mylist))

if __name__=="__main__":
    test()