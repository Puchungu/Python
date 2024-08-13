class Carro:
    def __init__(self, color, marca, modelo, vin, motor, placa, tipo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.vin = vin
        self.motor = motor
        self.placa = placa
        self.tipo = tipo

    def datos(self):
        return f"Datos del vehiculo: Color: {self.color}, Marca: {self.marca}, Modelo: {self.modelo}, VIN: {self.vin}, Motor: {self.motor}, Placa: {self.placa}, Tipo: {self.tipo}"

carro1 = Carro("Rojo", "Toyota", "Corolla", "1234567890", "a", "P345678", "sedan")
print(carro1.datos())


"""
class libro():
    def __init__(self,titulo,autor,edicion):
        self.editorial = "Libreria El Salvador"
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion

    def datos(self):
            print(f"Titulo: {self.titulo} Autor: {self.autor}")
libro1 = libro("a","b","c")
libro1.datos()
"""
