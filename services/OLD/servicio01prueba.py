from models.old import mascota


def getSaludo():
    print("ok en servicios ")

def getMascota1(): 
    Data=mascota.Mascota()
    Data.nombre="Pepe"
    Data.raza="dogo"
    Data.edad=4
    return Data


def getMascota2():
    Data=mascota.Mascota()
    Data.nombre="KIRA"
    Data.raza="Gato Comun"
    Data.edad=8
    return Data
