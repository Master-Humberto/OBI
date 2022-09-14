
n = int(input())

lista = []
for i in range(0, n):
	dx = input().split()
	d = int(dx[0])
	x = int(dx[1])
	lista.append([d,x])


cond1 = False
cond2 = False
cond3 = False

if n <= 999 and n % 2 == 1 : 
	cond1 = True
	
if 0 <= d and d <= 4 :
	cond2 = True
	
if 0 <= x and x <= 4 and d != x :
	cond3 = True
	
if cond1 and cond2 and cond3 : 
	xerxes = 0
	dario = 0
	for i in range(0,n):
		x = lista[i][0]
		d = lista[i][1]

		if x == 0 and d == 1 :
			xerxes += 1
		if x == 0 and d == 2 :
			xerxes += 1
		if x == 0 and d == 3 :
			dario += 1
		if x == 0 and d == 4 :
			dario += 1

		if x == 1 and d == 2 :
			xerxes += 1
		if x == 1 and d == 3 :
			xerxes += 1
		if x == 1 and d == 4 : 
			dario += 1
		if x == 1 and d == 0 :
			dario += 1

		if x == 2 and d == 3 :
			xerxes += 1
		if x == 2 and d == 4 :
			xerxes += 1
		if x == 2 and d == 0 :
			dario += 1
		if x == 2 and d == 1 :
			dario += 1

		if x == 3 and d == 4 :
			xerxes += 1
		if x == 3 and d == 0 : 
			xerxes += 1
		if x == 3 and d == 1 :
			dario += 1
		if x == 3 and d == 2 :
			dario += 1

		if x == 4 and d == 0 :
			xerxes += 1
		if x == 4 and d == 1 :
			xerxes += 1
		if x == 4 and d == 2 :
			dario += 1
		if x == 4 and d == 3 :
			dario += 1

	if dario > xerxes :
		print("xerxes")
	else:
		print("dario")
		
		

        