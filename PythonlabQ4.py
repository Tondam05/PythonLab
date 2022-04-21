# QUESTION NO:4

l = [35, 53, (525, 6743), 64, 63, [743, 754, 757]]
# creating list
def flatten(l):
    result = []
    #creating empty list
    if isinstance(l, (list, tuple)):
    # comparing data type of l with either list or tuple
        for x in l:
    #  iterating list
            result.extend(flatten(x))
    # adding elements to new list
    else:
        result.append(l)
    return result

print(flatten(l))