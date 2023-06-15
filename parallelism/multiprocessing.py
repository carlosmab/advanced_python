import concurrent.futures
import time

numbers = [40000, 50000, 60000]

# Function to perform a CPU-bound task
def square(n):
    for i in range(n):
        ...
    return n ** 2

def measure_time(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    return result


def perform_multiprocessing_tasks():
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as pool:
        results = pool.map(square, numbers)
    return results


def perform_multithreaded_tasks():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)
    return results


if __name__ == '__main__':
    print("multiprocessing time: ", measure_time(perform_multiprocessing_tasks))
    print("multithreaded time: ", measure_time(perform_multithreaded_tasks))
    