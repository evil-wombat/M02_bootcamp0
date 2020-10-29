# Para crear un objeto, primero definimos su clase:


#Por convenio el nombre siempre empieza por Mayuscula
class Perro(): 
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso