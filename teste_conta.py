
from conta_bancaria import ContaBancaria

conta1 = ContaBancaria("123", "Ana Lima")
conta2 = ContaBancaria("456", "Carlos Souza")
conta3 = ContaBancaria("789", "Maria Silva")

conta1.depositar(500)
conta2.depositar(300)
conta3.depositar(100)


print("Ana:", conta1.get_saldo())
print("Carlos:", conta2.get_saldo())
print("Maria:", conta3.get_saldo())

conta1.transferir(conta2, 200)
conta2.transferir(conta3, 150)

try:
    conta3.transferir(conta1, 500)
except ValueError as erro:
    print("Erro na transferência:", erro)

try:
    conta1.transferir(conta1, 50)
except ValueError as erro:
    print("Erro na transferência:", erro)


print("Ana:", conta1.get_saldo())
print("Carlos:", conta2.get_saldo())
print("Maria:", conta3.get_saldo())
