import random
import time
n = []

def sortear_números():
    usuario = int(input("Quantos valores e para eu sortear = "))
    while True:
        for i in range(0, usuario):
            s = random.randint(1, 10)
            if s == s in n:
                pass
            else:
                n.append(s)
        if len(n) == usuario:
            break
    print(f"Sorteando {usuario} valores da lista:", end='')
    for i in n:
        print(f" {i} ", end='',flush=True)
        time.sleep(0.5)
    print("PRONTO!")

def somar_par():
    par = 0
    for i in n:
        if i % 2 == 0:
            par += i
    print(f"Somando os valores pares de {n}, temos {par}")


sortear_números()
somar_par()
