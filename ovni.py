n = int(input())

d = int(input())

a = int(input())

cond1 = False
cond2 = False
cond3 = False

if 3 <= n and n <= 100 :
	cond1 = True
	
if 1 <= d and d <= n :
	cond2 = True

if 1 <= a and a <= n :
	cond3 = True
	
	
if cond1 and cond2 and cond3 : 
	apertos = 0
	posicao = a
	while d != posicao :
		posicao += 1
		apertos += 1
		if posicao == (n+1):
			posicao = 1
     
	print(apertos)