# Modifique o programa anterior para pesquisar dois valores. 
# Em vez de apenas p, leia outro valor v que também será procurado. 
# Na impressão, indique qual dos dois valores foi achado primeiro.

L = [15, 7, 27, 39]
p = int(input("Digite o valor P a procurar: "))
v = int(input("Digite o valor V a procurar: "))
primeiro = []


for x in range(len(L)):
    if L[x] == p and len(primeiro) == 0:
        primeiro = [p, x]
        
    elif L[x] == v and len(primeiro) == 0:
        primeiro = [v, x]
if len(primeiro) > 0:
    print("%d foi encontrado primeiro na posição %d" %(primeiro[0], primeiro[1]))

else:
    print("Os valores passados não foram encontrados :(")