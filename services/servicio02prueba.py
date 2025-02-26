from models import mascota


def getSaludo():
    print("ok en servicio 2 ")

def getMascota1(): 
    Data=mascota.Mascota()
    Data.nombre="SIRI"
    Data.raza="Gato Montes"
    Data.edad=3
    return Data


def getMascota2():
    Data=mascota.Mascota()
    Data.nombre="David"
    Data.raza="Humano"
    Data.edad=48
    return Data
