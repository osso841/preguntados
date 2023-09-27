import pygame

boton_inicio = pygame.image.load("imagenes\\boton_comenzar.png")
imagen_fondo_comienzo = pygame.image.load("imagenes\portada_inicio.png")
screen = pygame.display.set_mode([1280, 720])

rect_boton_inicio = pygame.draw.rect(screen, (255, 255, 255), (440, 50, boton_inicio.get_width(), boton_inicio.get_height()))                
screen.blit(imagen_fondo_comienzo,(0,0)) #fondo comienzo
screen.blit(boton_inicio, (440, 50))