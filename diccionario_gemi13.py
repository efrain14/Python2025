""" Ejemplo 1: Estudiantes y Cursos (Información Heterogénea)
Imagina que quieres registrar varios cursos en los que está inscrito un estudiante. La clave será el nombre del estudiante y el valor será una lista de cursos.  """




# 1. Crear el diccionario con la lista
registro_estudiante = {
    'nombre': 'Andrea Flores',
    'edad': 24,
    'cursos': ['Introducción a Python', 'Bases de Datos SQL', 'Estructuras de Datos'],
    'activo': True
}

print(f"Diccionario completo: {registro_estudiante}")
print("-" * 30)

# 2. Acceder a la lista completa de cursos
lista_cursos = registro_estudiante['cursos']
print(f"Cursos de Andrea: {lista_cursos}")

# 3. Acceder al segundo curso de la lista (índice 1)
segundo_curso = registro_estudiante['cursos'][1]
print(f"El segundo curso es: {segundo_curso}")

# 4. Agregar un nuevo curso a la lista
registro_estudiante['cursos'].append('Desarrollo Web')
print(f"Cursos actualizados: {registro_estudiante['cursos']}")