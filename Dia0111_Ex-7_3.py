numero1 = 0
numero2 = 0

while True:
    numero1 = int(input('Digite o Número 1: '))
    numero2 = int(input('Digite a Número 2: '))
    
    if numero1  != 0 and numero2 != 0:
            soma = numero1 + numero2
            print(soma)
            print('Continuar somando o Número 1 e o Número 2')
    else:
        print('Digitou 0 para sair')
        break
