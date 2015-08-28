'''
Created on 25 de ago de 2015

@author: Barbara
'''
from _ast import Del

class Pessoa():
    OLHOS=2
    def cumprimentar(self):
        return "Olá meu nome é %s" %self.nome
    
    
    def __init__(self,nome):
        self.nome=nome
        
pessoa=Pessoa('Babi')
barbara=Pessoa('BarbaraGouvea')

print(pessoa.nome)
print(barbara.nome)
print(barbara.cumprimentar())
print(pessoa.cumprimentar())
barbara.OLHOS=3
Pessoa.OLHOS=4
print(Pessoa.OLHOS)
print(pessoa.OLHOS)
print(barbara.OLHOS)

del barbara.OLHOS
print(barbara.OLHOS)


        
        
    