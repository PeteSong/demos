"""
Model Name: func_demo.py
Description: function demos
Author: Peter Song
Date: 2025-02-07
Version: 0.0.1
"""

from functools import wraps


def trace(f):
    @wraps(f)  # Update a wrapper function to look like the wrapped function
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f"Calling {f.__name__}({args}, {kwargs}) ====> {result}")
        return result

    return wrapper


def ptimeit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(
            f"""Calling {f.__name__}({args}, {kwargs})
        ====> {result}
        in {execution_time:.6f} seconds"""
        )
        return result

    return wrapper
