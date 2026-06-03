import time
import random
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


def measure_time(sort_func, data):
    start = time.time()
    sort_func(data.copy())
    return time.time() - start

sizes = [100, 500, 1000, 1500, 2000]
bubble_times = []
selection_times = []
insertion_times = []

for size in sizes:
    test_data = [random.randint(0, 10000) for _ in range(size)]
    bubble_times.append(measure_time(bubble_sort, test_data))
    selection_times.append(measure_time(selection_sort, test_data))
    insertion_times.append(measure_time(insertion_sort, test_data))

plt.style.use('bmh')
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
plt.plot(sizes, selection_times, label='Selection Sort', marker='s')
plt.plot(sizes, insertion_times, label='Insertion Sort', marker='h')
plt.title('Bubble sort vs selection sort vs insertion sort')
plt.xlabel('List size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.savefig('n2sorts_trueperformance.png')

if Path("n2sorts_bigo.png").is_file() == False:
    plt.style.use('bmh')
    n = np.linspace(1, 10, 1000)
    plt.figure(figsize=(12, 10))
    plt.ylim(0, 50)

    plt.plot(n, n**2, label="Bubble, selection and insertion sort big O notation")

    plt.legend(loc=0)
    plt.ylabel('Relative Runtime')
    plt.xlabel('Input Size')
    plt.grid(True)
    plt.savefig('n2sorts_bigo.png')
