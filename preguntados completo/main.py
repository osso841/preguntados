import pygame
from variables import *
from datos import lista
from funciones import *
from pantalla import *
from sonidos import *
from constantes import *

#creacion de una lista que contiene sublistas de las preguntas
lista_preguntas = normalizacion_preguntas(lista)

screen = pygame.display.set_mode(RESOLUCION_HD) 
running = True

while running:
    
    etiqueta_puntuacion = font.render(str(puntos_acumulados), True, COLOR_BLANCO)
    etiqueta_intentos_cantidad = font.render(str(intentos), True, COLOR_NEGRO)
    
    pregunta_juego, opcion_a, opcion_b, opcion_c = renderizado_preguntas_opciones(lista_preguntas, numero_pregunta, font)
    respuesta = lista_preguntas[numero_pregunta][4]

    screen.fill((100, 100, 100))
    
    #------------------------------- LISTA EVENTOS -------------------------------------------
    for event in pygame.event.get():

        #cerrar juego
        if event.type == pygame.QUIT:
            running = False

        #eventos Reiniciar, pregunta y opciones
        if event.type == pygame.MOUSEBUTTONDOWN:

            if not iniciar_juego: #NOTE click boton salir
                if rect_boton_inicio.collidepoint(event.pos):
                    sonido_botones.play()
                    iniciar_juego = True
            else:
                if not juego_terminado:
                    if rect_pregunta.collidepoint(event.pos): #NOTE click boton pregunta
                        sonido_botones.play()
                        intentos = 2              
                        primera_incorrecta = False
                        if numero_pregunta == len(lista_preguntas) - 1:
                            juego_terminado = True
                        else:
                            numero_pregunta += 1
                            respuesta_correcta = False
                            bloqueo_respuesta_a, bloqueo_respuesta_b, bloqueo_respuesta_c = (False, False, False)

                if rect_reiniciar.collidepoint(event.pos): #NOTE click boton Reiniciar
                    sonido_botones.play()
                    puntos_acumulados = 0
                    intentos = 2
                    numero_pregunta = 0
                    respuesta_correcta = False
                    bloqueo_respuesta_a, bloqueo_respuesta_b, bloqueo_respuesta_c = (False, False, False)
                    bloqueo_ganar_perder = False
                    juego_terminado = False
                    sonido_fondo.unpause()
                    sonido_ganar.stop()
                    sonido_perder.stop()
                    contador_aciertos_consecutivos = 0

                #NOTE valida las opciones cuando se inicia el programa, la respuesta es correcta o cuando no hay intentos
                if not respuesta_correcta and intentos > 0 and not juego_terminado:

                    if rect_opcion_a.collidepoint(event.pos): #NOTE click opcion A
                        if respuesta == 'a':
                            puntos_acumulados, respuesta_correcta = sumar_puntos(puntos_acumulados)
                            contador_aciertos_consecutivos = contador_aciertos_sonido(primera_incorrecta, contador_aciertos_consecutivos, sonido_correcto, sonido_acierto_consecutivo)

                        elif not bloqueo_respuesta_a:
                            intentos, bloqueo_respuesta_a = opcion_incorrecta(intentos)
                            sonido_incorrecto.play()
                            primera_incorrecta = True
                            contador_aciertos_consecutivos = 0

                    elif rect_opcion_b.collidepoint(event.pos): #NOTE click opcion B
                        if respuesta == 'b':
                            puntos_acumulados, respuesta_correcta = sumar_puntos(puntos_acumulados)
                            contador_aciertos_consecutivos = contador_aciertos_sonido(primera_incorrecta, contador_aciertos_consecutivos, sonido_correcto, sonido_acierto_consecutivo)

                        elif not bloqueo_respuesta_b:
                            intentos, bloqueo_respuesta_b = opcion_incorrecta(intentos)   
                            sonido_incorrecto.play()
                            primera_incorrecta = True
                            contador_aciertos_consecutivos = 0

                    elif rect_opcion_c.collidepoint(event.pos) :#NOTE click opcion C
                        if respuesta == 'c':
                            puntos_acumulados, respuesta_correcta = sumar_puntos(puntos_acumulados)
                            contador_aciertos_consecutivos = contador_aciertos_sonido(primera_incorrecta, contador_aciertos_consecutivos, sonido_correcto, sonido_acierto_consecutivo)

                        elif not bloqueo_respuesta_c:
                            intentos, bloqueo_respuesta_c = opcion_incorrecta(intentos)
                            sonido_incorrecto.play()
                            primera_incorrecta = True
                            contador_aciertos_consecutivos = 0

            if rect_mute_musica.collidepoint(event.pos):
                if sonido_general:
                    sonido_general = False
                else:
                    sonido_general = True

    #--------------------------------MUTEO SONIDOS - FINAL-----------------------------------------
    configuracion_sonido(sonido_general)
    bloqueo_ganar_perder = sonidos_final_ganar_perder(juego_terminado, puntos_acumulados, bloqueo_ganar_perder)
    #------------------------------------- OPCIONES -----------------------------------------------
    rect_opcion_a = pygame.Rect(80, 375, opcion_a.get_width(), opcion_a.get_height())
    rect_opcion_b = pygame.Rect(350, 375, opcion_b.get_width(), opcion_b.get_height())
    rect_opcion_c = pygame.Rect(620, 375, opcion_c.get_width(), opcion_c.get_height())
    #------------------------------------- PANTALLA -----------------------------------------------

    if not iniciar_juego:
        pantalla_inicio()
    elif not juego_terminado:
        pantalla_juego(pregunta_juego, opcion_a, opcion_b, opcion_c, etiqueta_puntuacion, etiqueta_intentos_cantidad, respuesta_correcta, intentos)
    else:
        pantalla_final_score(puntos_acumulados, font_final)

    if sonido_general:
        screen.blit(sonido_encendido, POS_BOTON_SONIDO)
    else:
        screen.blit(sonido_apagado, POS_BOTON_SONIDO)
    
    #----------------------------------------------------------------------------------------------
    pygame.display.flip()
pygame.quit() 