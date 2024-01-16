import tracemalloc

tracemalloc.start()

print("Now start running the program...")

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10 ** 6}MB, Peak was {peak / 10 ** 6}MB.")

tracemalloc.stop()
