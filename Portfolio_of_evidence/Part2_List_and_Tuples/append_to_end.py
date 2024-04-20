
# append_to_end.py

import timeit

def append_to_end(N):
    my_list = list(range(N))
    def operation():
        my_list.append(1)
    time_taken = timeit.timeit(operation, number=1000)
    return time_taken

if __name__ == "__main__":
    N_values = [10000, 20000, 30000]
    for N in N_values:
        time_taken = append_to_end(N)
        print(f"Append 1 at end with N={N}: {time_taken:.6f} seconds")
