
import time

current_time = time.time()
print(current_time)  # seconds since January 1st, 1970


# Decorator to calculate how long a function takes to run
def speed_calc_decorator(function):

    def wrapper_function():
        start_time = time.time()

        function()

        end_time = time.time()

        run_time = end_time - start_time

        print(f"{function.__name__} run speed: {run_time}s")

    return wrapper_function


# Fast function
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


# Slow function
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


# Run both functions
fast_function()
slow_function()



