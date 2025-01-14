import csv
import sys
from collections import deque

class Process:
    def __init__(self,name,length,start):
        self.name = name
        self.length = length
        self.start = start

class RoundRobinScheduler:
    def __init__(self,filepath,quantum):
        self.quantum = quantum
        self.current_time = 0
        self.waiting_queue = deque()
        self.ready_queue = deque()
        self.filepath= filepath

    def load_processes(self):
        with open(self.filepath, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, length, start = row[0], int(row[1]), int(row[2])
                self.waiting_queue.append(Process(name, length, start))

    def run(self):
        # Wczytanie pliku CSV i utworzenie kolejki, która zawiera oczekujące procesy na uruchomienie (CSV jest już posortowany, więc nie potrzebujemy tego robić lub stosować kolejki priorytetowej).
        self.load_processes()
        #Iteracja kolejnych przebiegów działania programu. Jeżeli obie kolejki są puste, to kończymy działanie programu
        while self.waiting_queue or self.ready_queue:
            #Sprawdzamy, czy są dostępne jakieś procesy do uruchomienia w danym momencie czasowym, jeżeli tak to przenosimy je z kolejki oczekującej na kolejkę szeregowania.
            while self.waiting_queue and self.waiting_queue[0].start <= self.current_time:
                process=self.waiting_queue.popleft()
                self.ready_queue.append(process)
                print(f"T={self.current_time}: New process {process.name} is waiting for execution (length={process.length})")
            #Jeżeli kolejka szeregowania nie jest pusta, to bierzemy pierwszy element i pozwalamy mu działać przez określony kwant czasu (lub aż zakończy swoje działanie, jeżeli trwa krócej).
            if self.ready_queue:
                process=self.ready_queue.popleft()
                time_runner= min(self.quantum,process.length)
                print(f"T={self.current_time}: {process.name} will be running for {time_runner} time units. Time left: {process.length-time_runner}")
            #Jeżeli proces został wywłaszczony (nie zakończył jeszcze swojego działania), to dodajemy go na koniec kolejki szeregowania.
                self.current_time += time_runner
                process.length -= time_runner
                if process.length>0:
                    self.ready_queue.append(process)
                else:
                    print(f"T={self.current_time}: Process {process.name} has been finished")
            else:
                print(f"T={self.current_time}: No processes currently available")
                self.current_time += 1

def main():
    if len(sys.argv) != 3:
        print("Zła ilość argumentów")
        return

    csv_file = sys.argv[1]
    quantum = int(sys.argv[2])

    scheduler = RoundRobinScheduler(csv_file,quantum)
    scheduler.run()

if __name__ == "__main__":
    main()
