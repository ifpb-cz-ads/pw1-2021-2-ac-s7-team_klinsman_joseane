#7) Modifique o programa anterior de forma a pesquisar p e v em toda a lista
# e informando o usuário a posição onde p e a posição onde v foram encontrados.

L = [15, 7, 27, 39]
p = int(input("Digite o valor P a procurar: "))
v = int(input("Digite o valor V a procurar: "))
checkP = 0
checkV = 0
for x in range(len(L)):
    if L[x] == p:
        print("%d achado na posição %d" % (p, x))
        checkP += 1
    if L[x] == v:
        print("%d achado na posição %d" % (v, x))
        checkV += 1
    x += 1
if(checkP == 0):
    print("%d não foi encontrado!" % p)
elif(checkV == 0):
    print("%d não foi encontrado!" % v)
