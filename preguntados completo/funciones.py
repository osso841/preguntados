import pygame

def normalizacion_preguntas(lista_preguntado:list) -> list:
    '''
    normalizar una lista de preguntas en un formato específico.

    Args:
        lista_preguntado: Es una lista que contiene preguntas en un formato que debe ser normalizado.

    Return:
        list: lista de sublistas
    '''
    lista_preguntas = []

    for e_preguntas in lista_preguntado:
        if not isinstance(e_preguntas, dict) and not e_preguntas:
            return False
        
        pregunta = e_preguntas['pregunta']
        a = e_preguntas['a']
        b = e_preguntas['b']
        c = e_preguntas['c']
        respuesta = e_preguntas['correcta']
        lista_preguntas.append([pregunta, a, b, c, respuesta])

    return lista_preguntas


def renderizado_preguntas_opciones(lista:list, posicion:int, font:pygame.font.Font) -> tuple:
    '''
    renderiza las preguntas y opciones de respuesta en una fuente especifica.

    Args:
        lista: Es una lista que contiene la pregunta y sus opciones de respuesta.
        posicion: Es un entero que indica la posición de la pregunta en la lista.
        font: Es un objeto de tipo pygame.font.Font que se utilizará para renderizar el texto.

    Return:
        Tupla: devuelve una colleccion de 4 elementos que representan:
            - pregunta_juego : etiqueta que corre la pregunta
            - opcion_a : etiqueta de la primera respuesta
            - opcion_b : etiqueta de la segunda respuesta
            - opcion_c : etiqueta de la tercera respuesta

    '''


    pregunta_juego = font.render(lista[posicion][0], True, (255, 255, 255))
    opcion_a = font.render("a) " + lista[posicion][1], True, (255, 255, 255))
    opcion_b = font.render("b) " + lista[posicion][2], True, (255, 255, 255))
    opcion_c = font.render("c) " + lista[posicion][3], True, (255, 255, 255))
    
    return pregunta_juego, opcion_a, opcion_b, opcion_c


def sumar_puntos(puntos:int) -> tuple:
    '''
    funcion que suma puntos a una variable y retorna una tupla de puntos y un estado

    Args:
        puntos: es un numero entero que representa la puntuacion actual

    Return:
        int: retorna los enteros actualizados
        bool: devuelve un estado booleano

    '''
    puntos += 10
    return puntos, True


def opcion_incorrecta(intentos:int) -> tuple:
    """
    Decrementa el número de intentos y devuelve una tupla indicando que la respuesta es incorrecta.

    Args:
        intentos (int): El número actual de intentos.

    Returns:
        tuple: Una tupla que contiene el nuevo número de intentos y un estado.

    """
    intentos -= 1
    return intentos, True


def contador_aciertos_sonido(primera_incorrecta:bool, contador_aciertos:int, sonido_correcto:pygame.mixer.Sound, sonido_acierto_consecutivo:pygame.mixer.Sound) -> int:
    """
    Cuenta los aciertos y reproduce el sonido correspondiente.

    Args:
        primera_incorrecta (bool): Indica si es el primer intento.
        contador_aciertos (int): Número actual de aciertos consecutivos.
        sonido_correcto (pygame.mixer.Sound): Sonido para aciertos.
        sonido_acierto_consecutivo (pygame.mixer.Sound): Sonido para aciertos consecutivos.

    Returns:
        int: Nuevo número de aciertos consecutivos.

    """
    if not primera_incorrecta:
        contador_aciertos += 1

    if contador_aciertos < 3:
        sonido_correcto.play()
    else:
        sonido_acierto_consecutivo.play()

    return contador_aciertos

