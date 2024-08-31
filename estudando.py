usuarios = []
contas = []

def exibir_menu():
    menu = '''
            Qual operação deseja realizar?
            1 - Cadastrar Cliente
            2 - Criar conta
            3 - Listar contas
            4 - Exibir extrato
            5 - Depositar
            6 - Sacar
            7 - Transferir
            8 - Sair

            *Digite o número da operação que deseja realizar:
            '''
    print(menu)

def cadastrar_cliente():
    nome_cliente = input("Insira seu nome: ").upper().strip()
    cpf_cliente = int(input("Insira seu CPF: "))
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf_cliente:
            print("CPF já cadastrado")
            return
        
    data_nascimento_cliente = input("Digite sua data de nascimento: ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    estado = input("Estado: ")
    
    cliente = {
        'nome': nome_cliente,
        'cpf': cpf_cliente,
        'data_nascimento': data_nascimento_cliente,
        'endereco': {
            'logradouro': logradouro,
            'numero': numero,
            'bairro': bairro,
            'estado': estado
        }
    }
    usuarios.append(cliente)
    print("Cliente cadastrado com sucesso!")

def criar_conta():
    cpf_cliente = int(input("Insira seu CPF: "))
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf_cliente:
            conta_cliente = {
                'agencia': '0001',
                'numero_conta': len(contas) + 1,
                'usuario': usuario['nome'],
                'cpf': cpf_cliente,
                'saldo': 0.0
            }
            contas.append(conta_cliente)
            print(f"Conta criada com sucesso para {usuario['nome']}")
            return
    
    print("CPF não encontrado na base de clientes. Crie um cliente antes de criar uma conta.")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(conta)

def depositar(cpf_cliente, numero_conta, valor, /):
    for conta in contas:
        if conta['cpf'] == cpf_cliente and conta['numero_conta'] == numero_conta:
            conta['saldo'] += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso na conta {numero_conta} de {conta['usuario']}. Saldo atual: R${conta['saldo']:.2f}")
            return
    
    print("Conta não encontrada.")

def exibir_extrato(cpf_cliente, numero_conta):
    for conta in contas:
        if conta['cpf'] == cpf_cliente and conta['numero_conta'] == numero_conta:
            print(f"Extrato da conta {numero_conta} de {conta['usuario']}: Saldo: R${conta['saldo']:.2f}")
            return
    
    print("Conta não encontrada.")

# Função principal
opcao = 0
while opcao != 8:
    exibir_menu()
    opcao = int(input("Número: "))
    
    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        criar_conta()
    elif opcao == 3:
        listar_contas()
    elif opcao == 4:
        cpf = int(input("Insira o CPF: "))
        numero_conta = int(input("Insira o número da conta: "))
        exibir_extrato(cpf, numero_conta)
    elif opcao == 5:
        cpf = int(input("Insira o CPF: "))
        numero_conta = int(input("Insira o número da conta: "))
        valor = float(input("Insira o valor do depósito: "))
        depositar(cpf, numero_conta, valor)
    elif opcao == 6:
        print("Função de saque ainda não implementada.")
    elif opcao == 7:
        print("Função de transferência ainda não implementada.")
    elif opcao == 8:
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente.")
