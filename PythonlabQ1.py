# QUESTION NO:1
list1 = [[1, 2, 3, 4], ['a', 'b', 'c'], [5, 'd']]

flat_list = [item for items in list1 for item in items]
print('original list,', list1)
print('transform list,', flat_list)
