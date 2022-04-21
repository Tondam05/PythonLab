# QUESTION NO:6

def joinLists(a, b):
    set1 = set(a)
    set2 = set(b)
# converting list into set to remove duplicate values
    if set1 == set2:
        print("The lists are same")
# if the set1 and set2 contain all elements same then it will print true
        file1 = open("common_elements.txt", "w")
        strLine = "\n".join(map(str, set1))
        print(strLine)
        file1.writelines(strLine)
        file1.close()
#  Then writing the common elements in file1
    else:
        print("Lists are different")
# if there is a diffrent elements in set1 and set2 it will print the lists are diffrent

        # Common elements

        set3 = set1.intersection(set2)
# creating set3 using intercection function in which set3 contains common elements in which in set1 and set2
        print(set3)
        file1 = open("common_elements.txt", "w")
        strLine = "\n".join(map(str, set3))
        print(strLine)
        file1.writelines(strLine)
        file1.close()
#  Then writing the common elements in file1

        # Disjoint elements

        set4 = set1.difference(set2)
        set4 = set4.union(set2.difference(set1))
# creating set4 using diffrence function in which set4 contains uncommon elements in which in set1 and set2 contains

        file2 = open("disjoint_elements.txt", "w")
        strLine = "\n".join(map(str, set4))
        print(strLine)
        file2.writelines(strLine)
        file2.close()
#  Then writing the uncommon elements in file2


a = [1, 2, 3, 4, 5, 6]
b = [3, 2, 1, 5, 7]
for i in (map(lambda p, q: p == q, a, b)):
    print(i)
joinLists(a, b)