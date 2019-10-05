#!-*- conding: utf8 -*-

from random import randint

n = randint(1,1000)

palpite = 0

tentativa = 0

while palpite != n:
	palpite = int(input('digite seu palpite de 1 a 1000: '))
	tentativa+=1
	if n == palpite:
		print('Parabens voce acertou. Seu numero de tentativas foi',tentativa)
		break	
	elif palpite < n:
		print('Voce errou. Digite um valor maior')
	else:
		print('Voce errou. Digite um valor menor')
print()
print('='*25)
print('FIM DO JOGO')
print('='*25)
