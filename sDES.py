#Sandra García Racilla
#Criptografía
#DES Simplificado (sDES)
op=input()
key=input()
plainT=input()

perM=[1,5,2,0,3,7,4,6]
perC=[3,0,2,4,6,1,7,5]
perK1=[0,6,8,3,7,2,9,5]
perK2=[7,2,5,4,9,1,8,0]
perExp=[3,0,1,2,1,2,3,0]
perX=[1,3,2,0]
perSwap=[4,5,6,7,0,1,2,3]

s0=[[1,0,3,2],
	[3,2,1,0],
	[0,2,1,3],
	[3,1,3,2]];

s1=[[0,1,2,3],
	[2,0,1,3],
	[3,0,1,0],
	[2,1,0,3]];

def permutacion(A,per):
	aux=[]
	for indice in per:
		aux.append(int(A[indice]))
	return aux
#Busca valor en la tabla S0/S1 y lo regresa como binario
def busquedaSx(XOR,Sx,inc):
	row=int(str(XOR[0+inc])+str(XOR[3+inc]),2)
	col=int(str(XOR[1+inc])+str(XOR[2+inc]),2)
	if Sx[row][col]<2:	
		return '0'+'{0:b}'.format(Sx[row][col])
	else:
		return '{0:b}'.format(Sx[row][col])

def feistelPer(lista,Kx):
	L=[]
	R=[]
	XOR=[]
	XOR2=[]
	global s0, s1, perX
	n=len(lista)//2
	#Se obtienen las dos partes, cada una de 4 bits
	for i in range(n):
		L.append(lista[i])
		R.append(lista[i+n])
	#Expansion de 4 a 8 bits
	listaExp=permutacion(R,perExp)
	#XOR con la llave
	for i in range(len(lista)):
		XOR.append(listaExp[i] ^ int(Kx[i]))
	#obtención 2 bits de S0 y 2 bits de S1
	XS0=busquedaSx(XOR,s0,0)
	XS1=busquedaSx(XOR,s1,4)
	#Permutación de X
	X=permutacion(XS0+XS1,perX)
	#XOR de permutacion X con parte izquierda 
	for i in range(len(X)):
		XOR2.append(X[i] ^ int(L[i]))
	#Concatenación XOR + Right
	return "".join(str(int) for int in XOR2) + "".join(str(int) for int in R)

#Permutación inicial
listPer=permutacion(plainT,perM)
#Calculo de los 2 llaves
K1=permutacion(key,perK1)
K2=permutacion(key,perK2)

#Cifrado
if op=='E':
	#Primer ronda
	p1=feistelPer(listPer,K1)
	#Senguda ronda con mitadas cambiadas
	p2=feistelPer(permutacion(p1,perSwap),K2)
#Decifrado
elif op=='D':
	#Primer ronda
	p1=feistelPer(listPer,K2)
	#Senguda ronda con mitadas cambiadas
	p2=feistelPer(permutacion(p1,perSwap),K1)
else:
	print("Opción no encontrada")
#Permutación final
resultado=permutacion(p2,perC)
resultado="".join(str(int) for int in resultado)
print(resultado)
