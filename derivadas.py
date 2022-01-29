

def firstDifFProg(h,fn): # Primera dervicada por diferencias finitas progresivas de primer orden
    # h, valor de paso (step) de la variable independiente (n)
    # fn, debe de ser un vector de por lo menos 2 valores
    dev=[] # inicializo el vector derivada
    i=0 # inicializo el centinela
    while i<len(fn)-1: # lo dejo como menor y no menos o igual y ademas le resto 1, por que las listas tienen posición 0 pero len da el numero de datos y porque diff prograsivas debe tener un valor menos que el la función primitiva al final.
        dev.append((fn[i+1]-fn[i])/h)
        if i==len(fn)-2:
            dev.append(None) # agrega una ultima possicioón con valor None a la lista para recordar que tiene una posición menos que la función primitiva
        i+=1
    return dev

def firstDifFReg(h,fn): # Primera dervicada por diferencias finitas regresivas de primer orden
    # h, valor de paso (step) de la variable independiente (n)
    # fn, debe de ser un vector de por lo menos 2 valores
    dev=[None] # inicializo el vector derivada con la primera posición con valor None debido a que va a tener un valor atrasado, o menor al comienzo, respecto a la función primitiva
    i=1 # inicializo el centinela con valor 1 para empezar a evaluar una posición adelantada
    while i<len(fn): # lo dejo como menor y no menos o igual, por que las listas tienen posición 0 pero len da el numero de datos.
        dev.append((fn[i]-fn[i-1])/h)
        i+=1
    return dev

def firstDifFCent(h,fn): # Primera dervicada por diferencias finitas regresivas de primer orden
    # h, valor de paso (step) de la variable independiente (n)
    # fn, debe de ser un vector de por lo menos 2 valores
    dev=[None] # inicializo el vector derivada con la primera posición con valor None debido a que va a tener un valor atrasado, o menor al comienzo, respecto a la función primitiva
    i=1 # inicializo el centinela con valor 1 para empezar a evaluar una posición adelantada
    while i<len(fn)-1: # lo dejo como menor y no menos o igual y ademas le resto 1, por que las listas tienen posición 0 pero len da el numero de datos y porque diff centradas debe tener un valor menos que el la función primitiva al final.
        dev.append((fn[i+1]-fn[i-1])/(2*h))
        if i==len(fn)-2:
            dev.append(None) # agrega una ultima possicioón con valor None a la lista para recordar que tiene una posición menos que la función primitiva
        i+=1
    return dev
