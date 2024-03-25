class Cliente:
    def __init__(self):
        self.nome = None
        self.email = None
        self.telefone = None
        self._cupom_desconto = 0

    def get_cupom_desconto(self):
        return self._cupom_desconto

    def realizar_compras(self, lista_itens):
        pass

class ClienteVipPF(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.2

    def realizar_compras(self, lista_itens):
        return f"Quantidade total de itens comprados = {len(lista_itens)}"

class ClientePF(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.05

    def realizar_compras(self, lista_itens):
        if len(lista_itens) <= 20:
            return f"Quantidade total de itens comprados = {len(lista_itens)}"
        else:
            return "Quantidade de itens superior ao limite permitido."

class ClientePJ(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.1

    def realizar_compras(self, lista_itens):
        if len(lista_itens) <= 50:
            return f"Quantidade total de itens comprados = {len(lista_itens)}"
        else:
            return "Quantidade de itens superior ao limite permitido."

# Validação de dados
def validar_nome(nome):
    if not nome or len(nome) < 3:
        raise ValueError("Nome inválido.")

def validar_email(email):
    if not email or "@" not in email:
        raise ValueError("Email inválido.")

def validar_itens(lista_itens):
    for item in lista_itens:
        if not item or not item.get("nome") or not item.get("preco"):
            raise ValueError("Item inválido.")
        
# Verificando compra
def calcular_valor_total(lista_itens, cupom_desconto):
    valor_total = sum(item.get("preco") for item in lista_itens)
    valor_total *= (1 - cupom_desconto)
    return valor_total

# def realizar_compras(self, lista_itens, limite_itens):
#     validar_itens(lista_itens)
#     if len(lista_itens) > limite_itens:
#         return "Quantidade de itens superior ao limite permitido."
#     valor_total = calcular_valor_total(lista_itens, self._cupom_desconto)
#     # Implementar métodos de pagamento
#     return f"Compra realizada com sucesso! Valor total: R${valor_total:.2f}"

# Exemplo de uso
cliente_vip = ClienteVipPF()
cliente_vip.nome = "Maria"

itens_cliente_vip = [
    {"nome": "Produto 1", "preco": 10.0},
    {"nome": "Produto 2", "preco": 20.0},
]

valor_total = calcular_valor_total(itens_cliente_vip, cliente_vip.get_cupom_desconto())

print(f"\n{'-'*20} Cliente VIP {'-'*20}")
print(f"Cliente: {cliente_vip.nome}")
print(f"Cupom de desconto: {cliente_vip.get_cupom_desconto():.2%}")
print(f"\nLista de compras:")

for item in itens_cliente_vip:
    print(f"- {item['nome']}: R${item['preco']:.2f}")

print(f"\nSubtotal: R${sum(item['preco'] for item in itens_cliente_vip):.2f}")
print(f"Desconto: R${valor_total * cliente_vip.get_cupom_desconto():.2f}")
print(f"\nValor total: R${valor_total:.2f}")
print('-' * 52)

cliente_pf = ClientePF()
cliente_pf.nome = "Mateus"

itens_ClientePF = [
    {"nome": "Produto 3", "preco": 15.0},
    {"nome": "Produto 4", "preco": 25.0},
    {"nome": "Produto 5", "preco": 30.0},
]

valor_total = calcular_valor_total(itens_ClientePF, cliente_pf.get_cupom_desconto())

print(f"\n{'-'*20} Cliente PF {'-'*20}")
print(f"Cliente: {cliente_pf.nome}")
print(f"Cupom de desconto: {cliente_pf.get_cupom_desconto():.2%}")
print(f"\nLista de compras:")

for item in itens_ClientePF:
    print(f"- {item['nome']}: R${item['preco']:.2f}")

print(f"\nSubtotal: R${sum(item['preco'] for item in itens_ClientePF):.2f}")
print(f"Desconto: R${valor_total * cliente_pf.get_cupom_desconto():.2f}")
print(f"\nValor total: R${valor_total:.2f}")
print('-' * 52)


cliente_pj = ClientePJ()
cliente_pj.nome = "Empresa X"

itens_cliente_pj = [
    {"nome": "Produto 6", "preco": 40.0},
    {"nome": "Produto 7", "preco": 50.0},
    {"nome": "Produto 8", "preco": 60.0},
    {"nome": "Produto 9", "preco": 70.0},
    {"nome": "Produto 10", "preco": 80.0},
]

valor_total = calcular_valor_total(itens_cliente_pj, cliente_pj.get_cupom_desconto())

print(f"\n{'-'*20} Cliente PJ {'-'*20}")
print(f"Cliente: {cliente_pj.nome}")
print(f"Cupom de desconto: {cliente_pj.get_cupom_desconto():.2%}")
print(f"\nLista de compras:")

for item in itens_cliente_pj:
    print(f"- {item['nome']}: R${item['preco']:.2f}")

print(f"\nSubtotal: R${sum(item['preco'] for item in itens_cliente_pj):.2f}")
print(f"Desconto: R${valor_total * cliente_pj.get_cupom_desconto():.2f}")
print(f"\nValor total: R${valor_total:.2f}")
print('-' * 52)
