import os
import multiprocessing
import time


def main(num):
    print("Main process")
    print(f"PID: {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")
    print()
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=count, args=(num, queue))
    process.start()
    print("Stater but not joined")
    process.join()
    total = queue.get()
    print(f"The total is {total}")


def count(num, queue):
    print("Sub process (count)")
    print(f"PID: {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")
    print()
    total = 0
    for x in range(num):
        total += x
        print(x)
        time.sleep(1)
    queue.put(total)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print()
    main(number)
