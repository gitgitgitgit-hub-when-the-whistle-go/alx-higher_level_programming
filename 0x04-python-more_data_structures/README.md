dictionary: set of key:value pairs you can access a value by doing dict[key]. this can cause some errors if key do not exist. we can solve this by using dict.get('key') that return None or default value in case key not found by doing dict.get('key', 'default value')
To change or add a value we can do: dict[newKey] = newValue, or by bulk dict.update({k1:v1}, {k2....})
To remove item: dict.pop(key) or del dict[key] (not a function lmao)
Supports len, .keys (dict.keys() don't return a list), .values, .items, for example: 'for k, v in dict.items():'

set is imutable and don't support list methods but have len.

lambda using examples:
lambda x1, x2, ...: x1 + x2 + ..
list(map(func, itterable))
my initial answer for 101-.. : return [list(map(lambda x: x ** 2, sub_list)) for sub_list in matrix]
but we can use a lambda list_matrix: list(map(...)) inside another map(this, matrix). A map inside another map. Nested map confrm333d ??
https://docs.python.org/3/tutorial/datastructures.html#sets
https://python-course.eu/advanced-python/lambda-filter-reduce-map.php
https://python-course.eu/advanced-python/list-comprehension.php
Corey Schafer - youtube channel - Dictionaries
