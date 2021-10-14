from array import array
from random import random

floats = array('d', (random() for i in range(1,10)))

# print(floats)
# print(floats[-1])
DIAL_CODES = [(86,'China'),(91, 'India'),(1, 'USA')]

res = {s: r for r, s in DIAL_CODES}


print(res.get('China', 0))


