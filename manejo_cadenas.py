nombre = "marco"
apellido = "MENDOZA"
frace = "Hola Esta es una Frace"

# famos a contar todo los caracteres en una cadena ya sea diccionaria cadena o tupla

lomgitud = len(frace)
print(lomgitud)

print(apellido[0]) # ---> se extrae el carcater la bariables que se tiene al ccambiar el numero al colocar 0 nos extraera la letra M si se colcoca 1 se extreae la letra e

palabras = frace.split()
print(palabras)

mayusculas = nombre.upper()
print(mayusculas)

minusculas = apellido.lower()
print(minusculas)

mensaje = "hola, Mundo"
cambio = mensaje.replace("hola", "Marcos")
print(cambio)

for x in apellido:
    print(x)
