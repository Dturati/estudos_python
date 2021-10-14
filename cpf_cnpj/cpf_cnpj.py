cpf = "01753491185"
cnpj = '21312312312222'

if len(cpf) == 11:
    new_cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]


print(cnpj)
new_cnpj = cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:]

print(new_cnpj)