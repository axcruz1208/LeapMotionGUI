import sys
import threading
import time
import random

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, \
    QScrollArea, QDialog, QStackedWidget, QFrame, QSizePolicy

#import Leap

class QHSeperationLine(QFrame):
  '''
  a horizontal seperation line\n
  '''
  def __init__(self):
    super().__init__()
    self.setMinimumWidth(1)
    self.setFixedHeight(5)
    self.setStyleSheet("background: '#ECE5EC';" + "color: '#ECE5EC';")
    self.setFrameShape(QFrame.HLine)
    self.setFrameShadow(QFrame.Sunken)
    self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
    return

"""
Clase que nos crea una especie de tarjeta para almacenar las clases/tutorias/conferencia que vamos a tener
con una fotografía e información sobre las mismas
"""
class CardView(QWidget):
    def __init__(self, image,name, information, size, *args, **kwargs):
        super(CardView, self).__init__(*args, **kwargs)

        #Imagen con sus propiedades
        self.lessonImage = QPixmap(image)
        self.lessonImage = self.lessonImage.scaled(size, size)
        self.cardViewImage = QLabel()
        self.cardViewImage.setPixmap(self.lessonImage)

        #Información sobre la clase en cuestión
        self.name = QLabel(name)
        self.name.setFont(QFont('Times', int(size/10)))
        self.name.setStyleSheet("color: '#ECE5EC';" + "margin-right: 150px;")
        self.information = QLabel(information)
        self.information.setFont(QFont('Times', int(size/20)))

        #Layout vertical que almacena la información
        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.name)
        verticalLayout.addWidget(self.information)

        #Layout horizontal que almacena imagen y layout vertical
        layout = QHBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.cardViewImage)
        layout.addLayout(verticalLayout)

        self.setLayout(layout)

    def changeParameters(self, image, name, information, size):
            self.lessonImage.load(image)
            self.lessonImage = self.lessonImage.scaled(size, size)
            self.cardViewImage.setPixmap(self.lessonImage)
            self.name.setText(name)
            self.information.setText(information)


"""
Clase que crea el frame que muestra la ocupación de la biblioteca y comedor
"""
class OcupacionFrame(QDialog):
    def __init__(self):
        super(OcupacionFrame, self).__init__()

        # OcupacionFrame layouts
        box1 = QHBoxLayout()
        box2 = QHBoxLayout()
        verticalLayout = QVBoxLayout()


        #Logo
        #image = QPixmap("logo2.png")
        #logo = QLabel()
        #logo.setPixmap(image)
        #logo.setAlignment(QtCore.Qt.AlignCenter)
        #logo.setStyleSheet("margin-top: 20px;")

        #Label para el titulo
        titulo = QLabel()
        titulo.setText("Ocupación")
        titulo.setAlignment(QtCore.Qt.AlignCenter)
        titulo.setFont(QFont('SansSerif', 75))
        titulo.setStyleSheet("color: '#ECE5EC';")

        #Información sobre la ocupacion en la biblioteca
        name = QLabel("Biblioteca: ")
        name.setFont(QFont('Times', 35))
        name.setStyleSheet("color: '#ECE5EC';" + "margin-left: 150px;")
        information = QLabel(str(random.randint(0,200)))
        information.setFont(QFont('Times', 35/2))
        information.setStyleSheet("color: '#ECE5EC';" + "margin-right: 150px;")

        #Introducimos la ocupación de la biblioteca en el primer grid
        box1.addWidget(name)
        box1.addWidget(information)
        #box1.setStyleSheet("margin-right: 150px;" + "margin-left: 160px")

        #Información sobre la ocupacion en el comedor
        name = QLabel("Comedor: ")
        name.setFont(QFont('Times', 35))
        name.setStyleSheet("color: '#ECE5EC';" + "margin-left: 150px;")
        information = QLabel(str(random.randint(0,200)))
        information.setFont(QFont('Times', 35/2))
        information.setStyleSheet("color: '#ECE5EC';" + "margin-right: 150px;")

        #Introducimos la ocupación de la biblioteca en el primer grid
        box2.addWidget(name)
        box2.addWidget(information)
        #box2.setStyleSheet("margin-right: 150px;" + "margin-left: 160px")

        
        separator1 = QHSeperationLine()
        separator1.setStyleSheet("margin-right: 150px;" + "margin-left: 160px")
        separator2 = QHSeperationLine()
        separator2.setStyleSheet("margin-right: 150px;" + "margin-left: 160px")



        #Añadimos los distintos elementos s los layouts
        #grid.addWidget(button1, 0, 0)
        #grid.addWidget(button2, 0, 1)
        verticalLayout.addWidget(titulo)
        verticalLayout.addWidget(separator1)
        verticalLayout.addLayout(box1)
        verticalLayout.addWidget(separator2)
        verticalLayout.addLayout(box2)
        #verticalLayout.addWidget(button3)

        #Enlazamos el layout principal con la clase QDialog
        self.setLayout(verticalLayout)


"""
Clase que crea el primer frame que se muestra cuando abrimos la aplicación
"""
class MainFrame(QDialog):
    def __init__(self):
        super(MainFrame, self).__init__()

        # MainFrame layouts
        grid = QGridLayout()
        verticalLayout = QVBoxLayout()

        #Logo
        image = QPixmap("logo2.png")
        logo = QLabel()
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: 20px;")

        #Botón de Horario
        button1 = QPushButton("Horario")
        button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button1.setStyleSheet(
            "*{border: 4px solid '#BC006C';" +
            "border-radius: 15px;" +
            "font-size: 75px;" +
            "color: 'white';" +
            "padding: 25px 0;" +
            "margin: 50px 100px;}"+
            "*:hover{background: '#BC006C';}"
        )

        #Conectar este botón con el frame del horario
        button1.clicked.connect(self.gotoScheduleFrame)

        #Botón de Mapa
        button2 = QPushButton("Ocupación")
        button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button2.setStyleSheet(
            "*{border: 4px solid '#BC006C';" +
            "border-radius: 15px;" +
            "font-size: 75px;" +
            "color: 'white';" +
            "padding: 25px 0;" +
            "margin: 50px 100px;}"+
            "*:hover{background: '#BC006C';}"
        )

        #Conectar este botón con el frame de horario
        button2.clicked.connect(self.gotoOcupacionFrame)

        #Botón de Brújula
        button3 = QPushButton("Salir")
        button3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button3.setStyleSheet(
            "*{border: 4px solid '#BC006C';" +
            "border-radius: 15px;" +
            "font-size: 75px;" +
            "color: 'white';" +
            "padding: 25px 0;" +
            "margin: 50px 100px;}"+
            "*:hover{background: '#BC006C';}"
        )

        #Añadimos los distintos elementos s los layouts
        grid.addWidget(button1, 0, 0)
        grid.addWidget(button2, 0, 1)
        verticalLayout.addWidget(logo)
        verticalLayout.addLayout(grid)
        verticalLayout.addWidget(button3)

        #Enlazamos el layout principal con la clase QDialog
        self.setLayout(verticalLayout)

    """
    Función que nos redirige a al frame del horario
    """
    def gotoScheduleFrame(self):
        window.setCurrentIndex(window.currentIndex()+2)

    def gotoOcupacionFrame(self):
        window.setCurrentIndex(window.currentIndex()+3)

"""
Clase que crea el frame del horario que nos muestra eventos cercanos de relevancia (clases, tutorías, etc)
"""
class ElectionFrame(QDialog):
    def __init__(self):
        super(ElectionFrame, self).__init__()

        #ScheduleFrame Widgets/layouts
        verticalLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        separator_horizontal = QHSeperationLine()
        separator_horizontal2 = QHSeperationLine()

        #Obtenemos la imagen de Like
        image = QPixmap("Like.png")
        like = QLabel()
        like.setPixmap(image)
        like.setAlignment(QtCore.Qt.AlignCenter)
        like.setStyleSheet("margin-top: 25px;" + "margin-bottom: 25px;")

        #Obtenemos la imagen de Stop
        image = QPixmap("Stop.png")
        stop = QLabel()
        stop.setPixmap(image)
        stop.setAlignment(QtCore.Qt.AlignCenter)
        stop.setStyleSheet("margin-top: 25px;" + "margin-bottom: 25px;")

        #Formulamos la pregunta y la añadimos al layout
        question = QLabel("¿Seguro que quieres salir?")
        question.setAlignment(QtCore.Qt.AlignCenter)
        question.setFont(QFont('Times', 50))
        question.setStyleSheet("color: '#ECE5EC';")
        verticalLayout.addWidget(question)
        verticalLayout.addWidget(separator_horizontal)

        #Añadimos las fotos al layout horizontal y lo añadimos al vergtical
        horizontalLayout.addWidget(stop)
        horizontalLayout.addWidget(like)
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addWidget(separator_horizontal2)

        #Motramos el logo de nuevo más pequeño
        image = QPixmap("logo.png")
        logo = QLabel()
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: 20px;")

        #Añadimos el logo al layout principal
        verticalLayout.addWidget(logo)

        #Enlazamos el layout principal con la clase QDialog
        self.setLayout(verticalLayout)

"""
Clase que crea el frame del horario que nos muestra eventos cercanos de relevancia (clases, tutorías, etc)
"""
class ScheduleFrame(QDialog):
    def __init__(self):
        super(ScheduleFrame, self).__init__()

        #ScheduleFrame Widgets/layouts
        self.scrollArea = QGridLayout()
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        verticalLayout = QVBoxLayout()
        separator_horizontal = QHSeperationLine()
        separator_horizontal2 = QHSeperationLine()

        image = QPixmap("upArrow.png")
        UA = QLabel()
        UA.setPixmap(image)
        UA.setAlignment(QtCore.Qt.AlignCenter)

        image = QPixmap("downArrow.png")
        DA = QLabel()
        DA.setPixmap(image)
        DA.setAlignment(QtCore.Qt.AlignCenter)

        #Creamos los distintos eventos del horario
        self.lesson1 = CardView("empty.png", "", "", 175)
        self.lesson2 = CardView("VC.png", "Visión por Computador (Teoría)", "Aula: 1.7\nHora: 8:30-10:30\nProfesor: Nicolás Pérez de la Blanca Capilla", 350)
        self.lesson3 = CardView("VC.png", "Visión por Computador (Practicas)", "Aula: 3.7\nHora: 10:30-12:30\nProfesor: Nicolás Pérez de la Blanca Capilla", 175)

        #Añadimos dichos eventos al layout
        self.scrollArea.addWidget(UA, 0,0)
        self.scrollArea.addWidget(self.lesson1,1,0)
        self.scrollArea.addWidget(separator_horizontal,2,0)
        self.scrollArea.addWidget(self.lesson2,3,0)
        self.scrollArea.addWidget(separator_horizontal2,4,0)
        self.scrollArea.addWidget(self.lesson3,5,0)
        self.scrollArea.addWidget(DA,6,0)

        #Añadimos el scrollArea al layout principal
        verticalLayout.addLayout(self.scrollArea)

        #Motramos el logo de nuevo más pequeño
        image = QPixmap("logo.png")
        logo = QLabel()
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: 20px;")

        #Añadimos el logo al layout principal
        verticalLayout.addWidget(logo)

        #Enlazamos el layout principal con la clase QDialog
        self.setLayout(verticalLayout)

    def changeCardView(self):
        self.lesson1.changeParameters(lista_images[contador], lista_names[contador], lista_info[contador], 175)
        self.lesson2.changeParameters(lista_images[contador+1], lista_names[contador+1], lista_info[contador+1], 350)
        self.lesson3.changeParameters(lista_images[contador+2], lista_names[contador+2], lista_info[contador+2], 175)

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    timer = 0
    ultimoSwipe = 300
    diferencia = 40

    def on_init(self, controller):
        print("Initialized")

    def on_connect(self, controller):
        print("Connected")

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        global is_gesturing
        global schedule
        global contador

        frame = controller.frame()

        if((self.timer - self.ultimoSwipe)%157 == self.diferencia):
            self.ultimoSwipe = 300

        self.timer = (self.timer+1) % 157

        print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures())))

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"
            print ("  %s, id %d, position: %s" % (handType, hand.id, hand.palm_position))

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            print ("  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                direction.pitch * Leap.RAD_TO_DEG,
                normal.roll * Leap.RAD_TO_DEG,
                direction.yaw * Leap.RAD_TO_DEG))

            #Obtenemos los distintos dedos de la mano
            thumb = hand.fingers[0]
            index = hand.fingers[1]
            middle = hand.fingers[2]
            ring = hand.fingers[3]
            little = hand.fingers[4]

            x_finger_position = int(((index.tip_position.x + 175) / 350) * 1920)
            y_finger_position = (int(((index.tip_position.y-100) / 200) * 1080)-1080)*-1

            x_hand_position = int(((hand.palm_position.x + 175) / 350) * 1920)
            y_hand_position = (int(((hand.palm_position.y-100) / 200) * 1080)-1080)*-1

            #Si solo tenemos sacado el dedo indice podemos controllar el ratón y pulsar botones
            if index.is_extended and not(middle.is_extended) and not(thumb.is_extended) and not(ring.is_extended) and not(little.is_extended):
                current_cursor.setPos(x_finger_position, y_finger_position)
                app.setOverrideCursor(current_cursor)
                is_gesturing = False

                if (index.tip_velocity[2] < -400 and window.currentIndex() == 0 and x_finger_position > 114 and x_finger_position < 849 and y_finger_position > 583 and y_finger_position < 724):
                    window.setCurrentIndex(window.currentIndex()+2)

                if (index.tip_velocity[2] < -400 and window.currentIndex() == 0 and x_finger_position > 114 and x_finger_position < 1806 and y_finger_position > 839 and y_finger_position < 976):
                    window.setCurrentIndex(window.currentIndex()+1)

            # Si extendemos todos los dedos podemos realizar gestos
            if index.is_extended and middle.is_extended and thumb.is_extended and ring.is_extended and little.is_extended and not(window.currentIndex() == 1):
                current_cursor.setPos(x_hand_position, y_hand_position)
                app.setOverrideCursor(gesture_cursor)
                is_gesturing = True

                #Swipe
                if((self.timer - self.ultimoSwipe) % 157 > self.diferencia):
                    if (hand.palm_velocity[1] < -400):
                        contador = (contador-1) % (len(lista_images)-2)
                        schedule.changeCardView()
                        self.ultimoSwipe = self.timer
                    elif(hand.palm_velocity[1] > 400):
                        contador = (contador+1) % (len(lista_images)-2)
                        schedule.changeCardView()
                        self.ultimoSwipe = self.timer

            #Gesto para volver a la pestaña anterior
            if(is_gesturing and window.currentIndex() == 2 and not(index.is_extended) and not(middle.is_extended) and not(thumb.is_extended) and not(ring.is_extended) and not(little.is_extended)):
                window.setCurrentIndex(window.currentIndex()-2)

            if(window.currentIndex() == 1):
                if (handType == "Right hand"):
                    if (normal.roll * Leap.RAD_TO_DEG > -120 and normal.roll * Leap.RAD_TO_DEG < -70):
                        if not (index.is_extended) and not (middle.is_extended) and not (ring.is_extended) and not (little.is_extended):
                            app.quit()
                            sys.exit()
                    if (direction.pitch * Leap.RAD_TO_DEG > 40 and direction.pitch * Leap.RAD_TO_DEG < 70):
                        if index.is_extended and middle.is_extended and thumb.is_extended and ring.is_extended and little.is_extended:
                            window.setCurrentIndex(window.currentIndex()-1)

        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ("")

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print ("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    #finally:
        # Remove the sample listener when done
        # controller.remove_listener(listener)




#Creamos la aplicación y variables globales
app = QApplication(sys.argv)

is_gesturing = False
contador = 0
lista_images = ["empty.png","VC.png", "VC.png", "RSC.png", "tutoria.png","conference.png","empty.png"]
lista_names = ["","Visión por Computador (Teoría)","Visión por Computador (Practicas)", "Procesadores de Lenguajes (Practicas)", "Tutoría (Visión por Computador)", "Conferencia (Ciberseguridad)",""]
lista_info = ["","Aula: 1.7\nHora: 8:30-10:30\nProfesor: Nicolás Pérez de la Blanca Capilla","Aula: 3.7\nHora: 10:30-12:30\nProfesor: Nicolás Pérez de la Blanca Capilla", "Aula: 2.8\nHora: 12:30-14:30\nProfesor: Ramón López-Cózar Delgado",
              "Aula: 1.7\nHora: 13:30-17:30\nProfesor: Nicolás Pérez de la Blanca Capilla","Aula: 0.3\nHora: 19:30-20:30\nPonente: Patricia Díez Muñoz", ""]

#Ponemos a ejecutar el listener en segundo plano ( en la terminal )
download_thread = threading.Thread(target=main, name="MainFunction")
download_thread.start()

#Definimos los dintintos frames de la app
mainWindow = MainFrame()
election = ElectionFrame()
schedule = ScheduleFrame()
ocupacion = OcupacionFrame()

#Creamos la ventana
window = QStackedWidget()
window.setWindowTitle("LeapMotion_APP")
window.setMinimumWidth(1000)
window.setMinimumHeight(500)
window.setStyleSheet("background: #161219;")
window.setAutoFillBackground(True)

#Cursor personalizado
cursor_pix = QPixmap('hand.png')
cursor_scaled_pix = cursor_pix.scaled(QtCore.QSize(60, 60), QtCore.Qt.KeepAspectRatio)
current_cursor = QCursor(cursor_scaled_pix, -1, -1)

#Cursor para los gestos
cursor_pix = QPixmap('gesture.png')
cursor_scaled_pix = cursor_pix.scaled(QtCore.QSize(60, 60), QtCore.Qt.KeepAspectRatio)
gesture_cursor = QCursor(cursor_scaled_pix, -1, -1)

#Almacenamos los frames en la ventana y mostramos por pantalla
window.addWidget(mainWindow)
window.addWidget(election)
window.addWidget(schedule)
window.addWidget(ocupacion)
window.show()

sys.exit(app.exec())

