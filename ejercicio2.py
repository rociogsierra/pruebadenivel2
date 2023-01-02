
#APARTADO 1
#Se deben contemplar tres niveles de prioridad para la cola
#mayor prioridad
#prioridad media
#prioridad baja

#APARTADO 2
#cada pedido de sugerencia cuenta con la siguiente información: 
#nombre del “Khan” solicitante, multiverso en el que se encuentra o el más próximo y descripción del pedido
class pedidos_de_sugerencia():
    def __init__(self, nombre_khan_solicitante, multiverso, descripcion):
        self.nombre_khan_solicitante = nombre_khan_solicitante
        self.multiverso = multiverso
        self.descripcion = descripcion
        self.prioridad = ""
    def __str__(self):
        return "El Khan solicitante es {}, procedente del multiverso {}, cuya descripción es {} y su orden de prioridad {}".format(self.nombre_khan_solicitante, self.multiverso, self.descripcion, self.prioridad)

#APARTADOS 3 y 4
def orden_de_prioridad(orden):
    orden_nombre_khan_solicitante = {"Gran conquistador: mayor prioridad", "Khan que todo lo sabe: prioridad media"}
    orden_multiverso = {"Universo_616: mayor prioridad", "Universo_838: prioridad media"}
    orden_descripcion = {"El que permanece: mayor prioridad", "Carnicero de dioses: prioridad media"}

