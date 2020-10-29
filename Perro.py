# Para crear un objeto, primero definimos su clase:

class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar (self):       
        if self.peso == None:
            print ('Soy un fantasma')
            return
            
        if self.peso >= 8:
            print ("Woof, woof")
        else:            
            print ("Guau, Guau")

#Por convenio el nombre siempre empieza por Mayuscula
class Perro(): 
    def __init__ (self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad     # Atributos
        self.peso = peso
        
    def ladrar (self):       # Método
        if self.peso >= 8:
            print ("Woof, woof")
        else:            
            print ("Guau, Guau")
    
    def __str__(self):
        return 'Perro: {}, edad: {} años, peso: {} kg'.format(self.nombre, self.edad, self.peso)
 
# Clase heredada. Hereda todos los atributos de la clase 'Padre' y se le añaden los suyos propios. 
class PerroAsistencia (Perro):
    def __init__  (self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
    
    def __str__ (self):
        return "Perro de asistencia de {}".format(self.amo)
    
    def pasear (self):
        print (" {} ayuda a {} a pasear".format(self.nombre, self.amo))
        
    def ladrar (self):
        if self.trabajando:
            print ("shhh, no puedo ladrar")
        else:
            Perro.ladrar (self)
    
    def trabajando (self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor