import numpy as np
import time
import threading


matriz = np.random.rand(3, 10) # valores random
ceros = np.zeros((1, 10)) # matriz para Z, con ceros

matriz[2] = ceros

nucleos = 2 #ejemplo para L.A.

localtime = time.localtime()
result = time.strftime("%I:%M:%S %p", localtime)
start = time.time()

def calcularZ():
    for i in range(len(matriz[0])):
        matriz[2][i] = matriz[0][i] + matriz[1][i]
        time.sleep(1)

def calcularZSpecific(a, b):
    for i in range(a, b):
        matriz[2][i] = matriz[0][i] + matriz[1][i]
        time.sleep(1)
    
def tiempo():
    global localtime, start
    localtime = time.localtime()
    start = time.time()
    result = time.strftime("%I:%M:%S %p", localtime)
    print("Empezado: ", result)

def printDif():
    global localtime, start
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    done = time.time()
    elapsed = done - start
    print("TERMINADO:", result, "\nTardó ", elapsed, " seg \n")

def leyAhmdals(n, p):
    return (1 / ((1-p) + (p/n)))

print("PRIMER INCISO")
tiempo()
calcularZ()
printDif()



######## Segunda parte
matriz[2] = ceros # reseteando matriz
hilos = 2
tareas = []
for i in range(0, hilos):
    thread = threading.Thread(target=calcularZSpecific(5*i, 5 *(i+1)))
    tareas.append(thread)
print("\n \nSEGUNDO INCISO")
tiempo()
for t in tareas:
    t.start()
printDif()
print("Según L.A. es ", leyAhmdals(nucleos, 1/hilos))


#### Tercer ejercicio
matriz[2] = ceros # reseteando matriz
hilos = 5
tareas = []
for i in range(0, hilos):
    thread = threading.Thread(target=calcularZSpecific(2*i, 2 *(i+1)))
    tareas.append(thread)
print("\n \nTERCER INCISO")
tiempo()
for t in tareas:
    t.start()
printDif()
print("Según L.A. es ", leyAhmdals(nucleos, 1/hilos))