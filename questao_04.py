# Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. Exemplo:

# (()) OK
# ()()(()()) OK
# ()) Erro
expressao = input("Informe a expressão: ")
pilha = list(expressao)

aberto = 0
fechado = 0


while len(pilha) > 0:
    if len(pilha) > 0:
        if pilha.pop() == ')':
            fechado += 1
        else:
            aberto += 1

    
if aberto != fechado:
    print(expressao + "Erro")
else:
    print(expressao + "OK")

  
