import numpy as np


class Cola: #Es una cola sencilla, solo FIFO
    def __init__(self):
        self.cola=[]
        self.tamaño=len(self.cola)
    
    def encolar(self,x):
        self.cola.append(x)
        self.tamaño+=1
    def sacar(self):
        x=self.cola.pop(0)
        self.tamaño-=1
        return x
    def is_empty(self):
        if self.tamaño == 0:
            return True
        else:
            return False
"2029-01-03"

def sacar_guion(string):
    lista=[]
    for e in string:
        if e=="-":
            pass
        else:
            lista.append(e)
    return "".join(lista)

def poner_guion(string): #Recibiria un string limpio
    lista=[]
    i=0
    for e in string:
        if i==4 or i==7:
            lista.append("-")
            lista.append(e)
            i+=2
        else:
            lista.append(e)
            i+=1
    return "".join(lista)
"01234567"
def radix_sort(json):#Esta funcion va orientado a ordenar llaves del json
    llaves=list(json.keys())
    cola=Cola()#Aqui ya obtuve las llaves, de aqui, simplemente ordenare, despues en el json sobreescribire con los datos ordenados
    for e in llaves:
        nueva_llave=sacar_guion(e)
        cola.encolar(nueva_llave)
    

    indice=7
    while indice>=0:
        cola0=Cola()
        cola1=Cola()
        cola2=Cola()
        cola3=Cola()    
        cola4=Cola()
        cola5=Cola()
        cola6=Cola()
        cola7=Cola()    
        cola8=Cola()
        cola9=Cola()  
        lista=[cola0,cola1,cola2,cola3,cola4,cola5,cola6,cola7,cola8,cola9]
        while not cola.is_empty():
            value=cola.sacar()

            indice2=int(value[indice])
            lista[indice2].encolar(value)
        #Reconstruccion de la cola
        for e in lista:
            while not e.is_empty():
                x=e.sacar()
                cola.encolar(x)
        indice-=1
    #Aqui la cola ya debe estar ordenado asi que con sacarlo, deberia sacarlo ordenado
    llaves_actualizadas=[]
    while not cola.is_empty():
        x=cola.sacar()
        llaves_actualizadas.append(poner_guion(x))
    #Hay que reconstruir el json, para ello tomaremos la llave ordenada, y el json original y crearemos un json modificado
    json_modificado={}
    for e in llaves_actualizadas:
        valor=json[e]
        json_modificado[e]=valor
    return json_modificado

            



