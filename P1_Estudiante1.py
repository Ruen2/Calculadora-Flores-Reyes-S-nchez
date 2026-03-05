import os 

# Estudiante 01 (Flores Rentería Atziry)

def validar_numero(mensaje): 
    """Verifica que la entrada sea un número válido."""
    while True: 
        valor = input(mensaje)
        try: 
            return float(valor)
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número válido.")

def historial(): 
    """Carga los datos guardados en el archivo txt."""
    lista = []
    if os.path.exists("datos/historial.txt"):
        with open("datos/historial.txt", "r") as f:
            for line in f:
                lista.append(line.strip())
    return lista

def guardarhistorial(lista): 
    """Guarda el historial."""
    if not os.path.exists("datos"):
        os.makedirs("datos")
    with open("datos/historial.txt", "w") as f:
        for item in lista:
            f.write(item + "\n")


# Estudiante 02 (Reyes Cuevas Marco Antonio


# Estudiante 03 (Sánchez Suárez Rubén)


# Evidencia/ Integración (Estudiante 01 Flores Rentería Atziry) 
# Yo junto lo que ustedes hagan, para realizar el menú.