# Script based python 3.7
# 赋值：只拷贝地址，；list1改变后list2也会跟着变
# 浅拷贝：只拷贝外层，故list1改变后list2外层不变，只有可能内层发生改变
# 深拷贝：完整拷贝， 无论list1发生怎样的变化，list2完全不会改变

import copy

a = [1,2,3,4,['a','b']]
b = a                   # 赋值
c = a[:]                # 浅拷贝
d = copy.copy(a)        # 浅拷贝
e = copy.deepcopy(a)    # 深拷贝

a.append(5)
a[4].append('C')

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
print('e=',e)
