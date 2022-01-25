ndig= 0
soma = 0
num = int(input("digite um numero:"))
while num>(-1):
   ndig+= 1
   soma = soma+num
   num = int(input("digite um numero:"))
media = soma/ndig
print("a media é:",media)
if ndig>0:
   print("a media é:",soma/ndig)
else:
   print("não é possível calcular a média")
    