numero1=float(input('primeiro número: '))
numero2=float(input('segundo número: '))
print('1-soma')
print('2-subtração')
print('3-multiplicação')
print('4-divisao')

opção =int(input('escolha uma opção : '))
if opção == 1:
    resultado= numero1 + numero2    
    print(f'a soma de {numero1} e {numero2} é {resultado}')
elif opção == 2:    
    resultado = numero1 - numero2   
    print(f'a subtração de {numero1} e {numero2} é {resultado}')
elif opção == 3: 
    resultado= numero1 * numero2
    print(f'a multiplicação de {numero1} e {numero2} é {resultado}') 
elif opção == 4: 
    if numero2 !=0:
        resultado = numero1 / numero2
        print(f'a divisão de {numero1} e {numero2} é {resultado}')
    else:   
        print('ERRO: não é possivel fazer divisao por ZERO')
else:
    print('Opção invalida')