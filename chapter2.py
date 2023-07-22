'''
find prime numbers between 1 and 100
for each that is not, pring x is not a prime number
'''

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# #pairs.sort(key=lambda pair: pair[1], reverse=True)
# pairs[len(pairs):]=[(5, "five")]
# pairs.insert(len(pairs),(6, "Six"))
# pairs.insert(2, (0.5, 'point 5'))
# print(pairs)
# pairs.remove((0.5, 'point 5'))
# print(pairs)
# pairs.remove(pairs[0])
# print(pairs)

# def concat(*args, sep="-"):
#     return sep.join(args)

# print(concat("dance","like","you","mean","it", sep="<:>"))



# for n in range(2,10):
#     if n % 2 == 0:
#         print(f"{n} is even")
#         continue
#     print(f"{n} is odd")


# for n in range(2, 40):
#     for x in range(2,n):
#         if n % x == 0:
#             print(f"{n} is most likely not a prime")
#             break
#     else:
#         print(f"{n} is probably a prime")








# 
# 
# 
#  for n in range(2,20):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//2}")
#             break
#     else:
#         print(n, "is a prime")



# print(list(range(10)))



'''
loop through list and get indices and each length
'''
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i], len(a[i]))
#     print(len(a))


'''
for loop wth a step using range
'''
# for i in range(1,700,27):
#     print(i)




'''
simple implementation of a for statement to multiply each number by itself
'''

# numbers = [1,23,2,4,6,7]
# words = ['cat', 'window', 'defenestrate']

# for n in numbers:
#     print(n*n)




# for w in words[:]:
#     if len(w)>6:
#         words.insert(1, w)
# print(words)



# words.sort(key=lambda x: len(x), reverse=True)

# for w in words:
#     print(w)