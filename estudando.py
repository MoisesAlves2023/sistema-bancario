from datetime import date
from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        conta._saldo += self.valor
        conta.historico.adicionar_transacao(self)
        return True

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        if conta._saldo >= self.valor:
            conta._saldo -= self.valor
            conta.historico.adicionar_transacao(self)
            return True
        return False

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0.0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo

    def nova_conta(cliente, numero):
        return Conta(cliente, numero)
    
    def sacar(self, valor):
        saque = Saque(valor)
        return saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        return deposito.registrar(self)

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=0.0, limite_saques=0):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


cliente = PessoaFisica("Irineu Silva", "123.456.789-00", date(1990, 5, 15), "Rua A, 123")
conta = ContaCorrente(cliente, 1, limite=1000.0, limite_saques=5)
cliente.adicionar_conta(conta)

cliente.realizar_transacao(conta, Deposito(200.0))
cliente.realizar_transacao(conta, Saque(50.0))

print(f"Saldo atual: R${conta.saldo:.2f}")

for transacao in conta.historico.transacoes:
    if isinstance(transacao, Deposito):
        print(f"Depósito: R${transacao.valor:.2f}")
    elif isinstance(transacao, Saque):
        print(f"Saque: R${transacao.valor:.2f}")
