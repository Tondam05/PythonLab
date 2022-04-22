# QUESTION NO:2
tuple1 = (('k', 5), ('n',1), ('a', 7), ('t', 6), ('j', 11))

print('My orginal tuple is :', tuple1,)
print('*'*50)
sort = sorted(tuple1)
print('sorting the tuple using the key value: ', sort)
sorts_revers = sorted(tuple1,reverse=True)
print('printing the sorted list in reverse: ', sorts_revers)


#      Sorting using second key value

# sort = sorted(tuple1,key=lambda x:x[1])
# print('sorting the tuple using the second value: ', sort)
# sorts_revers = sorted(tuple1,reverse=True,key=lambda x:x[1])
# print('printing the sorted list in reverse by second value: ', sorts_revers)