# Solicitar la cantidad de alumnos
cantidad = int(input("¿Cuántos alumnos desea calificar? "))
alumnos = []

# Recorrer la cantidad de alumnos
for i in range(cantidad):
    print(f"\nAlumno {i + 1}:")
    nombre = input("Ingrese el primer nombre del alumno: ")
    apellido = input("Ingrese el primer apellido del alumno: ")
    nota = float(input("Ingrese la nota del alumno: "))

    # Evaluar la nota
    if nota >= 90:
        mensaje = "¡Felicidades! Has aprobado con una calificación sobresaliente."
    elif nota >= 70:
        mensaje = "Has aprobado satisfactoriamente."
    elif nota >= 60:
        mensaje = "Has aprobado, pero necesitas mejorar un poco."
    else:
        mensaje = "Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación."

    # Guardar los datos en la lista
    alumnos.append({
        "nombre": nombre,
        "apellido": apellido,
        "nota": nota,
        "mensaje": mensaje
    })

# Mostrar el resumen final
print("\n📚 Resumen de calificaciones:")
for alumno in alumnos:
    print(f"- {alumno['nombre']} {alumno['apellido']}: Nota = {alumno['nota']} → {alumno['mensaje']}")