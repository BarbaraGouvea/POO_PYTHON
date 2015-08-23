lista=['Renzo','Igor','Igor']
lista.append('Liu')
print(lista)
lista.pop(0)
print(lista)

lista2=[n+'s' for n in lista if n!='Igor']
print(lista2)

lista3=['Celso', 'Thalita']
lista3.extend(lista)
#lista2=[n+'s' for n in lista]
#print(lista3+lista) //elas não foram alteradas no mais igual não altera
# sorted cria uma nova e ordena essa nova com os dados da outra
#o .sort altera a propria lista
print (lista3)
print(lista)




'''lista2=[]
for n in lista:
    lista2.append(n+'s')
print(lista)

'''

'''
Created on 19 de ago de 2015

@author: Barbara
'''
