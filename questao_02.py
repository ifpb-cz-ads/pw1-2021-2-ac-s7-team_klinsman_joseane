# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

lista1 = list()
lista2 = list()
lista3 = list()

for i in range(5):
    lista1.append(int(input("Lista 1 informe um número: ")))
    
for i in range(5):
    lista2.append(int(input("Lista 2 informe um número: ")))
    
lista3 = lista1 + lista2
print(lista3)