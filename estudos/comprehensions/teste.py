import array
symbols = "askds"

codes = [ord(r) for r in symbols]

colors = ['black', 'white']
sizes = ['S','M', 'L']
tshirts = [(color,size) for color in colors
                        for size in sizes]

# print(tshirts)
# 
symbols = "çxlkj"

res_tuple = tuple(ord(symbol) for symbol in symbols)

res_array = array.array('I',(ord(symbol) for symbol in symbols))

print(res_array)

