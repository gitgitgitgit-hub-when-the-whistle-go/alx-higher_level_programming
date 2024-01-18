dictionary: set of key:value pairs you can access a value by doing dict[key]. this can cause some errors if key do not exist. we can solve this by using dict.get('key') that return None or default value in case key not found by doing dict.get('key', 'default value')
To change or add a value we can do: dict[newKey] = newValue, or by bulk dict.update(k1:v1, k2....)
To remove item: dict.pop(key) or del(dict[key])
Supports len, .keys, .values, .items, for example: for k, v in dict.items():

Corey Schafer - youtube channel - Dictionaries

lambda using examples:
lambda x1, x2, ...: x1 + x2 + ..

