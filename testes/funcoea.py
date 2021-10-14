def func(*args):
    print(args)

def fun2(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}').format(key, value)

func(1,2,3)
arg = {'nome':'David'}
fun2(**arg)
fun2(nome="David")