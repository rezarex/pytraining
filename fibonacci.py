# a, b = 0, 1

# while a < 10:
#     print(a)
#     a, b = b, a+b

def fib(n):
    result = []
    a, b = 0,1

    while a < n:
        result.append(a)
        a,b = b, a+b
    return result

f100 = fib(100)
print(f100)