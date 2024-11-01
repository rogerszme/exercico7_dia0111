
usuario =''
senha = ''
while usuario != 'admin' or senha != '123':
    usuario = input('Digite o usuario: ')
    senha = input('Digite a senha: ')
    if usuario != 'admin' or senha != '123':
        print(' ESTÁ ERRADO !!! ')
print(' ESTÁ CORRETO !!! ')