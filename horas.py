import numpy as np

def cargas(imponibles_promedio):
    if imponibles_promedio<=649039:
        return 22601
    if imponibles_promedio<=947990:
        return 13870
    if 1478539<=imponibles_promedio:
        return 0


def horas_ext(sueldo_base,horas_extra):
    hora_normal=(sueldo_base/30)*(28/168)
    return hora_normal*1.5*horas_extra



def imponibles(sueldo_base, comisiones, bonos,horas_extra):
    
    def calculo_gratificacion(sueldo_base):
        if sueldo_base*0.25>=213354:
            return 213354
        else:
            return sueldo_base*0.25
        
    gratificacion=calculo_gratificacion(sueldo_base)
    
    horas_mas=horas_ext(sueldo_base,horas_extra)
        
    return sueldo_base + gratificacion + comisiones + bonos+horas_mas


def no_imponibles(movilizacion, colacion, cargas1,imponible):
    valor_cargas=cargas1*cargas(imponible)
    return movilizacion+colacion+cargas1+valor_cargas


def descuentos(AFP,imponible,fijo=False):
    salud=imponible*0.7
    afp_fijo=10
    if fijo==True:
        afc=0
    else:
        afc=imponible*0.6
    if AFP=="Uno":
        afp_fijo+=0.46
    elif AFP=="Modelo":
        afp_fijo+=0.58
    elif AFP=="Planvital":
        afp_fijo+=1,16
    elif AFP=="Habitat":
        afp_fijo+=1,27
    elif AFP=="Capital":
        afp_fijo+=1.44
    elif AFP=="Cuprum":
        afp_fijo+=1.44
    elif AFP=="Provida":
        afp_fijo+=1.45
    return salud+afp_fijo+afc

def calculo(imp,n_imp,descuentos):
    return (imp+n_imp)-descuentos


