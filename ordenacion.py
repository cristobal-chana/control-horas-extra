import json 
import pathlib as pt
import horas as hrs
import estructuras as est

def sumatoria_horas_dinero(ruta,ruta1):
    if ruta1.is_file():
        pass
    else:
        ruta1.parent.mkdir(parents=True,exist_ok=True)
        data={}
        with open(ruta1,"w",encoding="utf-8") as archivo:
            json.dump(data,archivo,indent=4,ensure_ascii=False)#Entrara un json y devolvera la sumatoria del apartado de "Horas extra" y "Ganancia"
    
    with open(ruta, "r",encoding="utf-8" ) as archivo:
        datos=json.load(archivo)
    keys=list(datos.keys())
    lista_horas=[]
    lista_ganancia=[]
    for e in keys:
        diccionario=datos[e]
        lista_horas.append(float(diccionario["Horas Extra"]))
        lista_ganancia.append(float(diccionario["Ganancia"]))
    h=sum(lista_horas)
    g=sum(lista_ganancia)
    data= {"Sumas":{"Horas" : str(h),"Ganancia":str(g)}}
    
    with open(ruta1, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)



fecha=str(input("Ingrese fecha"))
hora_extra=float(input("Ingrese numero de horas extras"))


def actualizar_registros(ruta,fecha,hora_extra,sueldo):
    if ruta.is_file():
        pass
    else:
        ruta.parent.mkdir(parents=True,exist_ok=True)
        data={}
        with open(ruta,"w",encoding="utf-8") as archivo:
            json.dump(data,archivo,indent=4,ensure_ascii=False)

    with open(ruta,"r",encoding="utf-8") as archivo1:
        datos=json.load(archivo1)

    if datos.get(fecha) is None:
        ganancia=hrs.horas_ext(int(sueldo),hora_extra)
        datos[fecha]={"Horas Extra":str(hora_extra),"Ganancia":str(ganancia)}
        with open(ruta,"w",encoding="utf-8") as archivo1:
            json.dump(datos,archivo1,indent=4,ensure_ascii=False)
    else:

        return "Esta fecha ya esta ocupada con " f"{"datos.get(fecha)"}"
    
    with open(ruta, "r",encoding="utf-8" ) as archivo:
        json_1=json.load(archivo)
    json_2=est.radix_sort(json_1)
    
    with open(ruta,"w",encoding="utf-8") as archivo:
        json.dump(json_2,archivo, indent=4, ensure_ascii=False)