# # dict1 = {'a': 1, 'b': 2, 'c': None, 'd': 'z', 'e': None}
# #
# #
# #
# # print(dict1.keys())
# # print(dict1.values())
# # del dict1[None]
# # print(dict1)
#
# def common_data(list1, list2):
#     result = False
#     for x in list1:
#         for y in list2:
#             if x == y:
#                 result = True
#                 return result
#
# print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
# print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

def test_includes_any(nums, lsts):
    for x in lsts:
        if x in nums:
            return True
    return False
print(test_includes_any([10, 20, 30, 40, 50, 60], [22, 42]))
print(test_includes_any([10, 20, 30, 40, 50, 60], [20, 80]))

