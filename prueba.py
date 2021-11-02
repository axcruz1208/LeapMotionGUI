import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QCursor

"""
Función que nos crea una especie de tarjeta para almacenar las clases/tutorias/conferencia que vamos a tener
con una fotografía e información sobre las mismas
"""
class CardView(QWidget):
	def __init__(self, image,name, information, *args, **kwargs):
		super(CardView, self).__init__(*args, **kwargs)

		#Imagen con sus propiedades
		lessonImage = QPixmap(image)
		lessonImage = lessonImage.scaled(290, 290)
		cardViewImage = QLabel()
		cardViewImage.setPixmap(lessonImage)
		cardViewImage.setStyleSheet("margin-left: 400px;")

		#Información sobre la clase en cuestión
		name = QLabel(name)
		name.setAlignment(QtCore.Qt.AlignLeft)
		name.setStyleSheet(	"font-size: 50px;" + "color: 'white';" + "margin-right: 150px")
		information = QLabel(information)
		information.setAlignment(QtCore.Qt.AlignTop)
		information.setStyleSheet(	"font-size: 25px;")

		#Layout vertical que almacena la información
		verticalLayout = QVBoxLayout()
		verticalLayout.addWidget(name)
		verticalLayout.addWidget(information)

		#Layout horizontal que almacena imagen y layout vertical
		layout = QHBoxLayout()
		layout.addWidget(cardViewImage)
		layout.addLayout(verticalLayout)

		self.setLayout(layout)


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("LeapMotion_APP")
window.setMinimumWidth(1000)
window.setMinimumHeight(500)
window.setStyleSheet("background: #161219;")
window.setAutoFillBackground(True)

#MainFrame Widgets
grid = QGridLayout()
verticalLayout = QVBoxLayout()

def main_frame():
	#display logo
	image = QPixmap("logo.png")
	logo = QLabel()
	logo.setPixmap(image)
	logo.setAlignment(QtCore.Qt.AlignCenter)
	logo.setStyleSheet("margin-top: 20px;")

	#button horario
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

	#button mapa
	button2 = QPushButton("Mapa")
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

	#button brújula
	button3 = QPushButton("Brújula")
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

	grid.addWidget(button1, 0, 0)
	grid.addWidget(button2, 0, 1)
	verticalLayout.addWidget(logo)
	verticalLayout.addLayout(grid)
	verticalLayout.addWidget(button3)

#ScheduleFrame Widgets
scrollArea = QScrollArea()
widget = QWidget()

def schedule_frame():

	lesson1 = CardView("VC.png", "Visión por Computador (Teoría)", "Aula: 1.7\nHora: 8:30-10:30\nProfesor: Nicolás Pérez de la Blanca Capilla")
	lesson2 = CardView("VC.png", "Visión por Computador (Practicas)", "Aula: 3.7\nHora: 10:30-12:30\nProfesor: Nicolás Pérez de la Blanca Capilla")
	lesson3 = CardView("RSC.png", "Procesadores de Lenguajes (Practicas)", "Aula: 0.8\nHora: 12:30-14:30\nProfesor: Ramón López-Cózar Delgado")
	lesson4 = CardView("tutoria.png", "Tutoría (Visión por Computador)", "Aula: 1.7\nHora: 13:30-17:30\nProfesor: Nicolás Pérez de la Blanca Capilla")
	lesson5 = CardView("conference.png", "Conferencia (Ciberseguridad)", "Aula: 0.3\nHora: 19:30-20:30\nPonente: Patricia Díez Muñoz")

	layout = QVBoxLayout()
	layout.addWidget(lesson1)
	layout.addWidget(lesson2)
	layout.addWidget(lesson3)
	layout.addWidget(lesson4)
	layout.addWidget(lesson5)

	widget.setLayout(layout)

	scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
	scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
	scrollArea.setWidgetResizable(True)
	scrollArea.setWidget(widget)
	verticalLayout.addWidget(scrollArea)

	#display logo
	image = QPixmap("logo.png")
	logo = QLabel()
	logo.setPixmap(image)
	logo.setAlignment(QtCore.Qt.AlignCenter)
	logo.setStyleSheet("margin-top: 20px;")
	verticalLayout.addWidget(logo)

schedule_frame()

window.setLayout(verticalLayout)

window.show()
sys.exit(app.exec())

