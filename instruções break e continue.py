while True:
    print('Para encerrar digite sair\n')
    cidade= input('Digite uma cidade: ')
    print("")
    if cidade == 'continuar':
        continue #para apenas este laço e volta do início, sem executar as intruções abaixo.
    elif cidade == 'sair':
        break  #se for verdadeiro o break tirará o laço de repetição e não executará mais nada.
    else:
        print('A cidade digitada foi:',cidade)

print('\n ESTAMOS ENCERRANDO O PROGRAMA...')