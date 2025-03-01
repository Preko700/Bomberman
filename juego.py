
from tkinter import *
from PIL import Image, ImageTk
import time
import threading
import random
import datetime
import time
import winsound
import pygame

'''
Funcion beta para cargar las imagenes

def initialize_sprites(cellSize=80):
    # Definimos los sprites para las bombas, muros, jugadores, fuego y power-ups
    BOMB = resizedImage("Sprites/Bomb/Bomb_f01.png", width=cellSize, height=cellSize)
    WALL = {
        IMMUNE: resizedImage("Sprites/Blocks/SolidBlock.png", width=cellSize, height=cellSize),
        BREAKABLE: resizedImage("Sprites/Blocks/ExplodableBlock.png", width=cellSize, height=cellSize),
    }
    PLAYER = {
        0: {
            UP: resizedImage("Sprites/Bomberman/0/Up.png", width=cellSize, height=cellSize),
            DOWN: resizedImage("Sprites/Bomberman/0/Down.png", width=cellSize, height=cellSize),
            RIGHT: resizedImage("Sprites/Bomberman/0/Right.png", width=cellSize, height=cellSize),
            LEFT: resizedImage("Sprites/Bomberman/0/Left.png", width=cellSize, height=cellSize),
        },
        1: {
            UP: resizedImage("Sprites/Bomberman/1/Up.png", width=cellSize, height=cellSize),
            DOWN: resizedImage("Sprites/Bomberman/1/Down.png", width=cellSize, height=cellSize),
            RIGHT: resizedImage("Sprites/Bomberman/1/Right.png", width=cellSize, height=cellSize),
            LEFT: resizedImage("Sprites/Bomberman/1/Left.png", width=cellSize, height=cellSize),
        },
        2: {
            UP: resizedImage("Sprites/Bomberman/2/Up.png", width=cellSize, height=cellSize),
            DOWN: resizedImage("Sprites/Bomberman/2/Down.png", width=cellSize, height=cellSize),
            RIGHT: resizedImage("Sprites/Bomberman/2/Right.png", width=cellSize, height=cellSize),
            LEFT: resizedImage("Sprites/Bomberman/2/Left.png", width=cellSize, height=cellSize),
        },
        3: {
            UP: resizedImage("Sprites/Bomberman/3/Up.png", width=cellSize, height=cellSize),
            DOWN: resizedImage("Sprites/Bomberman/3/Down.png", width=cellSize, height=cellSize),
            RIGHT: resizedImage("Sprites/Bomberman/3/Right.png", width=cellSize, height=cellSize),
            LEFT: resizedImage("Sprites/Bomberman/3/Left.png", width=cellSize, height=cellSize),
        },
    }
    FIRE = resizedImage("Sprites/Flame/Flame_f00.png", width=cellSize, height=cellSize)
    POWERUPS = {
        BOMB_AMOUNT: resizedImage("Sprites/Powerups/BombPowerup.png", width=cellSize, height=cellSize),
        BOMB_RANGE: resizedImage("Sprites/Powerups/FlamePowerup.png", width=cellSize, height=cellSize),
        THROW_BOMB: resizedImage("Sprites/title_flat.jpg", width=cellSize, height=cellSize),
        KICK_BOMB: resizedImage("Sprites/title_flat.jpg", width=cellSize, height=cellSize),
        MOVEMENT_SPEED: resizedImage("Sprites/Powerups/SpeedPowerup.png", width=cellSize, height=cellSize),
    }

    return BOMB, WALL, PLAYER, FIRE, POWERUPS
'''

#Funcion para reproducir sonidos durante el juego
def play_sound(name):
    winsound.PlaySound(f".//Sounds//{name}.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

#Función que se despliega antes de iniciar con el primer nivel del juego
#Su funcionalidad se basa en la personalización del personaje y el nombre
def Customization(root):
    def boton_presionado(skin, name):
        root.iconify()
        winsound.PlaySound(None, winsound.SND_PURGE)
        winsound.PlaySound(".//Sounds//item Get.wav",winsound.SND_FILENAME)
        customizationscreen.destroy()
        Level(root,skin,3,30,180,name, 1)
        

    # Crear la ventana
    customizationscreen = Toplevel(root)
    customizationscreen.title("Personalización")
    customizationscreen.config(bg="black")
    customizationscreen.resizable(False, False)  # Hacer que la ventana no sea redimensionable
    customizationscreen.attributes('-topmost', True)  # Hacer que la ventana esté siempre arriba
    # Cargar las imágenes
    img1 = PhotoImage(file=r".\Bomberman Images\0-2-1.png")
    img2 = PhotoImage(file=r".\Bomberman Images\1-2-1.png")
    img3 = PhotoImage(file=r".\Bomberman Images\2-2-1.png")
    image = Image.open(f"Bomberman Images//0-2-1.png")  
    image = image.resize((44, 44))
    image = ImageTk.PhotoImage(image)

    #Colocar entrada de texto
    txt_name = Label(customizationscreen, text="Ingresa tu nombre y escoge a tu personaje",font=("Fixedsys", 20, "normal"))
    txt_name.grid(row=0, column=1)
    name = Entry(customizationscreen,font=("Fixedsys", 20, "normal"))
    name.grid(row=2, column=1)

    # Crear los botones con las imágenes
    btn1 = Button(customizationscreen, image=img1,command=lambda: boton_presionado(0, name.get()))
    btn2 = Button(customizationscreen, image=img2,command=lambda: boton_presionado(1, name.get()))
    btn3 = Button(customizationscreen, image=img3,command=lambda: boton_presionado(2, name.get() ))
    #Colocar Imágenes en los botones
    btn1.image = img1
    btn2.image = img2
    btn3.image = img3

    # Colocar los botones en la ventana
    btn1.grid(row=1, column=0, padx=10, pady=10)
    btn2.grid(row=1, column=1, padx=10, pady=10)
    btn3.grid(row=1, column=2, padx=10, pady=10)

    
    # Ejecutar el bucle principal de la aplicación
    customizationscreen.mainloop()



# Función que contiene toda la lógica aplicada al videojuego, está parametrizada para incrementar el nivel de dificultad en diferentes niveles
def Level(root, skin_code,lifes, bombs, duración, nombre, level):
    play_sound("Level Start")
    
     # Crear la ventana del juego
    window = Toplevel(root)
    window.title(f"Bomberman Nivel {level}")
    window.resizable(False, False)
    window.config(bg="Green")
    window.attributes('-topmost', True)
    print(nombre)
    
    #Generar referencias a las variables globales que se utilizarán a lo largo del código para acceder más fácilmente a ellas y ejecutar cambios entre funciones
    global key_found,bombas,score, enemy1, enemy2, tiempo, maze
    global fire, enemigo1, enemigo2,personaje
    global enemigoImagen1, enemigoImagen2,personaje_imagen,imagen_actual
    global posicionEnemigo1, posicionEnemigo2,posicion_puerta,posiciones_destructibles, posicion_llave, personaje_posicion,bomba_posicion
    global lista_explosiones, nivel
    global skin, finish, name, sound
    '''
    Matriz de beta
    ###########
    # xxxxxxx #
    #x#x#x#x#x#
    #xxxxxxxxx#
    #x#x#x#x#x#
    # xxxxxxx #
    ###########
    '''
    #Matriz que contiene el maze
    maze = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'C', 'X', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', ' ', ' ', 'Y', ' ', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X'],
        ['X', ' ', ' ', 'Y', ' ', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', 'P', 'X'],
        ['X', ' ', ' ', 'Y', ' ', ' ', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', ' ', 'Y', 'Y', 'X'],
        ['X', ' ', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', 'Y', 'Y', 'Y', 'X', 'Y', ' ', ' ', 'Y', ' ', ' ', 'Y', ' ', 'X', 'Y', 'Y', ' ', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', 'X', 'Y', ' ', 'X', ' ', ' ', 'X', 'Y', ' ', ' ', 'Y', 'Y', 'X', 'Y', 'Y', ' ', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', 'X', ' ', ' ', ' ', 'Y', ' ', ' ', 'Y', ' ', 'X', 'Y', 'Y', ' ', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', 'Y', 'X', 'Y', 'X', 'X', 'Y', ' ', 'Y', ' ', 'X', 'X', 'Y', 'X', 'X', 'X'],
        ['X', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', 'Y', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    posicionEnemigo1 = [8,17]
    posicionEnemigo2 = [14,12]
    posicion_puerta = []
    key_found = False
    #Imagen con la que iniciará el personaje al inicio del juego
    imagen_actual = "1"
    bomba_posicion=[]
    personaje_posicion = [2,1]
    posiciones_destructibles = []
    lifes = lifes
    bombas = bombs
    lista_explosiones = [] 
    enemy1 = True
    enemy2 = True
    score = 0
    tiempo = duración
    skin = skin_code
    finish = False
    name = nombre
    nivel = level
    #Funciones de jugador
    

    ################################################
    #Función para Escribir nuevos datos en los documentos, cada nivel tiene su propio documento
    def WriteFile(name, score, level):
        ruta=f"{level}.txt"
        archivo=open(ruta,"a")#a->append OJO
        archivo.write(f"{name}@{score}\n") # escribe el dato en el archivo
        archivo.close()

    #Código obtenido por Blackbox IA, extension para Visual Studio Code
    def countdown(duration):
        global finish, tiempo
        remaining_time = datetime.timedelta(seconds=duration)
        while remaining_time.total_seconds() > 0:
            if finish:
                break
            Time= Label(window,text=remaining_time, bg="#973118", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"))
            Time.place(relx=0.0, rely=0.0)
            time.sleep(1)
            remaining_time -= datetime.timedelta(seconds=1)
            tiempo -=1
        if not finish:
            GameOver(root)
        
    #Función que valida si el tiene mas de 0 lifes, si no se acaba el juego, llamando la funcion GameOver
    def lifes(lifes):
        if lifes <= 0:
            GameOver(root)
        else:
            Vida= Label(window,text=str(lifes)+"X", relief="raised", bd=4, font=("Fixedsys", 17, "normal"),background="#973118",fg="white")
            Vida.grid(row=1, column=0)
            window.update()
    #Función que revisa si el jugador tiene mas de 0 bombas, si no se acaba el juego, llamando la funcion GameOver
    def Bombas(bombas):
        if bombas <= 0:
            GameOver(root)
        else:
            Bomba= Label(window,text=str(bombas)+"X", relief="raised", bd=4, font=("Fixedsys", 17, "normal"),background="#973118",fg="white")
            Bomba.grid(row=1, column=2)
            window.update()
    
    #Funcion encargada de mostrar el tipico contador con los puntos
    def Points(puntos):
        global nivel
        score= Label(window,text="Puntuación"+str(puntos), relief="raised", bd=4, font=("Fixedsys", 20, "normal"),background="#973118",fg="white")
        score.place(relx=0.5, rely=0)
        #Label que muestra el nivel en el que esta el jugador
        nivel_label= Label(window,text="Nivel "+str(nivel), relief="raised", bd=4, font=("Fixedsys", 20, "normal"),background="#973118",fg="white")
        nivel_label.place(relx=0.8, rely=0)
    #Función para cargar imágen
    def cargarImagen(name, row, column):
        imagen = Image.open(f"Bomberman Images//{name}.png")  
        imagen = imagen.resize((44, 44))
        imagen = ImageTk.PhotoImage(imagen)
        label = Label(window, image=imagen,borderwidth=0, highlightthickness=0)
        label.image = imagen
        label.grid(row=row, column=column)

    #Función que verifica si se encontró la llave o no
    def find_key(row, column):
        global key_found, posicion_llave
        if row == posicion_llave[0] and column == posicion_llave[1]:
            maze[row][column] = "E"
            key_found = True

    #Función para el win y el game
    def YouWin(root):
        global score,bombas,tiempo, finish,sound
        sound.stop()
        play_sound("Level Complete")
        score+=tiempo+100*lifes+25*bombas
        window.destroy()
        def Continuar():
            gameOver.destroy()
            if level == 1:
                Level(root=root, skin_code=skin,lifes=2,bombs=25,duración=120, nombre=nombre, level=2)
            elif level == 2:
                Level(root=root, skin_code=skin,lifes=1,bombs=15,duración=90, nombre=nombre, level=3)
            else:
                play_sound("Ending Theme")
                Finish = Toplevel(root)
                Finish.resizable(False, False)
                Finish.title("NIVEL SUPERADO")
                Finish.config(bg="black")
                Title= Label(Finish,text=f"Has estado increible {nombre}", relief="raised", bd=4,borderwidth=0, highlightthickness=0,font=("Fixedsys", 32, "normal"),fg="green", bg="black")
                Title.grid(row=0, column=0)
                root.deiconify()
                Finish.mainloop()
        gameOver = Toplevel(root)
        gameOver.resizable(False, False)
        gameOver.title("FIN DEL JUEGO")
        gameOver.config(bg="black")
        Title= Label(gameOver,text=f"FELICIDADES {nombre} HAZ COMPLETADO EL NIVEL {level}", relief="raised", bd=4,borderwidth=0, highlightthickness=0,font=("Fixedsys", 32, "normal"),fg="yellow", bg="black")
        Title.grid(row=0, column=0)
        Score =Label(gameOver,text=f"TU PUNTAJE ES {score}", borderwidth=0, highlightthickness=0,relief="raised", bd=4, font=("Fixedsys", 32, "normal"),fg="yellow", bg="black")
        Score.grid(row=1, column=0) 
        WriteFile(name, score, level)

        Continuar = Button(gameOver, text="CONTINUAR??", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=Continuar)
        Continuar.grid(row=2, column=0)
        gameOver.mainloop()
    #Función para llamar a ventana una vez que se determina que el usuario no pasó el nivel
    def GameOver(root):
        global finish
        finish = True
        sound.stop()
        play_sound("Just Died")
        window.destroy()
        def Retry():
            gameOver.destroy()
            if level == 1:
                Level(root=root, skin_code=skin,lifes=3,bombs=50,duración=180, nombre=nombre, level=1)
            elif level == 2:
                Level(root=root, skin_code=skin,lifes=2,bombs=25,duración=120, nombre=nombre, level=2)
            else:
                Level(root=root, skin_code=skin,lifes=1,bombs=15,duración=90, nombre=nombre, level=3)
        gameOver = Toplevel(root)
        gameOver.resizable(False, False)
        gameOver.title("FIN DEL JUEGO")
        gameOver.config(bg="black")
        Title= Label(gameOver,text=f"TENEMOS UN PERDEDOR", relief="raised", bd=4, font=("Fixedsys", 32, "normal"),fg="Red", bg="black")
        Title.grid(row=0, column=0)
        Title2= Label(gameOver,text=f"VUELVE A INTENTARLO", relief="raised", bd=4, font=("Fixedsys", 32, "normal"),fg="Red", bg="black")
        Title2.grid(row=1, column=0)
        Reiniciar = Button(gameOver, text="REINTENTAR", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=Retry)
        Reiniciar.grid(row=2, column=0)
        gameOver.mainloop()

   ##################################################
   #Colisiones
   #Revisa si las cordenadas del jugador estan ya usadas
    def colisiones_personaje(row, column, row2, column2):
        global lifes
        if row == row2 and column == column2:
                play_sound("Enemy Dies")
                lifes -= 1
                lifes(lifes)
                mostrar_maze(0,0)
    def colisiones_bomba():
        global lista_explosiones, personaje_posicion, posicionEnemigo1, posicionEnemigo2,enemy1, enemy2,score
        if personaje_posicion in lista_explosiones:
            play_sound("Enemy Dies")
            lifes -= 1
            lifes(lifes)
           # mostrar_maze(0,0)
        if posicionEnemigo1 in lista_explosiones:
            play_sound("Enemy Dies")
            enemy1 = False
            score += 10
            enemigo1.destroy()
        if posicionEnemigo2 in lista_explosiones:
            play_sound("Enemy Dies")
            enemy2 = False
            score += 25
            enemigo2.destroy()

            
################################################################################
#Personaje principal
#Función para mostrar el personaje principal
    def desplegar_personaje():
        global personaje, personaje_imagen, skin
        personaje_imagen = Image.open(f"Bomberman Images//{skin}-2-{imagen_actual}.png")
        personaje_imagen = personaje_imagen.resize((40, 40))
        personaje_imagen = ImageTk.PhotoImage(personaje_imagen)
        personaje = Label(window, image=personaje_imagen, fg = "#408404", bg="#408404")
        personaje.grid(row=personaje_posicion[0], column=personaje_posicion[1])

    #Función para cambiar la imagen del personaje dependiendo de su movimiento
    def cambiarImagenPersonaje(categoría, imagen):
        global personaje_imagen, skin
        personaje_imagen = Image.open(f"Bomberman Images//{skin}-{categoría}-{imagen}.png")
        personaje_imagen = personaje_imagen.resize((40, 40))
        personaje_imagen = ImageTk.PhotoImage(personaje_imagen)
        personaje.config(image=personaje_imagen)
        window.update()

    def animacion_moveAux(cat_move):
        global imagen_actual
        if imagen_actual == "1":
            imagen_actual = "0"
        elif imagen_actual == "0":
            imagen_actual = "2"
        elif imagen_actual == "2":
            imagen_actual = "1"
        cambiarImagenPersonaje(cat_move,imagen_actual)
    '''
    Funcion Beta del iincializador del jugador con power ups
    def init_character(id, pos, config, sprites):
    Returns a character
    character = {
        "id": id,
        "pos" : pos,
        "powerups": config.INIT_POWERUPS.copy(),
        "lifes": config.LIFES,
        "direction": DOWN,
        "Label": cell_label(sprites.PLAYER[id][DOWN], pos),
    }
    return character
    '''
        
    #Identifica el movimiento y pasa su categoría de imagen correspondiente al movimiento
    def Movimiento(move):
        if move == "w":
            return animacion_moveAux("2")
        elif move == "d":
            return animacion_moveAux("0")
        elif move == "a":
            return animacion_moveAux("1")
        elif move == "s":
            return animacion_moveAux("2")
        
        if move == "space":
            return colocarBomba()
        
        '''
        Funcion beta del movimiento del personaje

        def bind_input(self):
        master.bind("w", lambda event: move_character(0, UP))
        master.bind("a", lambda event: move_character(0, LEFT))
        master.bind("s", lambda event: move_character(0, DOWN))
        master.bind("d", lambda event: move_character(0, RIGHT))
        master.bind("<space>", lambda event: place_bomb(0))

        def move_character(character_id, direction):
        Move the character
        if not characters[character_id]["lifes"]:
            return
        character = characters[character_id]
        character["direction"] = direction
        new_pos = (character["pos"][0] + direction[0], character["pos"][1] + direction[1])
        pos = character["pos"]
        if can_walk_to_spot(new_pos, character["powerups"][KICK_BOMB]):
            pos = new_pos
        character["pos"] = pos
        character["Label"].destroy()
        character["Label"] = cell_label(PLAYER[character_id][direction], character["pos"])
        if fires[pos]:
            damage_character(character)
        if powerups[pos]:
            pickup_powerup(character_id, pos)
        if bombs[pos]:
            kick_bomb(character_id, pos, direction)
        '''
    
    def mover_personaje(event):
        global personaje_posicion
        global lifes
        tecla = event.keysym
        nueva_fila, nueva_columna = personaje_posicion
        
        
        if tecla == "w":
            nueva_fila -= 1
        elif tecla == "s":
            nueva_fila += 1
        elif tecla == "a":
            nueva_columna -= 1
        elif tecla == "d":
            nueva_columna += 1
        Movimiento(tecla)
        if es_accesible_personaje(nueva_fila, nueva_columna):
            
            #Crear nueva posición, cambiando el valor de la variable global posición
            personaje_posicion = [nueva_fila, nueva_columna]
            #Actualizando la los valores de la posición del personaje
            personaje.grid(row=nueva_fila, column=nueva_columna)
#Funciones de explosión y esparcimiento de la bomba    
    def colocarBomba():
        global personaje_posicion
        global bomba_posicion
        global bomba, bombas
        cargarImagen("bomba0",personaje_posicion[0],personaje_posicion[1])
        bomba_posicion = [personaje_posicion[0],personaje_posicion[1]]
        bombas -=1
        Bombas(bombas)
        hilo_bomba_animación = threading.Thread(target=esparcimiento_fuego, args=(bomba_posicion[0],bomba_posicion[1] ))
        hilo_bomba_animación.start()
        bomba_posicion = []

    def esparcimiento_fuego(row, column):
        global lista_explosiones
        
        time.sleep(2)
        play_sound("Bomb Explodes")
        cargarImagen("Fuego0", row, column)
        lista_explosiones+=[[row, column]]
        accesible_bomba(row+1,column)
        accesible_bomba(row-1, column)
        accesible_bomba(row, column+1)
        accesible_bomba(row, column-1)
        time.sleep(0.5)
        colisiones_bomba()
        lista_explosiones=[]
        mostrar_maze(0,0) 
    def accesible_bomba(row, column):
        global lista_explosiones, key_found, posicion_llave, personaje_posicion
        if maze[row][column] not in ["X","C", "B"]:
            cargarImagen("Fuego0", row, column)
            lista_explosiones+=[[row, column]]
            maze[row][column] = " "
            find_key(row,column)     
    ################################################
    #Enemigos
    def desplegar_enemigos(Imagen,row, column,enemytype):
        global enemigo1, enemigo2,enemigoImagen1,enemigoImagen2, enemy1, enemy2
        
        if enemytype == 1 and enemy1:
            enemigoImagen1 = Image.open(f"Bomberman Images//{Imagen}.png")
            enemigoImagen1 = enemigoImagen1.resize((40, 40))
            enemigoImagen1 = ImageTk.PhotoImage(enemigoImagen1)
            enemigo1 = Label(window, image=enemigoImagen1, fg = "#408404", bg="#408404")
            enemigo1.grid(row=row, column=column)
        elif enemytype == 2:
            enemigoImagen2 = Image.open(f"Bomberman Images//{Imagen}.png")
            enemigoImagen2 = enemigoImagen2.resize((40, 40))
            enemigoImagen2 = ImageTk.PhotoImage(enemigoImagen2)
            enemigo2 = Label(window, image=enemigoImagen2, fg = "#408404", bg="#408404")
            enemigo2.grid(row=row, column=column)
    def Enemigos():
        global enemigo
        global posicionEnemigo1, posicionEnemigo2
        hilo1 = threading.Thread(target=desplegar_enemigos, args=("Enemigo1", posicionEnemigo1[0],posicionEnemigo1[1],1))
        hilo2 = threading.Thread(target=desplegar_enemigos, args=("Enemigo2", posicionEnemigo2[0],posicionEnemigo2[1],2))
        hilo1.start()
        hilo2.start()
    
    def MovimientoLaberinto(row, column,enemytype, direction):
        global posicionEnemigo1, posicionEnemigo2, enemigo1, enemigo2
        global personaje_posicion

        colisiones_personaje(personaje_posicion[0],personaje_posicion[1], row,column)

        if direction == "Up"and enemytype==1:
            if es_accesible_personaje(row+1, column):
                posicionEnemigo1 = [row+1, column]
                enemigo1.grid(row = row+1, column=column)
                window.update()
                time.sleep(0.5)
                MovimientoLaberinto(row+1,column, enemytype, "Up")
                print(posicionEnemigo1)
            else:
                MovimientoLaberinto(posicionEnemigo1[0], posicionEnemigo1[1], 1,"Down")
        elif direction == "Down":
            if es_accesible_personaje(row-1, column):
                posicionEnemigo1 = [row-1, column]
                enemigo1.grid(row = row-1, column=column)
                window.update()
                time.sleep(0.5)
                MovimientoLaberinto(row-1,column, enemytype, "Down")
                print(posicionEnemigo1)
            else:
                MovimientoLaberinto(posicionEnemigo1[0], posicionEnemigo1[1], 1,"Up")
        if direction == "Right" and enemytype==2:
            if es_accesible_personaje(row, column+1):
                posicionEnemigo2 = [row, column+1]
                enemigo2.grid(row = row, column=column+1)
                window.update()
                time.sleep(0.5)
                MovimientoLaberinto(row,column+1, enemytype,"Right")
                print(posicionEnemigo2)
            else:
                MovimientoLaberinto(posicionEnemigo2[0], posicionEnemigo2[1], 2,"Left")
        elif direction == "Left":
            if es_accesible_personaje(row, column-1):
                posicionEnemigo2 = [row, column-1]
                enemigo2.grid(row = row, column=column-1)
                window.update()
                time.sleep(0.5)
                MovimientoLaberinto(row,column-1, enemytype,"Left")
                print(posicionEnemigo2)
            else:
                MovimientoLaberinto(posicionEnemigo2[0], posicionEnemigo2[1], 2,"Right")
        
    def AnimacionEnemigos():
        global posicionEnemigo1,posicionEnemigo2

        enemy1 = threading.Thread(target=MovimientoLaberinto, args=(posicionEnemigo1[0], posicionEnemigo1[1], 1, "Up"))
        enemy2 = threading.Thread(target=MovimientoLaberinto, args=(posicionEnemigo2[0], posicionEnemigo2[1], 2, "Right"))
        enemy1.start()
        enemy2.start()

    #Funciones para la llave oculta

    def posicion_random_con_espacios():
        # Encontrar las posiciones con valor " " utilizando la función recursiva
        global posiciones_destructibles

        # Elegir una posición aleatoria de las posiciones con valor " "
        posicion_elegida = random.choice(posiciones_destructibles)
        print (posicion_elegida)
        return posicion_elegida




    ################################################
        
    def mostrar_maze(x=0, y=0):
        global posiciones_destructibles, maze_cargado, score,bombas
        global posicion_puerta
        # Si se determina que se ha recorrido todas las filas y todas las columnas, se depliegan el resto de imágenes 
        if x == len(maze)-1 and y == len(maze[0])-1:
            print(maze)
            desplegar_personaje()
            Enemigos()
            lifes(lifes)
            Bombas(bombas)
            Points(score)

        if maze[x][y] != ' ' or maze[x][y] == "Z":
            if maze[x][y]=="Y":
                posiciones_destructibles +=[[x,y]]
            if maze[x][y] == "Z":
                cargarImagen("Y", x, y)
            elif maze[x][y] == "E":
                cargarImagen("llave", x, y)
            elif maze[x][y] == "P":
                posicion_puerta = [x,y]
                cargarImagen("puerta", x, y)
            elif maze[x][y] == "B":
                posicion_puerta = [x,y]
                cargarImagen("bomba", x, y)
            elif maze[x][y] == "C":
                posicion_puerta = [x,y]
                cargarImagen("life", x, y)
            else:
                cargarImagen(maze[x][y], x, y)
            #ventana.update()
        elif maze[x][y] == " " or [x,y] in lista_explosiones:
            cargarImagen("pasto", x, y)
        window.update()    
        if y < len(maze[0]) - 1: #Eval+ua si la posición de la matriz [x][y] en y no ha llegado al límite
            mostrar_maze(x, y + 1)
        elif x < len(maze) - 1:#Eval+ua si la posición de la matriz [x][y] en x no ha llegado al límite
            mostrar_maze(x + 1, 0)
        
    #Código basado en ChatGPT
    def es_accesible_personaje(fila, columna):
        global posicion_puerta, bomba_posicion
        global key_found
        if fila < 0 or columna < 0 or fila >= len(maze) or columna >= len(maze[0]):
            return False
        elif fila == posicion_puerta[0] and columna == posicion_puerta[1] and key_found:
            YouWin(root)
        return maze[fila][columna] in [" ", "E"]  # Retorna True solo si el valor accedido en la matriz sea == " "
    mostrar_maze(0,0)
    posicion_llave = posicion_random_con_espacios()
    maze[posicion_llave[0]][posicion_llave[1]] = "Z"
    
   
        
    AnimacionEnemigos() 
    
    pygame.mixer.init()

    #Se debe utilizar la biblioteca de Pygame para el audio de fondo del videojuego para que no interfiera con los efectos de sonido
    sound = pygame.mixer.Sound(".//Sounds//Stage Theme.wav")
    sound.play()
    cuenta_regresiva = threading.Thread(target=countdown, args=(tiempo,))
    cuenta_regresiva.start()
    
    window.bind("<KeyPress>", mover_personaje)
    window.mainloop()

    '''
    Funcionalidades Extras
    powerups
    Constantes

INIT_POWERUPS = {
    BOMB_AMOUNT: 1,
    BOMB_RANGE: 2,
    THROW_BOMB: 0,
    KICK_BOMB: False,
    MOVEMENT_SPEED: 1,

    Funcion para cargar los powerups
    def place_powerup(pos):
    powerup_type = random.choice(POWERUPS)
    label = POWERUPS[powerup_type]
    powerup = {
        "Label": cell_label(label, pos),
        "type": powerup_type,
    }
    powerups[pos] = powerup

    Funcion para activar los powerups
    def pickup_powerup(character_id, pos):
    powerup_type = powerups[pos]["type"]
    if powerup_type == BOMB_AMOUNT:
        characters[character_id]["powerups"][BOMB_AMOUNT] += 1
    elif powerup_type == BOMB_RANGE:
        characters[character_id]["powerups"][BOMB_RANGE] += 1
    elif powerup_type == THROW_BOMB:
        characters[character_id]["powerups"][THROW_BOMB] = True
    elif powerup_type == KICK_BOMB:
        characters[character_id]["powerups"][KICK_BOMB] = True
    elif powerup_type == MOVEMENT_SPEED:
        new_movement_speed = characters[character_id]["powerups"][MOVEMENT_SPEED] + 1
        characters[character_id]["powerups"][MOVEMENT_SPEED] = min(3, new_movement_speed)
    remove_powerup(pos)
    '''

