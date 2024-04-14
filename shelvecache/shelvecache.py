import functools
import shelve


def persistent_cache(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with shelve.open(filename) as cache:
                key = (args, frozenset(kwargs.items()))
                if key in cache:
                    print("Cache hit!")
                    return cache[key]
                else:
                    print("Cache miss!")
                    result = func(*args, **kwargs)
                    cache[key] = result
                    return result

        return wrapper

    return decorator


# Example usage:
@persistent_cache("cache.db")
def expensive_operation(x, y):
    print("Performing expensive operation...")
    return x * y


# Test the decorated function

if __name__ == "__main__":
    print(
        expensive_operation(2, 3)
    )  # Output: Performing expensive operation... Cache miss! 6
    print(expensive_operation(2, 3))  # Output: Cache hit! 6
