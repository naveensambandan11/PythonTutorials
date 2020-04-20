# Generators  -- inbuild function for iterators without calling --init-- and --next--

def Func_1():

    yield 10  # 'yield' should be given instead of 'return'. if yield is mentioned, then function becomes generator
    yield 20  # 'return' terminates the function whereas 'yield' continues to execute
    yield 30

a1 = Func_1()

print(a1.__next__())
print(next(a1))


#practice

def Func_2():
    for i in range(10):
        yield (i)


b1 = Func_2()

print(b1.__next__())
print(b1.__next__())
print(b1.__next__())
print(b1.__next__())

for i in b1:
    print(i)
