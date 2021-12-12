#3) Faça um programa que percorra duas listas e 
# gere uma terceira sem elementos repetidos.

lista1 = []
lista2 = []
lista3 = []
repetidos = []
while True:
    x = int(input("Informe um valor para primeira lista ou 0 para terminar: "))
    if x == 0:
        break
    lista1.append(x)
while True:
    x = int(input("Informe um valor para a segunda lista ou 0 para terminar: "))
    if x == 0:
        break
    lista2.append(x)

for i in lista1:
    for j in lista2:
        if(i==j):
            repetidos.append(i)

concatenando = lista1 + lista2
resultFinal = list(set(concatenando) - set(repetidos))
print(resultFinal)

        
    

