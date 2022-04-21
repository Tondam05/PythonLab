# QUESTION NO:14

def fib():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b

def power(li):
    for i in range(len(li)):
        yield li[i]*li[i]

obj = fib()
fiblist = []

for i in range(10):
    fiblist.append(next(obj))

print(fiblist)
p = power(fiblist)
sumofFib = 0
for i in range(10):
    sumofFib += next(p)

print("sum of Fib numbers: %r" %(sumofFib))
