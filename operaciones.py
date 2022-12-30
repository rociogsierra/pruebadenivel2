
def suma(primer_num, segundo_num):
    try:
        return primer_num + segundo_num
    except TypeError:
        print("ERROR: Tipo de dato no válido")

def resta(primer_num, segundo_num):
    try:
        return primer_num - segundo_num
    except TypeError:
        print("ERROR: Tipo de dato no válido")
    