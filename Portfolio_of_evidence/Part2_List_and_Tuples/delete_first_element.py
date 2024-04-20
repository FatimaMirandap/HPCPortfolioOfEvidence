
# delete_first_element.py

import timeit

def delete_first_element(N):
    my_list = list(range(N))
    def operation():
        my_list.pop(0)
    time_taken = timeit.timeit(operation, number=1000)
    return time_taken

if __name__ == "__main__":
    N_values = [10000, 20000, 30000]
    for N in N_values:
        time_taken = delete_first_element(N)
        print(f"Delete first element with N={N}: {time_taken:.6f} seconds")
