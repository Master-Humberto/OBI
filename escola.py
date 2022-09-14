l = int(input())
c = int(input())

cond1 = False
cond2 = False

if 1 <= l and l <= 100 :
	cond1 = True
	
if 1 <= c and c <= 100 :
	cond2 = True
	
if cond1 and cond2: 
	a = 0
	a += 2 * (l-1)
	a += 2 * (c-1)
	b = 0 
	b += c*l
	b += (c-1)*(l-1)
	print(a)
	print(b)
	
