def f(a, b):
    print(a + b)
    return a + b

if __name__ == '__main__':
    # import lib
    # a = lib.Base()
    from lib import Base
    a = Base()
    a.g()
    a.h()
    # # variable
    # a = 1
    # # reassign
    # a = 'string1'
    # print(a)
    # a = "string2"
    # print(a)
    # # list
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(a[0])
    # print(a[-1])
    #
    # # slice
    # print(a[0: 5: 2])
    # print(a[-1: : -2])
    # print(a[0: 2])
    #
    # # dictionary
    # a = {'key1': 'value1', 'key2': 'value2', 1: 'value3'}
    # print(a['key1'])
    #
    # # tuple
    # x = (1, 2, 3)
    # x = [1, 2, 3]
    # a, b, c = x # a = 1, b = 2, c = 3 tuple unpack
    # print(a, b, c)



