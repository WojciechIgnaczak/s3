import threading
import time     
import random

def job(n):
    sleep_time=random.randint(1,3)
    print(f"worker number {n}: sleep for {sleep_time} seconds")
    time.sleep(sleep_time)
    print(f"Worker number {n} done")

def test():
    begin = time.time()
    for i in range(24):
        threading.Thread(target=job,args=(i,)).start()
    end=time.time()
    print("DONE")
    print(f"Working time {end-begin} s")

if __name__=="__main__":
    test()