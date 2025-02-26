
#from services import servicio01prueba as servi
from services import servicio02prueba as servi
from models import mascota

print("todo bien en main")


saludo = servi.getSaludo()


perro = servi.getMascota1()
gato = servi.getMascota2()
print(f"Se llama {gato.nombre}, tiene {gato.edad} años, es un {gato.raza}")
print(f"Se llama {perro.nombre}, tiene {perro.edad} años, es un {perro.raza}")


