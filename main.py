import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor
import random


# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(652, 357)
#         self.pushButton = QtWidgets.QPushButton(Form)
#         self.pushButton.setGeometry(QtCore.QRect(520, 20, 101, 61))
#         self.pushButton.setStyleSheet("background: yellow")
#         self.pushButton.setObjectName("pushButton")


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 652, 357)
        self.setWindowTitle('Git и случайные окружности')
        self.is_draw = False

        self.pushButton = QPushButton('Жёлтая кнопка', self)
        self.pushButton.resize(101, 61)
        self.pushButton.move(520, 20)
        self.pushButton.setStyleSheet("background: yellow")
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.is_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.is_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        num = random.randint(1, 150)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(QPointF(250, 150), num, num)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
