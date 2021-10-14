import array

symbols = 'abcdef'

res = tuple(ord(s) for s in symbols)

print(res)

arr = array.array('I', res)

print(arr[0])