# from django.test import TestCase

# Create your tests here.
#
# def my_generator():  # 子生成器
#     for i in range(5):
#         if i == 2:
#             return '我被迫中断了'
#         else:
#             yield i
#
#
# def wrap_my_generator(generator):  # 委托生成器
#     result = yield from generator
#     # 自动触发StopIteration异常，并且将return的返回值赋值给yield from表达式的结果，即result
#     print('这是return 的返回值，', result)
#
#
# def main(generator):
#     print(type(generator))
#     # yield from generator
#     print([i for i in generator])
#
# g = my_generator()
# wrap_g = wrap_my_generator(g)
# main(wrap_g)
