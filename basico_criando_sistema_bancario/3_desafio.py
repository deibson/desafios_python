import textwrap
from abc import ABC
from datetime import datetime
import random

LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ''
numero_saques = 0

list_clientes = []
list_contas = []
list_transacoes = []

class PessoaFisica():
    def __init__(self, nome, data_nascimento, cpf, endereco):        
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        

class Cliente(PessoaFisica):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, data_nascimento, cpf, endereco)
        self.contas = []

    @staticmethod
    def selecionar_cliente(cpf):
        for cliente in list_clientes:
            if cliente.cpf == cpf: return cliente
        return None 

    def save(self):
        try:
            list_clientes.append(self)
            return True
        except :
            print(f'[ ERROR ] : Não foi possivel gravar os dados o cliente : {self.cpf}')
        return None
    
    def adicionar_conta(self, conta):
        for i in range(len(list_clientes)):
            if list_clientes[i] == self:
                list_clientes[i].contas.append(conta)
                return self.selecionar_cliente(self.cpf)
    

class Conta:
    def __init__(self, agencia, numero, cliente):        
        self.agencia = agencia
        self.numero = numero    
        self.cliente = cliente
        self.saldo = 0

    @staticmethod
    def selecionar_conta(agencia, numero, cliente):
        for conta in list_contas:
            if conta.get('agencia') == agencia and conta.get('numero') == numero and conta.get('cliente') == cliente: 
                return conta
        return None 
    
    def atualizar_saldo(self, valor):
        try:
            for i in range(len(list_contas)):
                if list_contas[i] == self:
                    list_contas[i].saldo += valor
                    return self.selecionar_conta(self.agencia, self.numero, self.cliente)
        except:
            print(f'[ ERROR ] : Não foi possivel Atualizar o saldo da conta : {self.numero}')
        return None
    

    @staticmethod
    def listar_contas(cliente):
        contas=[]
        for conta in list_contas:
            if cliente in conta:
                contas.append(conta)
        return contas


class Transacao:
    def __init__(self, data, tipo, cliente, conta, transacao, saldo_atual, saldo_final):
        self.data = data
        self.tipo = tipo
        self.cliente = cliente
        self.conta = conta
        self.transacao = transacao
        self.saldo_atual = saldo_atual
        self.saldo_final = saldo_final

    def save(self):
        list_transacoes.append(self)

    def adicionar_transacao(self):
        list_transacoes.append(self)


def show_extrato():
    print(f"""
        ---------------- EXTRATO ----------------
        {'Não foram realizadas movimentações.' if not extrato else extrato}

        Saldo: R$ {saldo:.2f}
        -----------------------------------------
    """)

def listar_contas():
    print("\n------------- LISTAR CONTAS -------------\n")
    cpf = input("Informe o CPF (somente número): ")
    cliente = buscar_cliente(cpf)
    if cliente:
        contas = Conta.listar_contas(cliente.cpf)
        print(cliente.cpf, textwrap.dedent(str(contas)))
    else:
        print('[ATENÇÃO] Cliente não existe')


def buscar_conta(agencia, conta, cliente):
    conta = Conta.selecionar_conta(agencia, conta, cliente)
    if conta:
        return conta
    print("\nConta não encontrado.\n")
    return None


def buscar_cliente(cpf):
    cliente = Cliente.selecionar_cliente(cpf=cpf)
    if cliente:
        return cliente
    print("\nCliente não encontrado.\n")
    return None


def depositar():
    print("\n---------------- DEPOSITO ----------------\n")
    cpf = input("Informe o CPF (somente número): ")    
    
    cliente = buscar_cliente(cpf)
    if cliente:
        agencia = input("Agencia : ")
        conta = input("Conta : ")
        dados_conta = buscar_conta(agencia,conta,cliente.get('cpf'))
        
        valor = float(input("Valor de depósito: ")) if dados_conta else 0
        if valor > 0:   
            saldo_atual = dados_conta.saldo
            dados_conta.atualizar_saldo(valor)  

            operacao = {
                'data': datetime.now().strftime("%x %X"),
                'tipo': 'Deposito',
                'cliente': cliente.cpf,
                'agencia': dados_conta.agencia,
                'conta': dados_conta.conta,
                'saldo_atual': saldo_atual,
                'saldo_final': dados_conta.saldo
            }
            transacao = Transacao(**operacao)
            transacao.save()

            print(f"\nDepósito efetuado com sucesso: R$ {valor:.2f}\n{'-'*43}")

    else:
        print(f"\nOperação falhou!\nO valor informado é inválido.\n{'-'*43}""")


def sacar():
    print("\n---------------- SAQUE ----------------\n")
    cpf = input("Informe o CPF (somente número): ")    
    
    cliente = buscar_cliente(cpf)
    if cliente:
        agencia = input("Agencia : ")
        conta = input("Conta : ")
        dados_conta = buscar_conta(agencia,conta,cliente.get('cpf'))
        
        valor = float(input("Valor de depósito: ")) if dados_conta else 0
        if valor > 0:   
            saldo_atual = dados_conta.saldo
            dados_conta.atualizar_saldo(-valor)  

            operacao = {
                'data': datetime.now().strftime("%x %X"),
                'tipo': 'Deposito',
                'cliente': cliente.cpf,
                'agencia': dados_conta.agencia,
                'conta': dados_conta.conta,
                'saldo_atual': saldo_atual,
                'saldo_final': dados_conta.saldo
            }
            transacao = Transacao(**operacao)
            transacao.save()

            print(f"\nSaque efetuado com sucesso: R$ {valor:.2f}\n{'-'*43}")

    else:
        print(f"\nOperação falhou!\nO valor informado é inválido.\n{'-'*43}""")


def criar_conta(cpf=None):
    print("\n------------ Cadastrar Conta -------------\n")

    if not cpf:
        cpf = input("Informe o CPF (somente número) : ")
    
    cliente = buscar_cliente(cpf)       
    if cliente:
        new_conta = Conta(agencia=AGENCIA, numero=random.randrange(10000,99999,1), cliente=cliente.cpf)
        cliente.adicionar_conta(new_conta)
        print(f'Agência : {new_conta.agencia} - Conta : {new_conta.numero}')
        print(f"\n[SUCCESS] Conta cadastrada com sucesso!\n{'-'*43}")
    else:
        print(f"\n[ERROR] No cadastro de contas\n{'-'*43}")


def cadastrar_cliente():
    print("\n------------ Cadastrar Usuário -------------\n")
    cpf = input("Informe o CPF (somente número): ")
    
    cliente = buscar_cliente(cpf)
    if cliente:
        print(f'''
            Cliente : {cliente.Nome} 
            CPF : {cliente.cpf} 
            Data de Nascimento : {cliente.data_nascimento} 
            Endereco : {cliente.endereco} 
            Contas : {cliente.contas} 
        ''')

        op = input('Deseja adicionar Nova Conta 1-Sim ou 0-Não : ')
        if op in ['1', 'Sim', 'sim', 'SIM']:
            criar_conta(cliente.cpf)
    else:
        nome = input("Nome completo: ")
        data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        novo_cliente = Cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        
        if novo_cliente.save(): 
            print(f'\nCliente {cpf} cadastrado com sucesso.\n') 
            
            op = input('Deseja adicionar Nova Conta 1-Sim ou 0-Não : ')
            if op in ['1', 'Sim', 'sim', 'SIM']:
                criar_conta(novo_cliente.cpf)
                               
        else:
            print('Houve algum problema ao tentar cadastrar o cliente {cpf} \nVerfique e tente novamente.')


def menu():
    return input(f"""      
    ================== Dados da Conta ======================
                                                          
     Saldo:{saldo:.2f}\t\tLimite:{limite:.2f}\t\tN.Saques:{numero_saques}/{LIMITE_SAQUES}   
                                                          
    |*********************** MENU *************************|
    |                                                      |
    | [d]-Depositar   [s]-Sacar   [e]-Extrato   [q]-Sair   |
    |                                                      |
    | [cc]-Nova Conta  [lc]-listar contas [cc]-Novo Cliente|
    |                                                      |
    ========================================================   
    Opção Selecionada: """)


def main():  
    while True:        
        opcao = menu()
        if opcao in "dD":
            depositar()

        elif opcao in "sS":
            sacar()

        elif opcao in "eE":
            show_extrato()

        elif opcao == "cc" or opcao == 'CC':
            cadastrar_cliente()

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
