'modulo de inventarios'
class Inventario:
    def __init__(self):
        self.ingredientes = {}
    
    def agregar_ingrediente(self, nombre, cantidad, unidad):
        """ Agrega un ingrediente al inventario """
        if nombre in self.ingredientes:
            self.ingredientes[nombre]['cantidad'] += cantidad
        else:
            self.ingredientes[nombre] = {'cantidad': cantidad, 'unidad': unidad}
    
    def definir_porcion(self, nombre, porcion, unidad):
        """ Define una porción para un ingrediente """
        if nombre in self.ingredientes:
            self.ingredientes[nombre]['porcion'] = porcion
            self.ingredientes[nombre]['unidad_porcion'] = unidad
        else:
            print(f"Ingrediente {nombre} no encontrado en el inventario.")
    
    def calcular_consumo(self, nombre, cantidad_porciones):
        """ Calcula el consumo de un ingrediente según la cantidad de porciones """
        if nombre in self.ingredientes and 'porcion' in self.ingredientes[nombre]:
            return self.ingredientes[nombre]['porcion'] * cantidad_porciones
        else:
            print(f"Porción no definida para el ingrediente {nombre}.")
            return None
    
    def actualizar_inventario(self, nombre, cantidad_porciones):
        """ Reduce la cantidad de un ingrediente en el inventario basado en la cantidad de porciones utilizadas """
        consumo = self.calcular_consumo(nombre, cantidad_porciones)
        if consumo is not None and nombre in self.ingredientes:
            if self.ingredientes[nombre]['cantidad'] >= consumo:
                self.ingredientes[nombre]['cantidad'] -= consumo
                print(f"Inventario actualizado: {nombre} restante: {self.ingredientes[nombre]['cantidad']} {self.ingredientes[nombre]['unidad']}")
            else:
                print(f"No hay suficiente {nombre} en el inventario.")
