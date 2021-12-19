import math
import random

print("Bienvenido a nuestro cuestionario")
print("¿Que tan fan eres de las peliculas de Marvel?")



def ronda1():
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("1. ¿En qué año se estrenó la primera película de Iron Man, que lanzó el Marvel Cinematic Universe?")
        print("A) 2005")
        print("B) 2008")
        print("C) 2010")
        print("D) 2012")
        pass
    elif (pregunta == 2):
        print("1. ¿Cómo se llama el martillo de Thor?")
        print("A) Vanir")
        print("B) Mjolnir")
        print("C) Aesir")
        print("D) Norn")
        pass
    elif (pregunta == 3):
        print("1. ¿Cuál es el verdadero nombre de la Bruja Escarlata?")
        print("A) Wanda")
        print("B) Scarlett")
        print("C) Natalie")
        print("D) Hayley")
        pass
    elif (pregunta == 4):
        print("1. ¿De qué está hecho el escudo del Capitán América?")
        print("A) Adamantium")
        print("B) Vibranio")
        print("C) Prometeo")
        print("D) Carbonadio")
        pass
    else:
        print("1. Los Flerkens son una raza de alienígenas extremadamente peligrosos que se parece a qué.")
        print("A) ")
        print("B) ")
        print("C) ")
        print("D) ")
        pass


    pass

def ronda2():
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("2. ¿Cuál es el verdadero nombre de la Pantera Negra?")
        print("A) ")
        print("B) ")
        print("C) ")
        print("D) ")
        pass
    elif (pregunta == 2):
        print("2. ¿Cuál es la raza alienígena que Loki envía para invadir la Tierra en The Avengers?")
        pass
    elif (pregunta == 3):
        print("2. ¿Qué nombre falso usa Natasha cuando conoce a Tony por primera vez?")
        pass
    elif (pregunta == 4):
        print("2. ¿Sobre qué ciudad recuerdan a menudo Hawkeye y Black Widow?")
        pass
    else:
        print("2. ¿A quién sacrifica el Titán Loco para adquirir la Piedra del Alma?")
        pass

    pass

def ronda3():
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("3. ¿Qué dice el Soldado de Invierno después de que Steve lo reconoce por primera vez?")
        pass
    elif (pregunta == 2):
        print("3. ¿Cuáles fueron los tres elementos que Rocket afirma que necesita para escapar de la prisión?")
        pass
    elif (pregunta == 3):
        print("3. ¿Qué palabra pronuncia Tony que hace que Steve diga 'Lenguaje'? ")
        pass
    elif (pregunta == 4):
        print("3. ¿Quién es asesinado por Loki en los Vengadores?")
        pass
    else:
        print("3. ¿Quién es la hermana de Black Panther?")
        pass

    pass

def ronda4():
    pregunta = random.randint(1,5)

    if (pregunta == 1):
        print("4. ¿De qué hito rescata Peter Parker a sus compañeros de clase en Spider-Man: Homecoming?")
        pass
    elif (pregunta == 2):
        print("4. ¿Qué canción baila Baby Groot al final del primer Guardian of the Galaxy?")
        pass
    elif (pregunta == 3):
        print("4. ¿Qué tipo de médico es Stephen Strange?")
        pass
    elif (pregunta == 4):
        print("4. ¿Cuál es el verdadero nombre de Deadpool?")
        pass
    else:
        print("4. ¿En qué película apareció The Aether por primera vez?")
        pass

    pass

def ronda5():
    pregunta = random.randint(1,5)
    print(pregunta)

    if (pregunta == 1):
        print("5. ¿Cuántas piedras infinitas hay?")
        pass
    elif (pregunta == 2):
        print("5. ¿Quién mató a los padres de Tony Stark?")
        pass
    elif (pregunta == 3):
        print("5. ¿Cuál es la única película de Marvel que no tiene una escena posterior al crédito?")
        pass
    elif (pregunta == 4):
        print("5. ¿Qué especie se revela que es Loki?")
        pass
    else:
        print("5. ¿Cuál es el nombre del universo microscópico al que viaja Ant-Man cuando se vuelve subatómico?")
        pass


    pass



ronda1()
