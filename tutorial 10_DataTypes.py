Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> // Datat types
SyntaxError: invalid syntax
>>> //none,numeric, list, tuple, set, string, range, dictonary -- these are the data types in python
SyntaxError: invalid syntax
>>> // none -- variables not assigned with any values
SyntaxError: invalid syntax
>>> //numeric -- int, float, complex, bool
SyntaxError: invalid syntax
>>> a = 2
>>> b=2.456
>>> c = 4+5j
>>> d = a<b
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'complex'>
>>> type(d)
<class 'bool'>
>>> e = int(b)
>>> type(e)
<class 'int'>
>>> e
2
>>> f = float(a)
>>> f
2.0
>>> type(f)
<class 'float'>
>>> ----------------
SyntaxError: invalid syntax
>>> // list, tuple, set, string
SyntaxError: invalid syntax
>>> lst = [1,21,54,78,11]
>>> tple = (4,4l5,14l5,145,55)
SyntaxError: invalid syntax
>>> tple =(4,5,4,5,8,6,7,78,79)
>>> st = {4,415,14l5,145,55}
SyntaxError: invalid syntax
>>> st = {4,415,5,145,55}
>>> type(lst)
<class 'list'>
>>> type(tple)
<class 'tuple'>
>>> type(st)
<class 'set'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> aa = list(range(9))
>>> bb = tuple(range(8))
>>> cc = set(range(7))
>>> aa
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> type(aa)
<class 'list'>
>>> bb
(0, 1, 2, 3, 4, 5, 6, 7)
>>> type(bb)
<class 'tuple'>
>>> cc
{0, 1, 2, 3, 4, 5, 6}
>>> type(cc)
<class 'set'>
>>> ------------------
SyntaxError: invalid syntax
>>> //dictionary -- set assigned with keys for each value
SyntaxError: invalid syntax
>>> dic = {'a':'naveen', 'b':'mages', 'c':'sambandan', 'd': 'udayabanu','e':'kasinathan','f':'revathy'}
>>> dic
{'a': 'naveen', 'b': 'mages', 'c': 'sambandan', 'd': 'udayabanu', 'e': 'kasinathan', 'f': 'revathy'}
>>> type(dic)
<class 'dict'>
>>> dic('a')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dic('a')
TypeError: 'dict' object is not callable
>>> dic['a']
'naveen'
>>> dic['f']
'revathy'
>>> dic.get('e')
'kasinathan'
>>> 