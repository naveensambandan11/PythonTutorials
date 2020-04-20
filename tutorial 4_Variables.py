Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=6
>>> y=5
>>> x+5
11
>>> x+y
11
>>> print x + ('apples')
SyntaxError: invalid syntax
>>> print(x + 'apples')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(x + 'apples')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> name = 'naveen'
>>> x+name
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x+name
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> name2 = 'mage'
>>> name + name2
'naveenmage'
>>> name2+name
'magenaveen'
>>> x+y
11
>>> _+4
15
>>> name[0:2]
'na'
>>> name2[1:3]
'ag'
>>> name[2:]
'veen'
>>> name2[-3]
'a'
>>> name[3]
'e'
>>> len(name)
6
>>> len(name2)
4
>>> len(name)+len(name2)
10
>>> len(name)-2
4
>>> 