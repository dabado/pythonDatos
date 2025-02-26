from services import servicio03persona
from models import persona as person

personaje1 = servicio03persona.getPersona1()
personaje2 = servicio03persona.getPersona2()
personaje3 = servicio03persona.getPersona3()
print(f"personaje1: trabaja como {personaje1.oficio} ,el nombre de esta persona es {personaje1.nombre} , tiene {personaje1.edad} años , y email es {personaje1.email}")
print(f"personaje2: trabaja como {personaje2.oficio}, el nombre de esta persona es {personaje2.nombre} , tiene {personaje2.edad} años , y email es {personaje2.email}")
print(f"personaje3: trabaja como {personaje3.oficio}, el nombre de esta persona es {personaje3.nombre} , tiene {personaje3.edad} años , y email es {personaje3.email}")

