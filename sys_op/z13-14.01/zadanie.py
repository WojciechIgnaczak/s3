import csv
import sys
from collections import deque

class Process:
    def __init__(self, name, length, start):
        self.name = name
        self.length = length
        self.start = start

class RoundRobinScheduler:
    def __init__(self, quantum):
        self.quantum = quantum
        self.current_time = 0
        self.waiting_queue = deque()
        self.ready_queue = deque()

    def load_processes(self, filepath):
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, length, start = row[0], int(row[1]), int(row[2])
                self.waiting_queue.append(Process(name, length, start))

    def run(self):
        while self.waiting_queue or self.ready_queue:
            # Check for new processes to move to the ready queue
            while self.waiting_queue and self.waiting_queue[0].start <= self.current_time:
                process = self.waiting_queue.popleft()
                print(f"T={self.current_time}: New process {process.name} is waiting for execution (length={process.length})")
                self.ready_queue.append(process)

            if self.ready_queue:
                process = self.ready_queue.popleft()
                time_to_run = min(process.length, self.quantum)
                print(f"T={self.current_time}: {process.name} will be running for {time_to_run} time units. Time left: {process.length - time_to_run}")
                self.current_time += time_to_run
                process.length -= time_to_run

                if process.length > 0:
                    self.ready_queue.append(process)
                else:
                    print(f"T={self.current_time}: Process {process.name} has been finished")
            else:
                print(f"T={self.current_time}: No processes currently available")
                self.current_time += 1

def main():
    if len(sys.argv) != 3:
        print("Usage: python rr.py <csv_file> <quantum>")
        return

    csv_file = sys.argv[1]
    quantum = int(sys.argv[2])

    scheduler = RoundRobinScheduler(quantum)
    scheduler.load_processes(csv_file)
    scheduler.run()

if __name__ == "__main__":
    main()
