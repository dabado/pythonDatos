from models import persona as person


def getSaludo():
    print("ok en servicio persona ")

def getPersona1(): 
    Data=person.Persona()
    Data.nombre="Juanito"
    Data.email="juanito@juanito.com"
    Data.edad=48
    Data.oficio="Carpintero"
    return Data

def getPersona2(): 
    Data=person.Persona()
    Data.nombre="Antonio"
    Data.email="Antonio@Antonio.com"
    Data.edad=42
    Data.oficio="Enfermera"

    return Data

def getPersona3(): 
    Data=person.Persona()
    Data.nombre="Manuela"
    Data.email="Manuela@Manuela.com"
    Data.edad=34
    Data.oficio="Conductor"
    return Data