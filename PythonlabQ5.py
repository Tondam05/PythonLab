# QUESTION NO:5
dict1 = {'a': 1, 'b': 2, 'c': None, 'd': 'z', 'e': None}

result = {key: value for key, value in dict1.items() if value is not None}

print(result)
