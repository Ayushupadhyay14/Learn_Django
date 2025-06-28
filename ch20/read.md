🧠 Low-Level Caching in Django 5
Low-level caching in Django allows you to manually control what data is cached and when. It's useful for caching specific data (like querysets, API calls, or computed values) instead of whole views or templates.

| Method                                         | Description                                                 |
| ---------------------------------------------- | ----------------------------------------------------------- |
| `cache.set(key, value, timeout=None)`          | Stores a value under the given key                          |
| `cache.get(key, default=None)`                 | Retrieves a value by key, returns default if not found      |
| `cache.add(key, value, timeout=None)`          | Sets a value only if the key doesn’t already exist          |
| `cache.get_or_set(key, default, timeout=None)` | Gets the value or sets it if it doesn’t exist               |
| `cache.set_many(data_dict, timeout=None)`      | Sets multiple values at once using a dictionary             |
| `cache.get_many([key1, key2, ...])`            | Retrieves multiple keys at once                             |
| `cache.delete(key)`                            | Deletes a key from the cache                                |
| `cache.delete_many([key1, key2, ...])`         | Deletes multiple keys                                       |
| `cache.clear()`                                | Clears the entire cache (use with caution)                  |
| `cache.has_key(key)` _(deprecated)_            | Returns `True` if key exists in cache (use `get()` instead) |
| `cache.touch(key, timeout=DEFAULT_TIMEOUT)`    | Resets the timeout for an existing key                      |
