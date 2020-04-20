Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> List = [2,4,5,6,888,97,100]
>>> List
[2, 4, 5, 6, 888, 97, 100]
>>> List(2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    List(2)
TypeError: 'list' object is not callable
>>> List[2]
5
>>> list[-1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list[-1]
TypeError: 'type' object is not subscriptable
>>> List[-1]
100
>>> List2 = List + 45
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    List2 = List + 45
TypeError: can only concatenate list (not "int") to list
>>> List2 = ['naveen', 'mage', 'anto', 'sowmya']
>>> ListAll = List + List2
>>> ListAll
[2, 4, 5, 6, 888, 97, 100, 'naveen', 'mage', 'anto', 'sowmya']
>>> ListAll[-1]
'sowmya'
>>> ListAll[-1,-2]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ListAll[-1,-2]
TypeError: list indices must be integers or slices, not tuple
>>> ListAll [0:6]
[2, 4, 5, 6, 888, 97]
>>> ListAll[-1:2]
[]
>>> List.append (25)
>>> List
[2, 4, 5, 6, 888, 97, 100, 25]
>>> List.append[25]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    List.append[25]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> List.count
<built-in method count of list object at 0x034EAD48>
>>> List
[2, 4, 5, 6, 888, 97, 100, 25]
>>> List.insert(3,''sri')
	    
SyntaxError: invalid syntax
>>> List.insert(3,'sri')
>>> List
[2, 4, 5, 'sri', 6, 888, 97, 100, 25]
>>> List.insert(-1,'dine')
>>> List
[2, 4, 5, 'sri', 6, 888, 97, 100, 'dine', 25]
>>> List
[2, 4, 5, 'sri', 6, 888, 97, 100, 'dine', 25]
>>> List.reverse
<built-in method reverse of list object at 0x034EAD48>
>>> List
[2, 4, 5, 'sri', 6, 888, 97, 100, 'dine', 25]
>>> List.pop(2)
5
>>> List
[2, 4, 'sri', 6, 888, 97, 100, 'dine', 25]
>>> List.pop()
25
>>> List
[2, 4, 'sri', 6, 888, 97, 100, 'dine']
>>> List.index
<built-in method index of list object at 0x034EAD48>
>>> List
[2, 4, 'sri', 6, 888, 97, 100, 'dine']
>>> del List
>>> List
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    List
NameError: name 'List' is not defined
>>> ListAll
[2, 4, 5, 6, 888, 97, 100, 'naveen', 'mage', 'anto', 'sowmya']
>>> ListAll.append [12,15,17]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    ListAll.append [12,15,17]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> ListAll.extend[12,15,17]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ListAll.extend[12,15,17]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> ListAll.extend([12,15,17])
>>> ListAll
[2, 4, 5, 6, 888, 97, 100, 'naveen', 'mage', 'anto', 'sowmya', 12, 15, 17]
>>> ListAll.max
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ListAll.max
AttributeError: 'list' object has no attribute 'max'
>>> ListAll(max)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    ListAll(max)
TypeError: 'list' object is not callable
>>> max(LiatAll)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    max(LiatAll)
NameError: name 'LiatAll' is not defined
>>> max(ListAll)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    max(ListAll)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> ListAll
[2, 4, 5, 6, 888, 97, 100, 'naveen', 'mage', 'anto', 'sowmya', 12, 15, 17]

>>> List_nums[] = [2,4,5,6,888,97,100]
SyntaxError: invalid syntax
>>> List_nums = [2,4,5,6,888,97,100]
>>> List_nums
[2, 4, 5, 6, 888, 97, 100]
>>> max(List_nums)
888
>>> min(List_nums)
2
>>> sum(List_nums)
1102
>>> List_nums.sort()
>>> List_nums
[2, 4, 5, 6, 97, 100, 888]
>>> List_nums.sort(desc)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    List_nums.sort(desc)
NameError: name 'desc' is not defined
>>> List_nums.sort(reverse = True)
>>> List_nums
[888, 100, 97, 6, 5, 4, 2]
>>> 