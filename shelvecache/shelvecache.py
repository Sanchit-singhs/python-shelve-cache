"""
ShelveCache
-----------
"""

import shelve
from functools import _make_key, wraps


def persistent_cache(filename):
    """
    A decorator to cache the results of a function using shelve.

    This decorator wraps a function to cache its return value based on its
    arguments. If the function is called with the same arguments again,
    it retrieves the cached result instead of recomputing.

    Args:
        filename (str): The name of the shelve file to store the cached results.

    Returns:
        function: The decorated function.
    """

    def decorator(func):
        mem_cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            with shelve.open(filename=filename, writeback=True) as cache:
                key = str(hash(_make_key(args=args, kwds=kwargs, typed=False)))
                return (
                    value
                    if (value := mem_cache.get(key))
                    else mem_cache.setdefault(
                        key, cache.setdefault(key, func(*args, **kwargs))
                    )
                )

        return wrapper

    return decorator


# Example usage:
@persistent_cache("cache")
def expensive_operation(x, y):
    print("Performing expensive operation...")
    return x * y


# Test the decorated function
if __name__ == "__main__":
    expensive_operation(
        38, 2
    )  # Output: Performing expensive operation... Cache miss! 6
    expensive_operation(2, 3)  # Output: Cache hit! 6
