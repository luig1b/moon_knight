velocidade = int(input("velocidade atingida: "))
tempo = int(input("quanto tempo você dirigiu: "))

velo1 = velocidade
velo2 = tempo
    
if velocidade <= 145 and tempo <= 24:
 result = (velo1*velo2)
            
print("km", result)

else:
print("não foi possivel calcular")
