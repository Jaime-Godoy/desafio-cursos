import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cursos.settings')

import django
django.setup()

from app import services

# Crear un profesor
profesor_juan = services.crear_profesor("123456789", "Juan", "Pérez", "Admin")

# Crear un curso
curso_programacion = services.crear_curso("PROG101", "Programación", 1)

# Crear un estudiante
estudiante_maria = services.crear_estudiante("987654321", "María", "González", "2000-01-01", "Admin")

# Crear una dirección para el estudiante
direccion_maria = services.crear_direccion("Calle Principal", 123, "A", "Santiago", "Santiago", "Metropolitana", estudiante_maria)

# Obtener un profesor por su rut
profesor_obtenido = services.obtener_profesor("123456789")
if profesor_obtenido:
    print("Profesor encontrado:", profesor_obtenido.nombre, profesor_obtenido.apellido)
else:
    print("Profesor no encontrado.")

# Obtener un curso por su código
curso_obtenido = services.obtener_curso("PROG101")
if curso_obtenido:
    print("Curso encontrado:", curso_obtenido.nombre)
else:
    print("Curso no encontrado.")

# Obtener un estudiante por su rut
estudiante_obtenido = services.obtener_estudiante("987654321")
if estudiante_obtenido:
    print("Estudiante encontrado:", estudiante_obtenido.nombre, estudiante_obtenido.apellido)
else:
    print("Estudiante no encontrado.")

# Obtener la dirección de un estudiante
direccion_estudiante = services.obtener_direccion(estudiante_maria)
if direccion_estudiante:
    print("Dirección de estudiante encontrada:", direccion_estudiante.calle, direccion_estudiante.numero)
else:
    print("Dirección de estudiante no encontrada.")
