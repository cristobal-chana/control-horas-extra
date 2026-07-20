import horas as hrs
import json
import pathlib as pt
import estructuras as est
import ordenacion as ord
###################################################################
ruta=pt.Path("datos/registros.json")
ruta1=pt.Path("datos/sumatorias.json")
#####################################################################


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

#En este apartado debe ir la parte de la grafica, estoy haciendo todo lo que incluya manejo de archivos
# Y demas en  diferentes modulos
sueldo=200000
fecha="2002-02-02"
hora_extra=12.0

ord.actualizar_registros(ruta,fecha,hora_extra,sueldo)
ord.sumatoria_horas_dinero(ruta, ruta1)
    

