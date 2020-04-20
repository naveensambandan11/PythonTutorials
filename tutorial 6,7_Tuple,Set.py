Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple = (1,2,45,78,55)
>>> tup;e
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tup;e
NameError: name 'tup' is not defined
>>> tuple
(1, 2, 45, 78, 55)
>>> tuple2 = (1,2,45,78,55, 'naveen','mage', 'anto', 'sowmya')
>>> tuple2
(1, 2, 45, 78, 55, 'naveen', 'mage', 'anto', 'sowmya')
>>> tuple
(1, 2, 45, 78, 55)
>>> tuple[3]
78
>>> tuple[3]= 100
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple[3]= 100
TypeError: 'tuple' object does not support item assignment
>>> set = {1,2,3,45,67,89,3,4,5,5}
>>> set
{1, 2, 67, 3, 4, 5, 45, 89}
>>> tuple.count(45)
1
>>> tuple.index(45)
2
>>> tuple.index(45,)
2
>>> set.add(1000)
>>> set
{1, 2, 67, 3, 4, 5, 1000, 45, 89}
>>> set.add(1000)
>>> set
{1, 2, 67, 3, 4, 5, 1000, 45, 89}
>>> set.clear
<built-in method clear of set object at 0x03648DB8>
>>> set
{1, 2, 67, 3, 4, 5, 1000, 45, 89}
>>> set.clear()
>>> set
set()
>>> set = {1,2,3,45,67,89,3,4,5,5}
>>> set
{1, 2, 67, 3, 4, 5, 45, 89}
>>> set.pop(2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    set.pop(2)
TypeError: pop() takes no arguments (1 given)
>>> set.pop[2]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set.pop[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> set.pop()
1
>>> set
{2, 67, 3, 4, 5, 45, 89}
>>> set.pop(1:3)
SyntaxError: invalid syntax
>>> 