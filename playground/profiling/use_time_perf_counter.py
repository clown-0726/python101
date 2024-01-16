import time

start_extract_time = time.perf_counter()

time.sleep(1)

end_extract_time = time.perf_counter() - start_extract_time
print(f'End extract pdf with cost time {str(end_extract_time * 1000)}')
