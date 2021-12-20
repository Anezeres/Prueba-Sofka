import math
import random


class Jugador:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos

    def getNombre(self):
        return self.nombre

    def getPuntos(self):
        return self.puntos

    def agregarPuntos(self):
        self.puntos += 1000 


nombre = input("¿Cual es tu nombre jugador?: ")
jugador = Jugador(nombre,0)
print("Bienvenido ",jugador.getNombre(), " a nuestro cuestionario")
print("¿Que tan fan eres de las peliculas de Marvel?")
ronda1()


def siguienteRonda(numero):
    if numero == 1:
        ronda1()
        pass 
    elif numero == 2:
        ronda2()
        pass
    elif numero == 3:
        ronda3()
        pass
    elif numero == 4:
        ronda4()
        pass
    elif numero == 6:
        pass
    else:
        ronda5()
        pass

def respuestaCorrecta(respuesta,respuestaUsuario,rondaSiguiente):
    if (respuesta == respuestaUsuario):
        print("¡Respuesta Correcta!")
        jugador.agregarPuntos()
        print("Excelente!, ganaste 1000 puntos!, actualmente tienes: ", jugador.getPuntos())
        siguienteRonda(rondaSiguiente)
        pass

    elif (respuesta =! respuestaUsuario):
        print("Lo siento, la respuesta no es correcta") 
        print("El concurso ha finalizado.")
        print("Puntos totales alcanzador: ",jugador.getPuntos())
        intento = int(input("¿Quieres volver a Jugar? Si = 1, No = 2:"))

        if (intento == 1):
            ronda1()
        else:
            print("Está bien, Vuelva pronto!")

    else: 
        print("Lo siento, el valor ingresado no corresponde a una respuesta")
        print("Ingrese Nuevamente su Respuesta")

        respuestaUsuario2 = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta(respuesta,respuestaUsuario2,rondaSiguiente)



def ronda1():
    print("###############################")
    print("#Bienvenido a la Primera Ronda#")
    print("###############################")
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("1. ¿En qué año se estrenó la primera película de Iron Man, que lanzó el Marvel Cinematic Universe?")
        print("A) 2005")
        print("B) 2008")
        print("C) 2010")
        print("D) 2012")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("B",respuestaUsuario2,2)

        pass
    elif (pregunta == 2):
        print("1. ¿Cómo se llama el martillo de Thor?")
        print("A) Vanir")
        print("B) Mjolnir")
        print("C) Aesir")
        print("D) Norn")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("B",respuestaUsuario2,2)
        pass
    elif (pregunta == 3):
        print("1. ¿Cuál es el verdadero nombre de la Bruja Escarlata?")
        print("A) Wanda")
        print("B) Scarlett")
        print("C) Natalie")
        print("D) Hayley")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,2)
        pass
    elif (pregunta == 4):
        print("1. ¿De qué está hecho el escudo del Capitán América?")
        print("A) Adamantium")
        print("B) Vibranio")
        print("C) Prometeo")
        print("D) Carbonadio")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("B",respuestaUsuario2,2)
        pass
    else:
        print("1. Los Flerkens son una raza de alienígenas extremadamente peligrosos que se parece a qué.")
        print("A) Gatos")
        print("B) Patos")
        print("C) Reptiles")
        print("D) Mapaches")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,2)
        pass


    pass

def ronda2():
    print("###############################")
    print("#Bienvenido a la Segunda Ronda#")
    print("###############################")
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("2. ¿Cuál es el verdadero nombre de la Pantera Negra?")
        print("A) N'Jobu")
        print("B) T'Challa")
        print("C) M'Baku")
        print("D) N'Jadaka")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("B",respuestaUsuario2,3)
        pass
    elif (pregunta == 2):
        print("2. ¿Cuál es la raza alienígena que Loki envía para invadir la Tierra en The Avengers?")
        print("A) El chitauri")
        print("B) Los skrulls")
        print("C) El kree")
        print("D) Los flerkens")

                           
        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,3)
        pass
    elif (pregunta == 3):
        print("2. ¿Qué nombre falso usa Natasha cuando conoce a Tony por primera vez?")
        print("A) Natalie Rushman")
        print("B) Natalia Romanoff")
        print("C) Nicole Rohan")
        print("D) Naya Rabe")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,3)
        pass
    elif (pregunta == 4):
        print("2. ¿Sobre qué ciudad recuerdan a menudo Hawkeye y Black Widow?")
        print("A) Budapest")
        print("B) Praga")
        print("C) Estanbul")
        print("D) Jugos")


        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,3)
        pass
    else:
        print("2. ¿A quién sacrifica el Titán Loco para adquirir la Piedra del Alma?")
        print("A) Nebula")
        print("B) Fauces de ébano")
        print("C) Obsidiana de sacrificio")
        print("D) Gamora")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("D",respuestaUsuario2,3)
        pass

    pass

def ronda3():
    print("###############################")
    print("#Bienvenido a la Tercera Ronda#")
    print("###############################")
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("3. ¿Qué dice el Soldado de Invierno después de que Steve lo reconoce por primera vez?")
        print("A) '¿Quién diablos es Bucky?'")
        print("B) '¿Te conozco?'")
        print("C) 'El se fue.'")
        print("D) ¿Qué dijiste?")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,4)
        pass
    elif (pregunta == 2):
        print("3. ¿Cuáles fueron los tres elementos que Rocket afirma que necesita para escapar de la prisión?")
        print("A) Una tarjeta de seguridad, un tenedor y un monitor de tobillo.")
        print("B) Una banda de seguridad, una batería y una pierna protésica.")
        print("C) Un par de binoculares, un detonador y una prótesis de pierna.")
        print("D) Un cuchillo, cables y la cinta de mezcla de Peter.")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("B",respuestaUsuario2,4)
        pass
    elif (pregunta == 3):
        print("3. ¿Qué palabra pronuncia Tony que hace que Steve diga 'Lenguaje'? ")
        print("A) ¡Mierda!")
        print("B) ¡Estúpido!")
        print("C) ¡Idiota!")
        print("D) ¡Diablos!")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,4)
        pass
    elif (pregunta == 4):
        print("3. ¿Quién es asesinado por Loki en los Vengadores?")
        print("A) Maria Hill")
        print("B) Nick Fury")
        print("C) Agente coulson")
        print("D) Doctor Erik Selvig")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("C",respuestaUsuario2,4)
        pass
    else:
        print("3. ¿Quién es la hermana de Black Panther?")
        print("A) Shuri")
        print("B) Nakia")
        print("C) Ramonda")
        print("D) Okoye")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,4)
        pass

    pass

def ronda4():
    print("##############################")
    print("#Bienvenido a la Cuarta Ronda#")
    print("##############################")
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("4. ¿De qué hito rescata Peter Parker a sus compañeros de clase en Spider-Man: Homecoming?")
        print("A) Monumento de Washington")
        print("B) Estatua de la Libertad")
        print("C) Mount Rushmore")
        print("D) Puente Golden Gate")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,5)
        pass
    elif (pregunta == 2):
        print("4. ¿Qué canción baila Baby Groot al final del primer Guardian of the Galaxy?")
        print("A) 'Cherry Bomb' - The Runaways")
        print("B) 'Ain't No Mountain High Enough' - Marvin Gaye y Tammi Terrell")
        print("C) 'Te quiero de vuelta' - The Jackson 5")
        print("D) 'Enganchado a un sentimiento' - Voidoid")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("C",respuestaUsuario2,5)
        pass
    elif (pregunta == 3):
        print("4. ¿Qué tipo de médico es Stephen Strange?")
        print("A) Neurocirujano")
        print("B) Cirujano cardiotoracico")
        print("C) Cirujano de trauma")
        print("D) Cirujano Plástico")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,5)
        pass
    elif (pregunta == 4):
        print("4. ¿Cuál es el verdadero nombre de Deadpool?")
        print("A) Dofinder Wilson")
        print("B) Wade Wilson")
        print("C) Ajax Wilson")
        print("D) Bob Wilson")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("B",respuestaUsuario2,5)
        pass
    else:
        print("4. ¿En qué película apareció The Aether por primera vez?")
        print("A) Thor: The Dark World")
        print("B) Thor: Ragnarok")
        print("C) Thor: Love and Thunder")
        print("D) Thor")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,5)
        pass

    pass

def ronda5():
    print("##############################")
    print("#Bienvenido a la Quinta Ronda#")
    print("##############################")
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("5. ¿Cuántas piedras infinitas hay?")
        print("A) 5")
        print("B) 6")
        print("C) 4")
        print("D) 7")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("B",respuestaUsuario2,6)
        pass
    elif (pregunta == 2):
        print("5. ¿Quién mató a los padres de Tony Stark?")
        print("A) Loki")
        print("B) Capitan America")
        print("C) El soldado de invierno")
        print("D) Hulk")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("C",respuestaUsuario2,6)
        pass
    elif (pregunta == 3):
        print("5. ¿Cuál es la única película de Marvel que no tiene una escena posterior al crédito?")
        print("A) Avengers: Infinity War")
        print("B) Thor: Ragnarok")
        print("C) Avengers")
        print("D) Avengers: Endgame")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("D",respuestaUsuario2,6)
        pass
    elif (pregunta == 4):
        print("5. ¿Qué especie se revela que es Loki?")
        print("A) Centaurians")
        print("B) Gigante de escarcha")
        print("C) Luphomoids")
        print("D) Atlanteans")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("B",respuestaUsuario2,6)
        pass
    else:
        print("5. ¿Cuál es el nombre del universo microscópico al que viaja Ant-Man cuando se vuelve subatómico?")
        print("A) Reino cuántico")
        print("B) Reino Microscópico")
        print("C) Reino Molecular")
        print("D) Reino Diminuto")

        respuestaUsuario = input("Ingrese su respuesta A,B,C o D: ")
        respuestaCorrecta("A",respuestaUsuario2,6)
        pass


    pass


print("Los puntos totales que conseguiste= ", jugador.getPuntos())