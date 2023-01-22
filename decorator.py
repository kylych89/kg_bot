# from datetime import datetime
#
#
# def check_time(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         print('start decor')
#
#         func(*args, **kwargs)
#
#         print(datetime.now() - start)
#         print('end decor')
#
#     return wrapper
#
#
# @check_time
# def first(l):
#     for i in range(0, 10):
#         if i % 2 == 0:
#             l.append(i)
#     print(f'I am first func list {l}')
#
#
# @check_time
# def second(count):
#     l = [x for x in range(0, 10) if x % 2 == 0]
#     count = tuple(l)
#     print(f'I am second func tuple {count}')
#
#
# f = first
# s = second
#
# f([1, 2, 3, 4, 5, 6, 7, 8])
# s((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#####################################################################################################################

# def header(func):
#     def inner(*args, **kwargs):
#         print('<h1>')
#
#         func(*args, **kwargs)
#
#         print('</h1>')
#
#     return inner
#
#
# def table(func):
#     def inner(*args, **kwargs):
#         print('<table>')
#
#         func(*args, **kwargs)
#
#         print('</table>')
#
#     return inner
#
#
# @header
# @table
# def say(name, surname, age):
#     print("hello", name, surname, age)
#
#
# say('vasya', 'ivsnov', 30)


########################################################################################################################


# def decor(f):
#     def wrapper():
#         try:
#             h = f()
#         except Exception:
#             print('Try again....')
#             h = f()
#         return h
#
#     return wrapper
#
#
# @decor
# def number():
#     enter = int(input('Enter number: '))
#     print(enter)


# number()

