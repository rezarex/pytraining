'''Looping

'''







# questions = ['name', 'quest', 'favorite color']
# for i, j in enumerate(questions):
#     print(dict([(i,j)]))



# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for i, j in knights.items():
#     print(i, j)



# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for i, j in zip(questions, answers):
#     print(f"hi, is your {i} by any chance {j}? ")





# '''Dictionaries

# '''
# tel = {'jack': 4098, 'sape': 4139, 'fiji':9009}
# print(tel)
# tel['hell'] = 666
# print(tel)
# print(list(tel))
# print(sorted(tel))
# print('sape' in tel)
# print(666 in tel) # returns false
# sqrt = {x: x**0.5 for x in range(100) if x % 3 == 0 if x % 9 == 0}
# print(sqrt)





'''Sets

'''

# pinned = {'1','att','att','close','down','shop'}
# print(pinned)
# #print(sorted(pinned))






'''Tuples and sequences

'''

# #tupple creation and unpacking
# user = "wallace", 97, "gunshot"
# name, death_year, reason = user

# print(name)
# print(death_year)
# print(reason)







'''List Comprehension

'''

# matrix = [
#     [5,2,5,6,2, 4],
#     [7,3,4,6,8,5],
#     [3,4,6,12,3,2],
#     [11,4,2,6,8,9]
# ]

# rx = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(rx)



# matrix = [
#     [5,2,5,6,2, 4],
#     [7,3,4,6,8,5],
#     [3,4,6,12,3,2],
#     [11,4,2,6,8,9]
# ]

# rex = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(rex)




# from math import pi
# pi_lst = [str(round(pi, i)) for i in range(9)]
# print(pi_lst)



# vec = [[1,2,3], [4,5,6], [7,8,9]]
# flat = []

# #this
# for elem in vec:
#     for x in elem:
#         flat.append(x)
# print(flat)

# #is same as
# rec = [nu for el in vec for nu in el]
# print(rec)

# seefar = [(x, x**2, x+x) for x in range(12)]
# print(seefar)


# #func starts
# fir = [1,2,3]
# sec = [3,1,4]
# com = []

# #this
# for x in fir:
#     for y in sec:
#         if x != y:
#             com.append((x, y))
# print(com)

# #is same as

# lazy = [(x,y) for x in fir for y in sec if x != y]
# print(lazy)




# square = list(map(lambda x: x**2, range(10)))
# print(square)



# squares = [x**2 for x in range(10)]
# print(squares)