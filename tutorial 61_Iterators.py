# Iterators

lst = [1,2,3,4,5,6]

it = iter(lst)

print(next(it))
print(next(it))# this is one way of printing next value

print(it.__next__())
print(it.__next__())#this is another way of printing next value


# create iterators to print first 10 numbers

class lst_Ten:
    def __init__(self):
        self.A = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.A<10:
            value = self.A
            self.A += 1
            return value

        else:
            raise StopIteration



a1 = lst_Ten()

#print(a1.__next__())

for i in a1:
    print(i)




# Practice - lst_1 = list(range(50))
lst_1 = list(range(50))
print(lst_1)

class lst_Ten:
    def __init__(self):
        self.A = lst_1[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self. A <45:
            value = self.A
            self.A += 1
            return value

        else:
            raise StopIteration



a1 = lst_Ten()

# print(a1.__next__())

for i in a1:
    print(i)