# QUESTION NO:7
dist1 = {'a': 1, 'b': 2, 'c': 3}
dist2 = {'a': 4, 'd': 'e'}

dict3 = dist1.copy()
dict3.update(dist2)
print(dict3)

""""
  when we have common keys and we merge dicts which having same 
  keys will union since 'a' is the same key in this dicts its update with dict1 
  with its key value in dict2 "a":4, will previle on dict1

"""
# if we need both values in whith same key we can use this

# for k in dist1.keys():
#     if k in dist2.keys():
#         dist1[k] = [dist1[k], dist2[k]]
#
# for k in dist2.keys():
#     if k not in dist1.keys():
#         dist1[k] = dist2[k]
#
# print(dist1)

"""
Same keys in the dict to preserve all the values
i have used list to store all values of that particular duplicate key
"""

# union of dict1 and dict2

# dict3 = {**dist1, **dist2}
# print(dict3)

