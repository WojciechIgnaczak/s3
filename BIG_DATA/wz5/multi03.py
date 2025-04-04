import threading
import time     
import random
import multiprocessing 
def job(n):
    print(f"worker number {n}")
    v=0
    for i in range (10000):
        for j in range(20000):
            v+=i*j
    print(f"Worker number {n} done")


def test_single_job():
        begin = time.time()
        job(0)
        end=time.time()
        print("DONE sigle job")
        print(f"Working time {end-begin} s")


def test():
    workers=[]
    begin = time.time()
    for i in range(24):
        worker=multiprocessing.Process(target=job,args=(i,))
        workers.append(worker)
        worker.start() 
        
    for worker in workers:
        worker.join()

    end=time.time()
    print("DONE")
    print(f"Working time {end-begin} s")

if __name__=="__main__":
    test_single_job()
    test()