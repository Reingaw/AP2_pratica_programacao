import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = 'AP2 - Prática de Programação'

        button1 = QPushButton('Enviar', self)
        button1.move(570, 490)  # (W, H)
        button1.resize(90, 30)  # (W, H)
        button1.setStyleSheet('QPushButton {background-color: #0FB328; font-size: 10px;}')
        button1.clicked.connect(self.doNothing)
        self.LoadWindow()

    def LoadWindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def doNothing(self):
        print('Viu, não fiz nada! hehe =D')

app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())