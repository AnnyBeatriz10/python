palavra = "chinelo"
palavra2 = "_" * len(palavra)
tentativas = 0
digitados = ""
chance = 0
while palavra2 != palavra:
	letra = input("informe uma letra:")
	digitados +=letra
	pos = palavra.find(letra)
	while pos != -1:
		palavra2 = palavra2[0:pos] + letra + palavra2[pos + 1:]
		pos = palavra.find(letra, pos + 1)
		print(palavra2)
		tentativas += 1
if palavra2==len(palavra):
  print("ops!,você tem mais uma chance")
  if palavra2!=palavra:
    chance = input("digite a palavra",palavra2)

