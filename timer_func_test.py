import time
import math

def timer(start_time, left_time):
    current_time = time.time()
    passed_time = current_time - start_time
    return left_time - math.floor(passed_time)