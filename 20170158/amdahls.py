# JOSÉ ALEJANDRO GUZMÁN ZAMORA

import numpy as np 
import time
import threading

matriz = np.hstack([np.random.randint(100, size=(10,2)),np.zeros((10,1))])

def funcion(matriz,resultado):
    for i in range(matriz.shape[0]):
        matriz[i,2] = matriz[i,0] + matriz[i,1]
        time.sleep(1)
        print("Cálculo Realizado: ",matriz[i])
    resultado.append(matriz[:,2])

def separation(cantidad,matriz):
    comienzo = time.time()
    size = int(matriz.shape[0] / cantidad)
    hilos = []
    res = []
    for i in range(cantidad):
        hilos.append(
            threading.Thread(target=funcion, args=(matriz[i * size: (i + 1) * size,:],res,))
            )
        hilos[i].start()
    for i in hilos:
        i.join()
    print("RESULTADO")
    print(matriz[:,2])
    final = time.time() - comienzo
    print("DURACIÓN: ",final)


print("UTILIZANDO 1 HILOS")
separation(1,matriz)

print("UTILIZANDO 2 HILOS")
separation(2,matriz)

print("UTILIZANDO 5 HILOS")
separation(5,matriz)

