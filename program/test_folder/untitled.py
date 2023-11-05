import time
from math import floor

print("wow")


print("\nlol")

start_time = time.time()
while True:
    current_time = time.time()
    passed_time = current_time - start_time
    left_time = 10 - floor(passed_time)
    print(left_time)