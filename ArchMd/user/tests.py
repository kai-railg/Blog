# # from django.test import TestCase
#
# # Create your tests here.
#
#
# def deco(func):
#     def inner(*args, **kwargs):
#         import cProfile, pstats, io
#         pr = cProfile.Profile()
#         pr.enable()
#         ret = func(*args, **kwargs)
#         pr.disable()
#         s = io.StringIO()
#         ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
#         ps.print_stats()
#         print(s.getvalue())
#         return ret
#
#     return inner
#
#
# @deco
# def hello():
#     print('hello world')
#     l = []
#     for i in range(10000):
#         l.append(i)
#
#
# hello()

def foo():
    a = 1
    return locals()


foo.__dict__ = foo()
print(foo.__dict__)
