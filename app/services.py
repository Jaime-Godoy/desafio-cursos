from app.models import Profesor, Curso, Estudiante, Direccion

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=True,  # Por defecto activo al crear
        creado_por=creado_por
    )
    profesor.save()
    return profesor

def crear_curso(codigo, nombre, version):
    curso = Curso(
        codigo=codigo,
        nombre=nombre,
        version=version
    )
    curso.save()
    return curso

def crear_estudiante(rut, nombre, apellido, fecha_nac, creado_por):
    estudiante = Estudiante(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac,
        activo=True,  # Por defecto activo al crear
        creado_por=creado_por
    )
    estudiante.save()
    return estudiante

def crear_direccion(calle, numero, depto, comuna, ciudad, region, estudiante):
    direccion = Direccion(
        calle=calle,
        numero=numero,
        depto=depto,
        comuna=comuna,
        ciudad=ciudad,
        region=region,
        estudiante_id=estudiante
    )
    direccion.save()
    return direccion

def obtener_profesor(rut):
    try:
        profesor = Profesor.objects.get(rut=rut)
        return profesor
    except Profesor.DoesNotExist:
        return None

def obtener_curso(codigo):
    try:
        curso = Curso.objects.get(codigo=codigo)
        return curso
    except Curso.DoesNotExist:
        return None

def obtener_estudiante(rut):
    try:
        estudiante = Estudiante.objects.get(rut=rut)
        return estudiante
    except Estudiante.DoesNotExist:
        return None

def obtener_direccion(estudiante):
    try:
        direccion = Direccion.objects.get(estudiante_id=estudiante)
        return direccion
    except Direccion.DoesNotExist:
        return None
