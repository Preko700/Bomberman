from PIL import ImageTk
from tkinter import *
from juego import Customization
import winsound
import threading
import os
import time
#Funcion que usa la libreria winsound para reproducir y parar los sonidos
def play_song():
    winsound.PlaySound("Sounds\menu.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def stop_song():
    winsound.PlaySound(None, winsound.SND_PURGE)

def ReproducirSonido(name):
    winsound.PlaySound(name,winsound.SND_FILENAME)

def LoadImage(nombre): # Funcion para cargar las imagenes
    ruta = os.path.join('Bomberman Images',nombre) # se define la ubicación de la imagen
    imagen = ImageTk.PhotoImage(file=ruta)
    return imagen #Devuelve la imagen

def Animation(contador, img_label):
    nombre = "frame_" + str(contador) + "_delay-0.1s.jpg" 
    img = LoadImage(nombre)
    img_label.config(image=img)  # Actualiza la imagen en la etiqueta
    contador += 1
    time.sleep(0.05)
    Animation(contador, img_label)

class BotonAnimado:
    def __init__(self, parent):
        self.parent = parent
        self.imagen1 = LoadImage("speaker.jpg")
        self.imagen2 = LoadImage("speakerX.jpg")
        self.boton = Button(parent, image=self.imagen1, command=self.ChangeImage)
        self.boton.pack()
        self.estado = 1

    def ChangeImage(self):
        if self.estado == 1:
            self.boton.config(image=self.imagen2)
            self.estado = 2
            stop_song()
        else:
            self.boton.config(image=self.imagen1)
            self.estado = 1
            play_song()

def settings():
    Settings=Toplevel(bg="#459DFF")
    Settings.title("Configuración")# titulo de la ventana
    Settings.minsize(500,500)# tamaño de ventana
    Settings.resizable(width=False,height=False) # si se puede hacer pequña o grande
    txt=Label(Settings,text="【C】【o】【n】【f】【i】【g】【u】【r】【a】【c】【i】【ó】【n】",bg="#459DFF",font=("Arial",10))
    txt.place(x=25,y=10)
    txt1=Label(Settings,text="ıllıllı⭐🌟 H͙a͙b͙i͙l͙i͙t͙a͙r͙/D͙e͙s͙a͙c͙t͙i͙v͙a͙r͙ C͙a͙n͙c͙i͙o͙n͙e͙s͙ 🌟⭐ıllıllı",bg="#459DFF",font=("Arial",10))
    txt1.place(x=25,y=50)
    i=LoadImage("info.jpg")
    info=Button(Settings,image=i,command=Info)
    info.place(x=450,y=450)
    boton_animado = BotonAnimado(Settings)
    boton_animado.boton.place(x=50, y=75)
    Settings.mainloop()

def Instrucciones():
    intrucciones = Toplevel()
    intrucciones.minsize(1200,800)# tamaño de root
    intrucciones.resizable(width=False,height=False)# no se hace mas pequña
    intrucciones.title("Instrucciones")
    instrucciones_label = Label(intrucciones, text= "Instrucciones del juego", font=("Helvetica", 18, "bold"), fg="navy")
    instrucciones_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    text = """Este juego está inspirado en Bomberman\n
    Tiene una jugabilidad muy semejante\n
    Está constituido por 3 niveles, para pasar cada nivel usted deberá ir destruyendo con las bombs los muros,\n 
    en alguno de ellos estará escondida una llave que le permitirá pasar al siguiente nivel\n
    Debes tener cuidado habrán enemigos que te harán daño al igual que las bombs, toma distancia\n
        Las teclas necesarias para el juego son:\n
        *W Para moverse hacia arriba\n
        *S para moverse hacia abajo\n
        *A para moverse hacia la izquierda\n
        *D para moverse hacia la derecha\n
        *Espacio coloca bombs\n
    -Con las bombs podrá ir destruyendo a sus enemigos y sumando más puntos"""
    instrucciones_label = Label(intrucciones, text=text, font=("Fixedsys", 14, "bold"), fg="navy")
    instrucciones_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    Continuar = Button(intrucciones, text="CONTINUAR??", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=Game)
    Continuar.place(relx=0.5, rely=0.8, anchor=CENTER)

def Info():
    info=Toplevel(bg="white")# se crea la ventana, top level porque es una ventana informativa
    info.title("Informacio sobre: Adrian Monge") # titulo de la ventana
    info.minsize(1024,900)# tamaño de ventana
    info.resizable(width=NO,height=NO) # Tamaño Reajustable? No
    Title=Label(info,text="DATOS GENERALES DEL AUTOR",bg="white",fg="black")#Titulo con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro  
    Title.place(x=400,y=50)#ubicacion del titulo
    Name=Label(info,text="Nombre: Adrián Monge Mairena",bg="white",fg="Black")#Variable que muestra un nombre con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro  
    Name.place(x=50,y=75)#Ubicacion de la variable "Name
    Age=Label(info,text="Edad: 21",bg="white",fg="Black")#Variable que muestra una edad con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro  
    Age.place(x=50,y=100)#ubicacion de la variable Age
    txtAsignatura=Label(info,text='Asignatura: Introducción a la programación (CE1101)')
    txtAsignatura.place(x=50,y=150)
    txtCarrera=Label(info,text='Carrera: Ingeniería en Computadores')
    txtCarrera.place(x=50,y=200)
    txtEntorno=Label(info,text='Entorno Académico: Instituto Tecnológico de Costa Rica')
    txtEntorno.place(x=50,y=250)
    txtAño=Label(info,text='Año: 2024')
    txtAño.place(x=50,y=350)
    txtProfesor=Label(info,text='Profesor: Jason Leiton Jimenez')
    txtProfesor.place(x=50,y=300)
    txtCountry=Label(info,text='Pais de Produccion: Costa Rica')
    txtCountry.place(x=50,y=400)
    txtversion=Label(info,text='Version: 0.1')
    txtversion.place(x=470,y=800)
    identF=LoadImage("identF.jpg")
    IFlabel=Label(info,image=identF)
    IFlabel.place(x=50,y=425)
    identT=LoadImage("idenT.jpg")
    ITLabel=Label(info,image=identT)
    ITLabel.place(x=350,y=425)
    imagen3=LoadImage("Selfie1.jpg")# carga la imagen s
    selfi=Label(info,image=imagen3)# etiqueta que va a contener la imagen
    selfi.place(x=600,y=75)# posicion de la imagen
    info.mainloop()

def Leaderboard():
    # Función para abrir la ventana de mejores puntajes
    def LeaderAux(level, root):
        mejores_puntajes_window_aux = Toplevel(root)
        mejores_puntajes_window_aux.title(f"Mejores Puntajes nivel {level}")
        def ReedFile(level):
            ruta=f"{level}.txt"
            archivo=open(ruta) # coloca el contenido en memoria
            contenido=archivo.readlines()
            archivo.close()
            return contenido 
        def Top(Registros, res):
            if Registros == []:
                res = res.split("@")
                #return f"El registro con más edad es: {res[0]+" "+res[1]} con {res[2][:len(res[2])-1]} años"
                return res
            elif int(Registros[0].split("@")[1][:len(Registros[0])-1])>int(res.split("@")[1]):
                return Top(Registros[1:], Registros[0])
            else:
                return Top(Registros[1:], res)
        content = ReedFile(level)
        def show(contenido,allregistrys, row):
            if contenido == []:
                return
            else:
                registro = contenido[0].split("@")
                #registro = Edad_Mayor(allregistrys, contenido[0])
                print(registro)
                registry= Label(mejores_puntajes_window_aux,text=f"Nombre: {registro[0]} Puntaje: {registro[1]}", relief="raised", bd=4, font=("Fixedsys", 20, "normal"))
                registry.grid(row=row, column=0)
                show(contenido[1:],allregistrys, row+1)

        show(content,content,0)
    mejores_puntajes_window = Toplevel(Menu)
    mejores_puntajes_window.title("Mejores Puntajes")
    PuntajesNivel1 = Button(mejores_puntajes_window, text="Nivel 1", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=lambda:LeaderAux(1,mejores_puntajes_window))
    PuntajesNivel1.grid(row=0, column=0)
    PuntajesNivel2 = Button(mejores_puntajes_window, text="Nivel 2", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=lambda:LeaderAux(2,mejores_puntajes_window))
    PuntajesNivel2.grid(row=1, column=0)
    PuntajesNivel3 = Button(mejores_puntajes_window, text="Nivel 3", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=lambda:LeaderAux(3,mejores_puntajes_window))
    PuntajesNivel3.grid(row=2, column=0)
    


    # Aquí puedes agregar los widgets y funcionalidades de la ventana de mejores puntajes

def Game():

    Customization(Menu)

# Configuración de la ventana principal
Menu = Tk()# se crea la ventana
Menu.title("Bomberman")# titulo de la ventana
Menu.minsize(1024,945)# tamaño de ventana
Menu.resizable(width=False,height=False) # si se puede hacer pequña o grande
Menu.iconbitmap("Bomberman Images\ico.ico")
MenuImg = LoadImage("menu.jpg")# carga la imagen
MenuScreen=Label(Menu, image=MenuImg) # etiqueta que va a contener la imagen
MenuScreen.place(x=0,y=0)# posicion de la imagen
SettingsIMG=LoadImage("setting1.jpg")
LeadersIMG=LoadImage("leader1.jpg")
PlayIMG=LoadImage("start.jpeg")
contador=0
img_label = Label(Menu)
img_label.place(x=200, y=70)
boton_configuracion = Button(Menu,command=settings,image=SettingsIMG)
boton_configuracion.place(x=900,y=70)
boton_mejores_puntajes = Button(Menu,command=Leaderboard,image=LeadersIMG)
boton_mejores_puntajes.place(x=25,y=70)
boton_inicio = Button(Menu,command=Instrucciones,image=PlayIMG)
boton_inicio.place(x=350,y=800)
hilo2 = threading.Thread(target=Animation,args=(contador,img_label))
hilo1 = threading.Thread(target=play_song)
hilo1.start()
hilo2.start()
Menu.mainloop()
