import threading
import time     
import random
import multiprocessing 
from multiprocessing import Pipe

def job(n, pipe):
    pipe.send(n)
    v=0
    for i in range(10000):
        for j in range(2000):
            v+=i*j
    print(f"Worker number: {n}")


def test():
    workers=[]
    pipes=[]
    begin = time.time()
    for i in range(24):
        pipeParent, pipeChild =Pipe()
        worker=multiprocessing.Process(target=job,args=(i,pipeChild))
        workers.append(worker)
        pipes.append(pipeParent)

        worker.start() 
    for worker in workers:
        worker.join()

    mylist=[]
    number=0
    new_pipes= pipes

    while number<24:
        for p in new_pipes:
            data=p.recv()
            if data is not None:
                number +=1
                mylist.append(data)
                pipes.remove(p)

        new_pipes = pipes
        time.sleep(1)
    
    end=time.time()
    print("DONE")
    print(f"Working time {end-begin} s")
    print(mylist)


if __name__=="__main__":
    test()