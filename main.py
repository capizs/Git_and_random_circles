import sys
from random import randint
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.setWindowTitle("Кружочки")
        self.resize(400, 400)
        self.add_circle = QPushButton("Кружочек", self)
        self.add_circle.setGeometry(QtCore.QRect(125, 170, 150, 30))


class Circles(UI,QWidget):
    def __init__(self):
        UI.__init__(self)
        self.add_circle.clicked.connect(self.add)
    def paintEvent(self, event):
        if self.flag:
            qp=QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0,255), randint(0,255), randint(0,255)))
            r = randint(0, 150)
            qp.drawEllipse(randint(0, 400 - r), randint(0, 400 - r), r, r)
            qp.end()

    def add(self):
        self.flag = True
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
