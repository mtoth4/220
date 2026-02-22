import multiprocessing
import random
import time

def whoami():
    delay = random.uniform(0, 1)
    time.sleep(delay)
    print("Process", multiprocessing.current_process().pid,
          "current time:", time.ctime())

if __name__ == "__main__":
    processes = []

    for _ in range(3):
        p = multiprocessing.Process(target=whoami)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()