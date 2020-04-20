#multiply two matrix w/o in build function

from numpy import *

a=array([[2,3],[4,5]])

b=array([[2,4,3],[8,4,2]])
c=zeros(len(a)*len(b[0]),int)
c=c.reshape(len(a),len(b[0]))
i=0
k=0

while i<len(a):

    for j in range(len(b)):
        c[i][k]=c[i][k]+(b[j][k]*a[i][j])


    k=k+1


    if k==len(b[0]):
        i=i+1
        k=0

print(c)