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

    if datos.get(fecha) is not None:
        return f"Esta fecha ya esta ocupada con {datos.get(fecha)}"

    ganancia=hrs.horas_ext(int(sueldo),hora_extra)
    datos[fecha]={"Horas Extra":str(hora_extra),"Ganancia":str(ganancia)}
    datos_ordenados=est.radix_sort(datos)

    with open(ruta,"w",encoding="utf-8") as archivo:
        json.dump(datos_ordenados,archivo, indent=4, ensure_ascii=False)