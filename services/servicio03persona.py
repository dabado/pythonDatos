from models import persona as person


def getSaludo():
    print("ok en servicio persona ")

def getPersona1(): 
    getPersona1=person.Persona()
    getPersona1.nombre="Juanito"
    getPersona1.email="juanito@juanito.com"
    getPersona1.edad=48
    getPersona1.oficio="Carpintero"
    return getPersona1

def getPersona2(): 
    getPersona2=person.Persona()
    getPersona2.nombre="Antonio"
    getPersona2.email="Antonio@Antonio.com"
    getPersona2.edad=42
    getPersona2.oficio="Enfermera"

    return getPersona2

def getPersona3(): 
    getPersona3=person.Persona()
    getPersona3.nombre="Manuela"
    getPersona3.email="Manuela@Manuela.com"
    getPersona3.edad=34
    getPersona3.oficio="Conductor"
    return getPersona3