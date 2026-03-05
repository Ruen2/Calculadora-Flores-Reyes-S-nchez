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
def programa_principal
    lista_historial = cargar_historial()
                   while True: 
                       print("-----------------------------------------")
                       print("CALCULADORA MULTIFUNCIONAL")
                       print("Equipo: Marco Antonio Reyes Cuevas, Rubén Sánchez Suárez, Atziry Flores Rentería")
                       print("-----------------------------------------")\n
                       
                       print("1. Calculadora básica")
                       print("2. Conversor de unidades de datos")
                       print("3. Calculadora de sistemas numéricos")
                       print("4. Ver historial")
                       print("5. Limpiar historial")
                       print("6. Salir") 

                       opcion = input("\nSeleccione una opción: ")
#Funcionamiento de las opciones del menú principal "Calculadora" 
if opcion == "1": 
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Suma | 2. Resta | 3. Mult. | 4. Div. | 5. Mod | 6. pot") 
    sub_op = input("Seleccione su operación: ")
    n1 = validar_numero("Ingrese su primer número: ")
    n2 = validar_numero(Ingrese su segundo numero: ")
    res = None
    simbolo = ""
    if sub_op == "1": res = sumar(n1, n2); simbolo = "+"
elif sub_op == "2": res = restar(n1, n2); simbolo = "-"
elif sub_op == "3" res = multiplicar(n1, n2); simbolo = "*"
elif sub_op == "4" res = dividir(n1, n2); simbolo = "/"
elif sub_op == "5" res = modulo(n1, n2); simbolo = "%"
elif sub_op == "6" res = potencia(n1, n2); simbolo = "^"

if res is None: 
    print("Error: Operación inválida o división por cero."
          else: 
    texto = f"{n1} {simbolo} {n2} = {res}"
    print(f"Resultado: {texto}")

# Funcionamiento de las opciones del menú principal "Unidades"
elif opcion == "2": 
print("\n--- CONVERSOR DE DATOS ---")
print("1. B a KB | 2. KB a MB | 3. MB a GB | 4. KB a B | 5. MB a KB | 6. GB a MB")
sub_op = input("Seleccione: ")
val = validar_numero("Cantidad: ")

res = 0 
txt = ""

if sub_op == "1": res= bytes_a_kb(val); txt = f"{val} Bytes a KB"
elif sub_op == "2": res= kb_a_mb(val); txt = f"{val} KB a MB"
elif sub_op == "3": res= mb_a_gb(val); txt = f"{val} MB a GB"
elif sub_op == "4": res= kb_a_bytes(val); txt = f"{val} KB a Bytes"
elif sub_op == "5": res= mb_a_kb(val); txt = f"{val} MB a KB"
elif sub_op == "6": res= gb_a_mb(val); txt = f"{val} GB a MB"
    print(f"Resultado: {res}")
lista_historial.append(f"{txt} = {res}")




                      

