class Mulher (Pessoa):
    def __init__(self, nome):
        print('Iniciando __init___ de mulher')
        super().__init__(nome)
        print('Finalizando __init__ de Mulher')

mulher = Mulher('Barbara')

print (mulher.cumprimentar())
print (isinstance(mulher, Mulher))
print (isinstance(mulher, Pessoa))
print (isinstance(mulher,object))
    
    class Homem (Pessoa):
        def cumprimentar (self):
            return super().cumprimentar()+'Aperto de mão'
        
    
    homem=Homem ('Liu')
    print(homem.cumprimentar())
    
    class Hermafrodita (Homem, Mulher):
        def cumprimentar(self):
            return Homem.cumprimentar(self)
    
hermafrodita=Hermafrodita('Não é nenhum aluno')
print(hermafrodita.cumprimentar())
print(isinstance(hermafrodita, Mulher))
print(isinstance(hermafrodita.Homem())

    