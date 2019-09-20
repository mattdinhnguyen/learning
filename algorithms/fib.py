from functools import reduce

def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

print(reduce(lambda a,b: a+b, filter(lambda a: a%2, fib(4000001))))
