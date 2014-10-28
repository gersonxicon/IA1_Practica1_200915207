import sys
import random
import csv
import math

def test():
    k=0
    thethas2=[]
    for k in range (0,len(thethas)):
        thetha=0
        i=0
        suma=0
        for i in range(0,m):
            xi=xs[i]
            val=0
            j=0
            while j<len(xi):
                val=val+xi[j]*thethas[j]
                j+=1
            val=val-ys[i]
            val=val*xi[k]
            suma+=val
        thetha=thethas[k]-(alpha/float(m))*suma
        thethas2.append(thetha)       
    return thethas2
	
def costos():
    i=0
    suma=0
    for i in range(0,m):
        xi=xs[i]
        val=0
        j=0
        while j<len(xi):
	        val+=xi[j]*thethas[j]
	        j+=1
        val=val-ys[i]
        val=val*val
        suma+=val        
    return (1/float(2*m))*suma
	

    
#------------------	
lasx = open('D:/Tareas/IA1/Laboratorio/IA1_Practica1_200915207/Entradas/xs.csv','r')
lasy = open('D:/Tareas/IA1/Laboratorio/IA1_Practica1_200915207/Entradas/ys.csv','r')
listax = lasx.readline()
listay = lasy.readline()
xs=[]
ys=[]
while listax and listay:
    aux=[]
    for num in listax.split(','):
        aux.append(float(num))
    xs.append(aux)
    ys.append(float(listay))
    listax = lasx.readline()
    listay = lasy.readline()
print ('xs\n')
print (xs)
print ('\nys\n')
print (ys)
print ('\n')
alpha=float(0.01)
iteraciones=int(40000)
tolerancia=float(0.0001)
n=len(xs[0])
m=len(ys)
thethas=[]
for val in xs[0]:
    thethas.append(random.uniform(-25,25))
print ('Inicio:'+str(thethas))

i=0       
archivo=open("D:/Tareas/IA1/Laboratorio/IA1_Practica1_200915207/Costos.txt","w")

for i in range(0,iteraciones):
    thethas=test()
    archivo.write(str(costos())+" ")        
archivo.close()   
print ('Fin:'+str(thethas))	

	