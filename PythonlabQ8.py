# QUESTION NO:8

from math import sqrt


def eratos(num):
    # max number
    n = num

    # creating list of integers 2,3,4 ... n
    integers = list(range(2, n + 1, 1))
    print(integers)

    # Starting from the first prime number
    j = 0
    while j < len(integers) and integers[j] < sqrt(n):
        # print(len(integers))
        # Determining the limit of iterations
        maxMultiple = int(((integers[-1])) / integers[j]) + 1
        print("prime - %r maxMultiple - %r" % (integers[j], maxMultiple))

        # Looping for all multiples of prime number
        for i in range(2, maxMultiple):
            # print(i)
            try:
                # Removing the multiple of prime number
                integers.remove(integers[j] * i)
            except:
                pass
            print(integers)
        j = j + 1


eratos(40)




