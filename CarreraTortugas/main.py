import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'black', 'yellow', 'white')

#Definimos la pantalla
    
    def __init__ (self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startline = -width/2 + 20
        self.__finishline = width/2 - 20
        
        self._createRunners()


# Creamos las 4 tortugas

    def _createRunners (self):   
       for i in range (4):
            new_turtle = turtle.Turtle()
            new_turtle.color (self.__colorTurtle[i])
            new_turtle.shape ('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startline, self.__posStartY[i])
            
            self.corredores.append (new_turtle)


# Definimos como va a ser la carrera

    def competir (self):
        
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint (1,6)
                tortuga.fd (avance)
                
                if tortuga.position()[0] >= self.__finishline:
                    hayGanador = True
                    print ("la tortuga de color {} ha ganado".format(tortuga.color()[0]))
                
                
                
            


if __name__ == '__main__':
    circuito = Circuito (640, 480)
    circuito.competir()