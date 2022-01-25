

def firstDifFProg(h,fn): # Primera dervicada por diferencias finitas progresivas
    # h, valor de paso (step) de la variable independiente (n)
    # fn, debe de ser un vector de por lo menos 2 valores
    dev=[] # inicializo el vector derivada
    i=0 # inicializo un centinela
    while i<len(fn)-1: # lo dejo como menor y no menos o igual y ademas le resto 1, por que las listas tienen posición 0 pero len da el numero de datos y porque diff prograsivas debe tener un valor menos que el la función primitiva.
        dev.append((fn[i+h]-fn[i])/h)
        i+=1
    return dev
