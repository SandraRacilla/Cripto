#Sandra García Racilla
#Criptografía
#RC4
S=[]
T=[]
aux=[]
keyStream=[]
XOR=[]
key=input()
plainT=input()

def KSA():
	global S
	##Inicialización de los Vectores S y T
	#Vector S
	for i in range (256):
		S.append(i)
	#Vector T
	for letra in key:
		T.append(ord(letra))
	j=0
	for i in range (256):
		#Nuevo valor j
		j=( j + S[i] + T[i % len(key)] ) % 256
		#Intercambio
		temp= S[i]
		S[i] = S[j]
		S[j] = temp

def PRGA():
	global S,keyStream,plainT
	#inicialización variables
	i= j = k = 0
	while (k < len(plainT)):
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		#intercambio
		temp = S[i]
		S[i] = S[j]
		S[j] = temp
		keyStream.append(S[(S[i] + S[j]) % 256])
		k+=1
#Función para dar formato a valor hexadecimal
#Le quita los caracteres '0x' a cada número hexadecimal y las letras las pone en mayúscula
def hexa(lista):
	for i in range (len(lista)):
		#Si el valor es menor que 9 contatenamos un '0'
		#para tener 2 bytes por caracter
		if int(lista[i],16)<=9:
			lista[i]='0'+lista[i][2:].upper()
		else:
			lista[i]=lista[i][2:].upper()
	return lista

KSA()
PRGA()
v=0
#Realiza operación XOR de cada caracter del texto claro con cada keyStrem
#El resultado de la operación la convierte a valor hexadecimal
for letra in plainT:
	XOR.append(hex(keyStream[v] ^ ord(letra)))
	v+=1
#Llama a la función 'hexa' y une cada valor de la lista en una cadena
cipherText="".join(hexa(XOR))
print(cipherText)
