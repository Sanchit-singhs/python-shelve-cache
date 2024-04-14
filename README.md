---

# Shelve Caching Decorator

## Overview

This Python package provides a decorator leveraging Shelve for persistent caching. The decorator allows efficient caching of function results, improving performance by storing data persistently between program executions.

## Features

- **Persistent Caching:** Utilizes Shelve for persistent storage of cached function results.
- **Efficient Performance:** Caches function results to avoid recomputation, enhancing performance for repeated calls.
- **Easy Integration:** Simple decorator syntax for easy integration with existing functions.
- **Customizable:** Easily configurable to cache functions with different argument combinations.

## Installation

You can install the package using pip:

```bash
pip install shelve-caching-decorator
```

## Usage

1. **Decorator Application:** Use the `@persistent_cache` decorator to cache function results.

    ```python
    from shelvecache import persistent_cache

    @persistent_cache("cache.db")
    def expensive_operation(x, y):
        # Your expensive computation here
        return x * y

    result = expensive_operation(2, 3)  # Function result cached
    ```

2. **Persistent Storage:** The cached results are stored in the specified Shelve file ("cache.db" in the example above), ensuring persistence between program executions.

## Examples

Check the [examples](examples/) directory for detailed usage examples.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize and expand upon this README as needed for your repository!
