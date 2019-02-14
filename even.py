jas=input()
if jas.isnumeric():
	g=int(jas)
	if g%2==0:
		print("Even")
	else:
		print("Odd")
else:
	print("invalid")
