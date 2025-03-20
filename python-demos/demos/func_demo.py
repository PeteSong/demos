"""
Model Name: func_demo.py
Description: function demos
Author: Peter Song
Date: 2025-02-07
Version: 0.0.1
"""

from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def trace(f: Callable[P, R]) -> Callable[P, R]:
    @wraps(f)  # Update a wrapper function to look like the wrapped function
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        result = f(*args, **kwargs)
        print(f"Calling {f.__name__}({args}, {kwargs}) ====> {result}")
        return result

    return wrapper


def ptimeit(f: Callable[P, R]) -> Callable[P, R]:
    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
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
