import time
import matplotlib.pyplot as plt

from searching import linear_search, binary_search
from generators import ordered_sequence

sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
lin_times = []
bin_times = []

# num_trials = 20

# print("Zahajuji měření...")

for size in sizes:
    data = ordered_sequence(size)
    target = size + 1

    start_time = time.perf_counter()
    linear_search(data, target)

    end_time = time.perf_counter()
    lin_times.append(end_time - start_time)

    start_time = time.perf_counter()
    binary_search(data, target)

    end_time = time.perf_counter()
    bin_times.append(end_time - start_time)

plt.plot(sizes, lin_times, color="blue", label="Sekvenční hledání")

plt.plot(sizes, bin_times, color="red", label="Binární hledání")

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.grid(True)
plt.legend("LB")
plt.title("Porovnání časové složitosti: Sekvenční vs. Binární hledání")

plt.show()
