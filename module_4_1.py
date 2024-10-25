# fake_math
def divide(first, second):
    if second == 0:
        print('Ошибка')
    else:
        delit_ = first/second
        print(delit_)


#  true_math
from math import inf


def divide(first, second):
    if second == 0:
        print(inf)
    else:
        delit_ = first/second
        print(delit_)
    return inf


# module_4_1
from fake_math import divide as  di1
from true_math import divide as  di2


result1 = di1(69, 3)
result2 = di1(3, 0)
result3 = di2(49, 7)
result4 = di2(15, 0)
