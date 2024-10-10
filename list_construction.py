import timeit
from timeit import Timer

# Concatenate
def list_construction_concat():
    l = []
    for i in range(1000):
        l = l + [i]
# Append
def list_construction_for():
    l = []
    for i in range(1000):
        l.append(i)

# List Comprehension
def list_construction_comprehension():
    l = [n for n in range(1000)]

# List Constructor
def list_construction_list():
    l = list(range(1000))


test_1 = Timer('list_construction_concat()', 'from __main__ import list_construction_concat')
print("concat ",test_1.timeit(number=1000), "milliseconds")
test_2 = Timer('list_construction_for()', 'from __main__ import list_construction_for')
print("append ",test_2.timeit(number=1000), "milliseconds")
test_3 = Timer('list_construction_comprehension()', 'from __main__ import list_construction_comprehension')
print("list comprehension ",test_3.timeit(number=1000), "milliseconds")
test_4 = Timer('list_construction_list()', 'from __main__ import list_construction_list')
print("list range ",test_4.timeit(number=1000), "milliseconds")


