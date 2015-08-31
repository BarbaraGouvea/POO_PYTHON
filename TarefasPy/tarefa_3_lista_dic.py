lista=enumerate('zero um dois tres quatro cinco seis sete oito nove dez'.split())
numero_string=dict(lista)
string_numero={valor:chave for chave, valor in numero_string.items()}
print (numero_string)


def para_numeral (n):
    numeros=''
    for digito in  str(n):
        
        numeros+=numero_string[int (digito)]
        numeros+=', '
    return numeros[0:-2]

assert 'um'==para_numeral(1)
assert 'um, dois'==para_numeral(12)
assert 'um, um'==para_numeral(11)


def para_inteiros (string_n):
    str2=''
    lista=string_n.split(', ')
    for digito2 in lista:
        str2+= str (string_numero[digito2])
    return int (str2)

assert 1==para_inteiros('um')
assert 12==para_inteiros('um, dois')
assert 123==para_inteiros('um, dois, tres')

