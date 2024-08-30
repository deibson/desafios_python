import random
from datetime import datetime

LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
usuarios = []
contas = []


def menu():
    return input(f"""      
    ================== Dados da Conta ======================
                                                          
     Saldo:{saldo:.2f}\t\tLimite:{limite:.2f}\t\tN.Saques:{numero_saques}/{LIMITE_SAQUES}   
                                                          
    |*********************** MENU *************************|
    |                                                      |
    | [d]-Depositar   [s]-Sacar   [e]-Extrato   [q]-Sair   |
    |                                                      |
    | [nc]-Nova Conta  [lc]-listar contas [nu]-Novo Usuario|
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
        extrato += f'\tDeposito:\t{datetime.now().strftime("%x %X")}\t\tValor: R$ {valor:.2f}\n'

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
        extrato += f"\tSaque:\t{datetime.now()}\t\tValor: R$ {valor:.2f}\n"
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


def filtrar_usuario(cpf):
    global usuarios
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario():
    global usuarios
    cpf = input("""
          
        ------------ Cadastrar Usuário -------------
                        
          Informe o CPF (somente número): """)

    if not filtrar_usuario(cpf):
        #nome = input("Informe o nome completo: ")
        #data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        #endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({
            "nome": input("Informe o nome completo: "), 
            "data_nascimento": input("Informe a data de nascimento (dd-mm-aaaa): "), 
            "cpf": cpf, 
            "endereco": input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")})
        
        print(f"\n[SUCCESS] Usuário cadastrado com sucesso!\n{'-'*43}")
    else:
        print(f"\n[ATENÇÂO] Já existe usuário com esse CPF!\n{'-'*43}")


def criar_conta():
    global contas, AGENCIA
    usuario = filtrar_usuario(input("""
          
        ------------ Cadastrar Usuário -------------
                        
          Informe o CPF (somente número): """))

    if usuario:
        contas.append({"agencia": AGENCIA, "numero_conta": random.randrange(10000,99999,1), "usuario": usuario})

        print(f"\n[SUCCESS] Agência cadastrado com sucesso!\n{'-'*43}")
    else:
        print(f"\n[ATENÇÂO] Usuário deve estar cadastrado previamente.\n{'-'*43}")


def listar_contas():
    global contas
    print("\n------------ Lista de Contas -------------")
    if contas:
        for conta in contas:
            print(f"""
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            ------------------------------------------""")
    else:
        print(f"\n[ATENÇÂO] Não existe nenhuma conta cadastrada.\n{'-'*43}")


def main():  

    while True:
        
        opcao = menu()
        if opcao in "dD":
            depositar()

        elif opcao in "sS":
            sacar()

        elif opcao in "eE":
            show_extrato()

        elif opcao == "nu" or opcao == 'NU':
            criar_usuario()

        elif opcao == "nc" or opcao == 'NC':
            criar_conta()

        elif opcao == "lc" or opcao == 'LC':
            listar_contas()

        elif opcao in "qQ":
            break

        else:
            print(f"\n[ATENÇÃO] Operação inválida,\nEscolha uma opção válida no menu.\n{'-'*43}")


if __name__ == "__main__":
    main()
