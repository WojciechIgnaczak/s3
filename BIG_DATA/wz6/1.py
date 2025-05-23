import multiprocessing
import time
from multiprocessing import Queue

def jobConsumer(queue):
    while True:
        msg=queue.get()
        if msg=="DONE":
            break
    print("Consumer done.")

def jobProducer(queue, number):
    for i in range (number):
        queue.put(1024*"   ")
    
    queue.put("DONE")

    print("Producer done.")


def test():
    for number in [10**4,10**5,10**6]:
        queue=Queue()

        consumer=multiprocessing.Process(target=jobConsumer, args=(queue,))
        consumer.start()

        start = time.time()

        jobProducer(queue,number)
        consumer.join()

        stop=time.time()

        result=stop-start

        print(f"{result}s")

if __name__ =='__main__':
    test()