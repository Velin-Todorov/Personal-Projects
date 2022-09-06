from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300,  600, 600)
        self.setWindowTitle('Test Title')
        self.show()


window = Window()
app = QApplication(sys.argv)
label = QLabel("<font color=red size=40>Hello World!</font>")
label.show()
app.exec()
