# DESAFIO:Criar um sistema bancario com as operacoes: sacar, depositar e visualizar extrato

import os

LIMITE_SAQUES = 3

aux = 0
saldo = 0
limite = 500
extrato = []
numero_saques = 0

menu = '''
***************
(1) Depositar
(2) Sacar
(3) Extrato
(0) Sair
***************
=> '''

while True:
    opcao = input(menu)
 
 #=-=-=-=-=-=-=-=-=-=  Depositar  
    if opcao == '1': 
        aux = float(input('Digite o valor para deposito: '))
        
        if aux <= 0: # - Deve ser possivel depositar somente valores positivos
            os.system('cls')
            print('Valor inválido! Por favor, inserir valor maior que zero.')
        else:
            os.system('cls')
            extrato.append(f'Deposito no valor de:R${aux}')
            saldo += aux
               
#=-=-=-=-=-=-=-=-=-=  Sacar 
    elif opcao == '2': 
        aux = float(input('Digite o valor para saque: '))
        
        if aux <= 0 or aux > 500: # - O limite diario deve ser R$500,00 por saque
            os.system('cls')
            print('''Valor inválido! Seu limmte de valor de saque diario é de:R$500,00'
            Por favor, verificar extrato e inserir valor valido!''')

        elif saldo < aux:         # - Caso usuario sem saldo, exibir msg de aviso sem saldo
            os.system('cls')
            print('''Saque indisponivel! Voce esta sem limite para esse saque.
            Por favor, verificar extrato e inserir valor valido.''')
                  
        elif numero_saques > 3:   # - O siatema deve permitir realizar apenas 3 saques
            os.system('cls')
            print('Saque indisponivel! Voce ja atingiu seu limite de saque diario.')   
            
        else:
            os.system('cls')
            extrato.append(f'Saque no valor de:R${aux}')
            numero_saques +=1
            saldo -=aux
        
#=-=-=-=-=-=-=-=-=-=  Extrato 
    elif opcao == '3':   
        os.system('cls')
        for i in extrato:              # - Deve listar todos os depositos e saques
            print(i,'\n',10*'_') 
        
        print(f"Saldo atual:R${saldo}") # - No fim da listagem exibir saldo atual. Exibir formato R$ xxx.xxS
        print(10*'_')
    
#=-=-=-=-=-=-=-=-=-=  Sair
    elif opcao == '0': 
        break   
     
    else:
        os.system('cls')
        print('Operacao inválida! Por favor, selecionar novamente a operação desejada.')