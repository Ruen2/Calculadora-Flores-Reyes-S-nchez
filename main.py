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


# Estudiante 02 (Reyes Cuevas Marco Antonio)

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b

def modulo(a, b):
    if b == 0:
        return None
    return a % b

def potencia(a, b):
    return a ** b

# conversions numéricas

def dec2bin(n):
    n = int(n)
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s

def dec2hex(n):
    n = int(n)
    if n == 0:
        return "0"
    hex_dig = "0123456789ABCDEF"
    s = ""
    while n > 0:
        s = hex_dig[n % 16] + s
        n //= 16
    return s

def bin2dec(b):
    try:
        return int(str(b), 2)
    except ValueError:
        return None

def hex2dec(h):
    try:
        return int(str(h), 16)
    except ValueError:
        return None

# Estudiante 03 (Sánchez Suárez Rubén)
# Conversiones de bytes a kb, mg, gb y viceversa.
def bytes_a_kb(b):
    resultado = b / 1024
    guardarhistorial(str(b) + " Bytes = " + str(resultado) + " KB")
    return resultado

def kb_a_mb(kb):
    resultado = kb / 1024
    guardarhistorial(str(kb) + " KB = " + str(resultado) + " MB")
    return resultado

def mb_a_gb(mb):
    resultado = mb / 1024
    guardarhistorial(str(mb) + " MB = " + str(resultado) + " GB")
    return resultado

def kb_a_bytes(kb):
    resultado = kb * 1024
    guardarhistorial(str(kb) + " KB = " + str(resultado) + " Bytes")
    return resultado

def mb_a_kb(mb):
    resultado = mb * 1024
    guardarhistorial(str(mb) + " MB = " + str(resultado) + " KB")
    return resultado

def gb_a_mb(gb):
    resultado = gb * 1024
    guardarhistorial(str(gb) + " GB = " + str(resultado) + " MB")
    return resultado

# Evidencia/ Integración (Estudiante 01 Flores Rentería Atziry) 

# Yo junto lo que ustedes hagan, para realizar el menú.

