
import threading
import time
import random

def job(n):
    print(f"Worker number {n}: ")

    v = 0
    for i in range(10000):
        for j in range(20000):
            v += i*j

    print(f"Worker number {n}: done")



def test():
    workers = []

    begin = time.time()

    for i in range(24):
        worker = threading.Thread(target=job, args=(i,))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

    end = time.time()

    print("Done")
    print(f"Working time {end-begin} s")

if __name__ == "__main__":
    test()