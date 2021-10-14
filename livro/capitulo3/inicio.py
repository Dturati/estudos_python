a = dict(one=1, two=2, three=3)
b = {'one':1,'two':2, 'three':3}

# print(a,b)

res = b.setdefault('vazio', [])

print(res)
print(b)