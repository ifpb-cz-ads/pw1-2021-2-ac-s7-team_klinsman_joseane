#9) Escreva um programa que lê uma string com uma palavra ou frase, 
# e que gera um dicionário onde cada chave seja um caractere, e seu 
# valor seja a quantidade de vezes que o caractere aparece na frase. 
# Você deve ignorar os espaços em branco.
#Exemplo: "programacao" -> {"p": 1, "r": 2, "o": 2, "g": 1, "a": 2, "m": 1, "c": 1}

palavra = input("Digite um palavra ou frase: ")
lista = list(palavra.replace(" ", ""))
dicionario = {}
count = 0
for i in lista:
    for j in lista:
        if(i==j):
            count += 1
    
    if(i not in dicionario):
        dicionario[i] = count
    count = 0
print(palavra, " -> ", dicionario)
        
