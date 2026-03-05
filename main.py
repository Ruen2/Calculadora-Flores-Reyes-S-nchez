import os  
# módulo 'os' se usa para manejar el sistema de archivos (crear carpetas, verificar existencia de archivos)


# Función de utilidad para pedir y validar un número al usuario, recibe un mensaje y repite la lectura hasta obtener un float

def validar_numero(mensaje): 
    """Verifica que la entrada sea un número válido."""
    while True: 
        valor = input(mensaje)
        try: 
            return float(valor)
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número válido.")

# Lee el archivo de historial y devuelve las líneas como lista

def historial(): 
    """Carga los datos guardados en el archivo txt."""
    lista = []
    if os.path.exists("datos/historial.txt"):
        with open("datos/historial.txt", "r") as f:
            for line in f:
                lista.append(line.strip())
    return lista

# Escribe en el archivo de historial, creando el directorio si es necesario

def guardarhistorial(lista): 
    """Guarda el historial."""
    if not os.path.exists("datos"):
        os.makedirs("datos")
    with open("datos/historial.txt", "w") as f:
        for item in lista:
            f.write(item + "\n")

    # Estudiante 02 (Reyes Cuevas Marco Antonio)

# Suma dos números
def sumar(a, b):
    return a + b
# Resta dos números
def restar(a, b):
    return a - b
#Multiplica dos números
def multiplicar(a, b):
    return a * b
# Divide dos números, devuelve None si el divisor es cero
def dividir(a, b):
    if b == 0:
        return None
    return a / b
# Calcula el resto de la división de a por b (módulo), devuelve None si el divisor es cero
def modulo(a, b):
    if b == 0:
        return None
    return a % b
# Eleva un número a la potencia de otro
def potencia(a, b):
    return a ** b

    #Conversions numéricas
def dec2bin(n):
    n = int(n)
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s
# Convierte un número decimal a su representación hexadecimal
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
# Interpreta una cadena binaria y devuelve su valor decimal, devuelve None si la cadena no es un binario válido
def bin2dec(b):
    try:
        return int(str(b), 2)
    except ValueError:
        return None
# Interpreta una cadena hexadecimal y devuelve su valor decimal, devuelve None si la cadena no es un hexadecimal válido
def hex2dec(h):
    try:
        return int(str(h), 16)
    except ValueError:
        return None

# Estudiante 03 (Sánchez Suárez Rubén)

# Conversiones de bytes a kb, mb, gb y viceversa, registrando en historial, convierte bytes a kilobytes y guarda operación en historial

def bytes_a_kb(b):
    resultado = b / 1024
    guardarhistorial(str(b) + " Bytes = " + str(resultado) + " KB")
    return resultado

# Convierte gigabytes a megabytes y graba el resultado en historial, convierte kilobytes a megabytes guardando el cálculo

def kb_a_mb(kb):
    resultado = kb / 1024
    guardarhistorial(str(kb) + " KB = " + str(resultado) + " MB")
    return resultado

# Convierte megabytes a gigabytes y anota en historial

def mb_a_gb(mb):
    resultado = mb / 1024
    guardarhistorial(str(mb) + " MB = " + str(resultado) + " GB")
    return resultado

# Convierte kilobytes a bytes y registra la operación

def kb_a_bytes(kb):
    resultado = kb * 1024
    guardarhistorial(str(kb) + " KB = " + str(resultado) + " Bytes")
    return resultado

# Convierte megabytes a kilobytes guardando en historial

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
    n2 = validar_numero("Ingrese su segundo numero: ")
    res = None
    simbolo = ""
            if sub_op == "1":
                res = sumar(n1, n2)
                simbolo = "+"
            elif sub_op == "2":
                res = restar(n1, n2)
                simbolo = "-"
            elif sub_op == "3":
                res = multiplicar(n1, n2)
                simbolo = "*"
            elif sub_op == "4":
                res = dividir(n1, n2)
                simbolo = "/"
            elif sub_op == "5":
                res = modulo(n1, n2)
                simbolo = "%"
            elif sub_op == "6":
                res = potencia(n1, n2)
                simbolo = "^"
            if res is None:
                print("Error: Operación inválida o división por cero.")
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
            if sub_op == "1":
                res = bytes_a_kb(val)
                txt = f"{val} Bytes a KB"
            elif sub_op == "2":
                res = kb_a_mb(val)
                txt = f"{val} KB a MB"
            elif sub_op == "3":
                res = mb_a_gb(val)
                txt = f"{val} MB a GB"
            elif sub_op == "4":
                res = kb_a_bytes(val)
                txt = f"{val} KB a Bytes"
            elif sub_op == "5":
                res = mb_a_kb(val)
                txt = f"{val} MB a KB"
            elif sub_op == "6":
                res = gb_a_mb(val)
                txt = f"{val} GB a MB"
            print(f"Resultado: {res}")
            lista_historial.append(f"{txt} = {res}")
#Funcionamiento de las opciones del menú principal "Sistemas"
        elif opcion == "3":
            print("\n--- SISTEMAS NUMÉRICOS ---")
            print("1. Dec a Bin | 2. Dec a Hex | 3. Bin a Dec | 4. Hex a Dec")
            sub_op = input("Seleccione: ")
            res = None
            if sub_op == "1":
                n = validar_numero("Número decimal: ")
                res = dec2bin(n)
                lista_historial.append(f"Decimal {n} a Binario = {res}")
            elif sub_op == "2":
                n = validar_numero("Número decimal: ")
                res = dec2hex(n)
                lista_historial.append(f"Decimal {n} a Hexadecimal = {res}")
            elif sub_op == "3":
                b = input("Número binario: ")
                res = bin2dec(b)
                lista_historial.append(f"Binario {b} a Decimal = {res}")
            elif sub_op == "4":
                h = input("Número hexadecimal: ")
                res = hex2dec(h)
                lista_historial.append(f"Hexadecimal {h} a Decimal = {res}")
            if res is not None:
                print(f"Resultado: {res}")
            else:
                print("Error: Entrada de sistema numérico inválida.")

# Desarrollo de historial
        elif opcion == "4":
            print("\n" + "-"*10 + " HISTORIAL (Últimas 10) " + "-"*10)
            if not lista_historial:
                print("No hay registros.")
            else:
                for item in lista_historial[-10:]:
                    print(item)
        # Opción de limpiar historial
        elif opcion == "5":
            lista_historial.clear()
            print("Historial borrado.")
        # Opción de salir
        elif opcion == "6":
            guardarhistorial(lista_historial)
            print("¡Gracias por utilizar nuestra calculadora! Tu historial fue guardado.")
            break
        else:
            print("Opción no válida.")
# Inicio de programa
if __name__ == "__main__":
    programa_principal()  

