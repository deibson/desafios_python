from datetime import datetime

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


def menu():    
    return input(f"""      
    ================== Dados da Conta ======================
                                                          
     Saldo:{saldo:.2f}    Limite:{limite:.2f}    N.Saques:{numero_saques}/{LIMITE_SAQUES}   
                                                          
    ************************ MENU *************************|
    |                                                      |
    | [d]-Depositar   [s]-Sacar   [e]-Extrato   [q]-Sair   |
    |                                                      |
    ========================================================   
    Opção Selecionada: """)


def depositar():
    valor = float(input("""
          
        ---------------- DEPOSITO ----------------
                        
          Informe o valor de depósito: """))
    
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: {datetime.now().strftime("%x %X")}  Valor: R$ {valor:.2f} \n'

        print(f"""\n  
          Depósito efetuado com sucesso: R$ {valor:.2f}
        -------------------------------------------""")

    else:
        print(f"""\n 
        Operação falhou! 
            O valor informado é inválido.        
        -------------------------------------------""")


def sacar():
    valor = float(input("""
          
        ---------------- SAQUE ----------------
                        
          Informe o valor de saque:  """))

    global saldo, extrato, numero_saques
    if valor > saldo:
        print(f"""\n  
        Operação falhou! 
            Você não tem saldo suficiente.
        -------------------------------------------""")

    elif valor > limite:
        print(f"""\n  
        Operação falhou! 
            O valor do saque excede o limite.
        -------------------------------------------""")

    elif numero_saques >= LIMITE_SAQUES:
        print(f"""\n  
        Operação falhou! 
            Número máximo de saques excedido.
        -------------------------------------------""")

    elif valor > 0:        
        saldo -= valor
        extrato += f"Saque: {datetime.now()}  Valor: R$ {valor:.2f} \n"
        numero_saques += 1

        print(f"""\n  
          Saque efetuado com sucesso: R$ {valor:.2f}
        -------------------------------------------""")

    else:
        print(f"""\n 
        Operação falhou! 
            O valor informado é inválido.        
        -------------------------------------------""")


def show_extrato():
    print(f"""
        ---------------- EXTRATO ----------------
        {'Não foram realizadas movimentações.' if not extrato else extrato}
        Saldo: R$ {saldo:.2f}
        -----------------------------------------
    """)


def main():  

    while True:
        
        opcao = menu()
        if opcao in "dD":
            depositar()

        elif opcao in "sS":
            sacar()

        elif opcao in "eE":
            show_extrato()

        elif opcao in "qQ":
            break

        else:
            print(f"""\n 
            Operação inválida, 
                Escolha uma opção válida no menu        
            -------------------------------------------""")


if __name__ == "__main__":
    main()
