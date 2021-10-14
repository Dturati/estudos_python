vals = [
    {
        'mes': 1
    },

    {
        'mes': 2
    },

    {
        'mes': 3
    }
]

print(vals)

res = [r for r in vals if r['mes'] == 1]

print(res)