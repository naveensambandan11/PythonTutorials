Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=25
>>> id(num)
1385691440
>>> a=88
>>> id(a)
1385692448
>>> b = a
>>> id(b)
1385692448
>>> id(66)
1385692096
>>> id(88)
1385692448
>>> a=99
>>> id(a)
1385692624
>>> id(b)
1385692448
>>> k = a
>>> id(k)
1385692624
>>> b = k
>>> id(b)
1385692624
>>> x = 5
>>> y=5.5
>>> z='naveen'
>>> xyz = [1.2.3.4.5]
SyntaxError: invalid syntax
>>> xyz = [1,2,3,4,5]
>>> type
<class 'type'>
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> type(z)
<class 'str'>
>>> type(xyz)
<class 'list'>
>>> abc = (6,7,8,9,10)
>>> type(abc)
<class 'tuple'>
>>> dfg = {1,2,3,4,5,6}
>>> type(dfg)
<class 'set'>
>>> 