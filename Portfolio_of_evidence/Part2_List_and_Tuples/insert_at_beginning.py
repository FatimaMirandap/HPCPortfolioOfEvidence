# insert_at_beginning.py

import timeit

def insert_at_beginning(N):
    my_list = list(range(N))
    def operation():
        my_list.insert(0, 1)
    time_taken = timeit.timeit(operation, number=1000)
    return time_taken

if __name__ == "__main__":
    N_values = [10000, 20000, 30000]
    for N in N_values:
        time_taken = insert_at_beginning(N)
        print(f"Insert 1 at beginning with N={N}: {time_taken:.6f} seconds")
