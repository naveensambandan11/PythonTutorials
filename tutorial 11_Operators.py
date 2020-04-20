Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  //arithmatic, assignment, unary
 
SyntaxError: unexpected indent
>>> arithmatic - +,-,*,/,//,%
SyntaxError: invalid syntax
>>> a = 100
>>> b = 200
>>> c = 1000
>>> 
>>> a+b
300
>>> b-a
100
>>> a*c
100000
>>> c/b
5.0
>>> c//a
10
>>> c%a
0
>>> assignment operators -- =, +=, -+, *=, /+
SyntaxError: invalid syntax
>>> assignment operators -- =, +=, -+, *=, /=
SyntaxError: invalid syntax
>>> a+=5
>>> a =
SyntaxError: invalid syntax
>>> a
105
>>> b+=10
>>> b
210
>>> c-=500
>>> c
500
>>> d/=5
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d/=5
NameError: name 'd' is not defined
>>> c/=5
>>> c
100.0
>>> x,y = 70, 68
>>> x
70
>>> y
68
>>> unary operators -- minus(-)
SyntaxError: invalid syntax
>>> n = 70
>>> n - -n
140
>>> n = -n
>>> n
-70
>>> 
>>> ---------------------------
SyntaxError: invalid syntax
>>> Relational Operators -- comparing
SyntaxError: invalid syntax
>>> a = 10
>>> b = 20
>>> a<b
True
>>> b<a
False
>>> a>b
False
>>> b>a
True
>>> a==b
False
>>> a = 20
>>> a==b
True
>>> a!=b
False
>>> a <=b
True
>>> a>=b
True
>>> a = 10
>>> a<=
SyntaxError: invalid syntax
>>> a<=b
True
>>> a>=b
False
>>> a!=b
True
>>> ------------------------------
SyntaxError: invalid syntax
>>> logical operators -- and, or, not
SyntaxError: invalid syntax
>>> a= 10
>>> b= 20
>>> c = 30
>>> a<b and a<c
True
>>> b<a and b<c
False
>>> b<a or b<c
True
>>> x = True
>>> not x
False
>>> x = not x
>>> x
False
>>> 