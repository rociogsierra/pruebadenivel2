
#SUMA
def suma(primer_num, segundo_num):
    try:
        return primer_num + segundo_num
    except TypeError:
        print("ERROR: Tipo de dato no válido")

#RESTA
def resta(primer_num, segundo_num):
    try:
        return primer_num - segundo_num
    except TypeError:
        print("ERROR: Tipo de dato no válido")
    
#MULTIPLICACIÓN
def multiplicacion(primer_num, segundo_num):
    try:
        return primer_num * segundo_num
    except TypeError:
        print("ERROR: Tipo de dato no válido")

#DIVISIÓN
def division(primer_num, segundo_num):
    try:
        return primer_num / segundo_num
    except TypeError:
        print("ERROR: Tipo de dato no válido")
    except ZeroDivisionError:
        print("ERROR: No es posible dividir entre cero")
