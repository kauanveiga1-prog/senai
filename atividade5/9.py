maior = float()
manor = float()
soma  = 0
acima_100 = 0
for cont in range(10):
    temperatura = float (input(f"digite a {cont }temperatura:"))
    soma += temperatura
    if cont == 1:
       maior = temperatura
       menor = temperatura
    if temperatura > maior:
        maior = temperatura
        if temperatura > menor:
        menor = temperatura
         if temperatura> 100:
          acima_100 += 1
media = soma/cont 
        