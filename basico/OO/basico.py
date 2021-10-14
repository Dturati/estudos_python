import collections

def teste(arg,*args):
    print(arg)
    for arg in args:
        print(arg)

def teste2(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key,value))

teste(1,2,3)
teste2(nome="David", idade=35)

tst = {}
tst.setdefault('Banana',[]).append({'name': 'David'})

print(tst)

index = collections.defaultdict(list)
print(index)
index['Fruta'].append('banana')
print(index)
index['Fruta'].append('Jaca')
print(index)