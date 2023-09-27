import pygame
from variables import screen, imagen_fondo_juego, imagen_fondo_final, imagen_fondo_comienzo #imagenes
from variables import etiqueta_juego_terminado, etiqueta_intentos, etiqueta_score #etiquetas
from variables import boton_reiniciar, boton_pregunta, boton_inicio #botones
from constantes import *

def pantalla_inicio() -> None:
    '''
    Muestra la pantalla de inicio del juego

    Args:
        None

    Return:
        None
    '''
    screen.blit(imagen_fondo_comienzo,(0,0)) #fondo comienzo
    screen.blit(boton_inicio, (440, 50))

#--------------------------------------------
def pantalla_juego(pregunta_juego:pygame.surface.Surface, opcion_a:pygame.surface.Surface, opcion_b:pygame.surface.Surface, opcion_c:pygame.surface.Surface, etiqueta_puntuacion:pygame.surface.Surface, etiqueta_intentos_cantidad:pygame.surface.Surface, respuesta_correcta:pygame.surface.Surface, intentos:pygame.surface.Surface) -> None:
    '''
    muestra la pantalla del juego con la pregunta y las opciones de respuesta.
    
    Args:
        pregunta_juego: Es la pregunta que se mostrará en la pantalla del juego.
        opcion_a, opcion_b, opcion_c: Son las opciones de respuesta que se mostrarán en la pantalla del juego.
        etiqueta_puntuacion, etiqueta_intentos_cantidad: Son etiquetas relacionadas con la puntuación y los intentos.
        respuesta_correcta: Indica si la respuesta dada es correcta.
        intentos: Indica la cantidad de intentos disponibles.

    Return:
        None
    '''
    #NOTE comienza la impresion en pantalla cuando se inicia la primera pregunta
    screen.blit(imagen_fondo_juego,(0,0)) #fondo de juego
    screen.blit(boton_pregunta, (500,65))
    screen.blit(boton_reiniciar,(500,500))
    screen.blit(etiqueta_score, (900, 570))
    screen.blit(etiqueta_intentos, (80, 650))
    screen.blit(etiqueta_intentos_cantidad, (220, 650))
    screen.blit(etiqueta_puntuacion, (1000, 570))
    screen.blit(pregunta_juego, (80, 302))

    #NOTE bloquea la impresion en pantalla de las preguntas cuando se agotan los intentos o cuando la respuesta es correcta
    if not respuesta_correcta and intentos > 0:
        screen.blit(opcion_a, (80, 375))
        screen.blit(opcion_b, (350, 375))
        screen.blit(opcion_c, (620, 375))   

#--------------------------------------------
def pantalla_final_score(puntos_acumulados:int, font_final:pygame.font.Font) -> None:
    '''
    mostrar la pantalla final del juego, donde se presenta la puntuacion acumulada

    args:
        puntos_acumulados: Es la puntuación total acumulada durante el juego.
        font_final: Es la fuente que se utilizará para mostrar la puntuación.

    Return:
        None
    '''

    screen.blit(imagen_fondo_final, (0,0)) #fondo Fin
    screen.blit(boton_reiniciar,(500,500)) ###################
    screen.blit(etiqueta_juego_terminado, (300,100))
    screen.blit(font_final.render('Puntuacion Total: ', True, COLOR_BLANCO), (200, 315))
    screen.blit(font_final.render(str(puntos_acumulados), True, COLOR_BLANCO), (850, 315))
