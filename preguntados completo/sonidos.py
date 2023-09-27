from variables import sonido_correcto, sonido_incorrecto, sonido_acierto_consecutivo, sonido_ganar, sonido_perder, sonido_botones, sonido_fondo

def configuracion_sonido(sonido_general:bool) -> None:
    '''
    configura los niveles de volumen de distintos sonidos del juego, dependiendo del estado del sonido general.

    Args:
        sonido_general (bool): indica si el sonido general esta habilitado o deshabilitado

    Return:
        None

    '''
    if sonido_general:
        sonido_correcto.set_volume(0.4)
        sonido_incorrecto.set_volume(0.4)
        sonido_acierto_consecutivo.set_volume(0.4)
        sonido_ganar.set_volume(0.12)
        sonido_perder.set_volume(0.12)
        sonido_botones.set_volume(0.12)
        sonido_fondo.set_volume(0.16)   
    else:
        sonido_correcto.set_volume(0)
        sonido_incorrecto.set_volume(0)
        sonido_acierto_consecutivo.set_volume(0)
        sonido_ganar.set_volume(0)
        sonido_perder.set_volume(0)
        sonido_botones.set_volume(0)
        sonido_fondo.set_volume(0)


def sonidos_final_ganar_perder(juego_terminado:bool, puntos_acumulados:int, bloqueo_ganar_perder:bool) -> bool:
    '''
    maneja la reproduccion de los sonidos finales del juego y actualiza los estados de bloqueo para no repetirlo en bucle.

    Args:
        juego_terminado (bool): indica si el juego ha terminado y el comienzo de la reproduccion
        Puntos_ganar (int): Puntos acumulados por el jugador.
        Bloqueo_ganar_perder: bloque la reproduccion en bucle del sonido ganar o el sonido perder
    
    Return:
        bloqueo_ganar_perder(bool): estado de bloqueo de reproduccion de sonidos

    '''
    if juego_terminado:
        if puntos_acumulados >= 100 and not bloqueo_ganar_perder:
            sonido_fondo.pause()
            sonido_ganar.play()
            bloqueo_ganar_perder = True
        elif not bloqueo_ganar_perder:
            sonido_fondo.pause()
            sonido_perder.play()
            bloqueo_ganar_perder = True

    return bloqueo_ganar_perder
