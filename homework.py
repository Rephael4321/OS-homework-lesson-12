import os
import multiprocessing
import time


def main(num):
    print("Main process")
    print(f"PID: {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")
    print()
    process = multiprocessing.Process(target=count, args=(num, ))
    process.start()
    print("Stater but not joined")
    process.join()


def count(num):
    print("Sub process (count)")
    print(f"PID: {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")
    print()
    for x in range(num):
        print(x)
        time.sleep(1)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print()
    main(number)
