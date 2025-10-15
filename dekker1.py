import threading
import time
import random

flag = [False, False]  # banderas de cada proceso

def proceso(i):
    global flag
    j = 1 - i  # el otro proceso
    
    while True:
        # Quiere entrar a la sección crítica
        flag[i] = True
        print(f"P{i} quiere entrar a la sección crítica.")
        
        # Espera mientras el otro quiera entrar
        while flag[j]:
            print(f"P{i} esperando... (P{j} también quiere entrar)")
            time.sleep(1)
        
        # Sección crítica
        print(f" P{i} entra a la sección crítica.")
        time.sleep(random.uniform(1, 2))  # simulamos trabajo
        print(f" P{i} sale de la sección crítica.")
        
        # Sale de la sección crítica
        flag[i] = False
        
        # Sección no crítica
        time.sleep(random.uniform(1, 3))

# Crear y lanzar los hilos
t1 = threading.Thread(target=proceso, args=(0,))
t2 = threading.Thread(target=proceso, args=(1,))

t1.start()
t2.start()