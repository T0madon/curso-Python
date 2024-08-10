import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

lista = [ n for n in range(10000)]
generator = (n for n in range(10000))

print(generator)

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))