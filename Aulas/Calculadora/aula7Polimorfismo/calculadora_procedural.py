def calcular():
    argumento_1 = float(input('Digite um n�mero: '))
    sinal = input('Digite o sinal da oper��o: ')
    argumento_2 = float(input('Digite outro n�mero: '))
    if sinal == '+':
        return argumento_1+argumento_2
    elif sinal == '-':
        return argumento_1-argumento_2
    else:
        raise Exception('Opera��o n�o implementada')

if __name__=='__main__':
    print(calcular())
        