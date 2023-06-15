import time
from threading import Thread

def print_numbers():
    for i in range(1, 10):
        time.sleep(0.5)
        print(i)

def print_numbers2():
    for i in range(1, 10):
        time.sleep(0.8)
        print(i)

def main():
    # Create a new thread and start it
    thread = Thread(target=print_numbers)
    thread2 = Thread(target=print_numbers2)
    thread.start()
    thread2.start()

    # Wait for the thread to complete
    thread.join()
    thread2.join()

    print("All threads have completed")

if __name__ == "__main__":
    main()