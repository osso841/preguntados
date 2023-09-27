import pygame
from constantes import *


pygame.init() 
pygame.mixer.init()
screen = pygame.display.set_mode(RESOLUCION_HD) 

#declaracion de variables
puntos_acumulados = 0
numero_pregunta = 0
intentos = 2
iniciar_juego = False
respuesta_correcta = False
juego_terminado = False

#contador sonidos
contador_aciertos_consecutivos = 0
primera_incorrecta = False

#declaracion variable cuando la respuesta es incorrecta
bloqueo_respuesta_a = False
bloqueo_respuesta_b = False
bloqueo_respuesta_c = False

#declaracion variable bloqueo respuesta
bloqueo_ganar_perder = False

#bandera sonido encendido apagado
sonido_general = True

#fuentes
font = pygame.font.SysFont("Arial Sparrow", 40)
font_final = pygame.font.SysFont("Arial", 90)

#imagenes pantalla inicio
boton_inicio = pygame.image.load("imagenes\\boton_comenzar.png")
rect_boton_inicio = pygame.Rect(440, 50, boton_inicio.get_width(), boton_inicio.get_height())
imagen_fondo_comienzo = pygame.image.load("imagenes\portada_inicio.png")   

#etiquetas e imagenes pantalla juego
imagen_fondo_juego = pygame.image.load("imagenes\\fondo_juego.png")
etiqueta_intentos = font.render('Intentos:', True, COLOR_NEGRO)
etiqueta_score = font.render('Score: ', True, COLOR_BLANCO)

#boton opciones
boton_seleccionado = None

#etiquetas e imagenes pantalla final
boton_reiniciar = pygame.image.load("imagenes\\boton_reiniciar.png")
rect_reiniciar = pygame.Rect(500, 500, boton_reiniciar.get_width(), boton_reiniciar.get_height())
etiqueta_juego_terminado = font_final.render('Juego Finalizado', True, COLOR_NEGRO)
imagen_fondo_final = pygame.image.load("imagenes\\fondo_final_juego.png")

#imagen boton pregunta 
boton_pregunta = pygame.image.load("imagenes\\boton_pregunta.png")
rect_pregunta = pygame.Rect(500, 65, boton_pregunta.get_width(), boton_pregunta.get_height())

#imagenes musica encendida - apagada
sonido_encendido = pygame.image.load("imagenes\sonido_encendido.png")
sonido_encendido = pygame.transform.scale(sonido_encendido, (70,70))
sonido_apagado = pygame.image.load("imagenes\sonido_apagado.png")
sonido_apagado = pygame.transform.scale(sonido_apagado, (70,70))
rect_mute_musica = pygame.Rect(20, 20, sonido_encendido.get_width(), sonido_encendido.get_height())


#sonidos ambiente
sonido_fondo = pygame.mixer.music
sonido_fondo.load("sounds\\ambiente.mp3")
sonido_fondo.play(-1)

#sonido opciones
sonido_correcto = pygame.mixer.Sound("sounds\correcto.mp3")
sonido_incorrecto = pygame.mixer.Sound("sounds\incorrecto.mp3")
sonido_acierto_consecutivo = pygame.mixer.Sound("sounds\\aciertos_consecutivos_1.mp3")

#sonido ganar, perder
sonido_ganar = pygame.mixer.Sound("sounds\\trumpet_winner.mp3")
sonido_perder = pygame.mixer.Sound("sounds\\trumpet_loose.mp3")

#sonido botones
sonido_botones = pygame.mixer.Sound("sounds\\botones.mp3")
