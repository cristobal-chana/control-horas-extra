import horas as hrs
import json
import pathlib as pt
import estructuras as est
###################################################################
ruta=pt.Path("datos/registros.json")
if ruta.is_file():
    pass
else:
    ruta.parent.mkdir(parents=True,exist_ok=True)
    data={}
    with open(ruta,"w",encoding="utf-8") as archivo:
        json.dump(data,archivo,indent=4,ensure_ascii=False)
#####################################################################

sueldo=input("Ingrese su sueldo base")
    #comisiones=input("Ingrese comisiones")
    #bonos=input("Ingrese Bonos")    #

    #movilizacion=input("Ingrese movilziacion")
    #colacion=input("Ingrese colacion")
    #cargas=input("Cargas")
    #afp=input("Tipo de AFP ")   #

    #fijo=input("¿Contrato fijo?")
    #if fijo=="Si":
    #    fijo==True
    #else:
    #    fijo==False #


def HORAS():
    fecha=str(input("Ingrese fecha"))
    hora_extra=float(input("Ingrese numero de horas extras"))

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
HORAS()
    

