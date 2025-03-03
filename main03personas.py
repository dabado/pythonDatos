from services import servicio03persona as service
from models.old import persona as person

personaje1 = service.getPersona1()
personaje2 = service.getPersona2()
personaje3 = service.getPersona3()
print(f"personaje1: trabaja como {personaje1.oficio} ,el nombre de esta persona es {personaje1.nombre} , tiene {personaje1.edad} años , y email es {personaje1.email}")
print(f"personaje2: trabaja como {personaje2.oficio}, el nombre de esta persona es {personaje2.nombre} , tiene {personaje2.edad} años , y email es {personaje2.email}")
print(f"personaje3: trabaja como {personaje3.oficio}, el nombre de esta persona es {personaje3.nombre} , tiene {personaje3.edad} años , y email es {personaje3.email}")

