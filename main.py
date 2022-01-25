#elementos = (input("Digite a quantidade de elementos:"))
l = [1]
print(l)
for lin in range(2,10+1):
#for lin in range(2,elementos+1):
  l2 = []
  for i in range(0,len(l)-1):
    l2.append(l[i] + l[i+1])
  l2 = [1] + l2 + [1]
  print(l2)
  l = l2
  
  
