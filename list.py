# from ast import Str
#
#
# def my_common():
#     A = [1,2,3,4,5,6]
#     B = [3,5,7,8,9,10]
#     c=[]
#     for i in A:
#             if i in B:
#                 print(i)
#             else:
#                 print(i+100)
# my_common()

def common_member(list1, list2):
    a_set = set(list1)
    b_set = set(list2)
    if (a_set & b_set):
        return True
    else:
        return False


list1 = [3, 6, 9, 12, 15]
list2 = [2, 4, 6, 8, 10, 12, 14]
print(common_member(list1, list2))

list1 = [3, 6, 9, 12, 15]
list3 = [20, 25, 30, 35]
print(common_member(list1, list3))


# def common_items(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     if(set1 & set2):
#         print ('common elements: ' + str(set1 & set2))
#     else:
#         print( 'No common elements' + str(set1 & set2))
def common_member(a, b):
    set1 = set(list1)
    set2 = set(list2)
    result = [i for i in a if i in b]
   # path = "C:\Users\252834\Desktop\common_elements.txt"
   #  file = open("C:\Users\252834\Desktop\common_elements.txt",'w')
    file1 = open("common_elements.txt", "w")
    strLine = "\n".join(map(str, set1))
    print(strLine)
    file1.writelines(strLine)
    file1.close()
    for element in result:
        # file.writelines(element + "/n")
      return result


list1 = [3, 6, 9, 12, 15]
list2 = [2, 4, 6, 8, 10, 12, 14]
# list3 = [15, 20, 25, 30, 35]

ac = common_member(list1, list2)
print(ac)


# common_items(list1, list3)
# common_items(list2, list3)

def uncommon_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if (set1 ^ set2):
        print('Uncommon elements: ' + str(set1 ^ set2))
        file2 = open("disjoint_elements.txt", "w")
        strLine = "\n".join(map(str, set2))
        print(strLine)
        file2.writelines(strLine)
        file2.close()

    else:
        print('No Uncommon elements')


list1 = [3, 6, 9, 12, 15]
list2 = [2, 4, 6, 8, 10, 12, 14]
# list3 = [15, 20, 25, 30, 35]
uncommon_items(list1, list2)
