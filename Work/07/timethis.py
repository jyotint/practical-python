# Exercise 7.10: A decorator for timing

# timethis.py

import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}::{func.__name__}() - Executed in {end-start:.5f} second(s).')
        return return_value
    return wrapper

def logthis(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__module__}::{func.__name__}() - Execution started...')
        return_value = func(*args, **kwargs)
        print(f'{func.__module__}::{func.__name__}() - Execution completed. Return Value: {return_value}')
        return return_value
    return wrapper


if __name__ == '__main__':
    
    @logthis
    @timethis
    def countdown(n):
        n_initial = n
        while n > 0:
            time.sleep(1)
            n -= 1
        return f"counted {n_initial}"

    countdown(2)
