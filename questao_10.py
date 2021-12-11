# Altere o programa abaixo de forma a solicitar ao usuário o produto e a quantidade vendida. 
# Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque.

# estoque={ "tomate": [ 1000, 2.30], "alface": [ 500, 0.45], "batata": [ 2001, 1.20], "feijão": [ 100, 1.50] }
# venda = [ ["tomate", 5], ["batata", 10], ["alface",5] ]
# total = 0
# print("Vendas:\n")

# for operação in venda:
# 	produto, quantidade = operação
# 	preço = estoque[produto][1]
# 	custo = preço * quantidade
# 	print("%12s: %3d x %6.2f = %6.2f" %
# (produto, quantidade,preço,custo))	 
# 	estoque[produto][0] -= quantidade
# 	total+=custo
    
# print(" Custo total: %21.2f\n" % total)
# print("Estoque:\n")

# for chave, dados in estoque.items():
# 	print("Descrição: ", chave)
# 	print("Quantidade: ", dados[0])
# 	print("Preço: %6.2f\n" % dados[1])


estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45],
           "batata": [2001, 1.20], "feijão": [100, 1.50]}
venda = []
total = 0

while True:
    produto = input("informe o nome do produto, informe x para encerrar: ")
    if produto == 'x':
        break
    quantidade = int(input("Informe a quantidade: "))

    if produto in estoque and estoque[produto][0] > quantidade:
        venda.append([produto, quantidade])
        estoque[produto][0] -= quantidade
    else:
        print("Produto não existe ou está fora de estoque :(")

print("Vendas:\n")
for operação in venda:
    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
          (produto, quantidade, preço, custo))
    estoque[produto][0] -= quantidade
    total += custo

print(" Custo total: %21.2f\n" % total)

print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])
