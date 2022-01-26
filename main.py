soma = 0 # QUESTÃO 1
for num in range(1000):
  if(num%3==0) or (num%5==0):
    soma+=num
  print(soma)