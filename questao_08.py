#  A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. 
#  Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

T = [ -10, -8, 0, 1, 2, 5, -2, -4]

menor = min(T)
maior = max(T)
media = 0

for i in T:
    media += i

media = media/len(T)

print(f""" 
A menor temperatura é {menor}
A maior temperatura é {maior}
A média das temperaturas é {media}
      """)