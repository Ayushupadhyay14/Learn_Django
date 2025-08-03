from collections.abc import Iterable
# define a function '
def flatten(lst):
    for item in lst:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)

        else:
            yield item


arr = [1, 1, [2, 2, [3, 3, [4, 4, [5, 5]]]]]
flat = list(flatten(arr))
unique_sorted = sorted(set(flat))
total = sum(unique_sorted)

print("float unique list:", unique_sorted)
print("Sum", total)
