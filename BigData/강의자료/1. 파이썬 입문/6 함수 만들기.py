'''
>>> add_num1(1,3)
1 + 3 = 4 (함수 안에서 출력되는 값)
4 (리턴값)'''

def add_num1(a, b):
    c = a+b
    print("{} + {} = {}".format(a, b, c))
    return c
