import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Calculator")
        self.CreateApp()

    def CreateApp(self):

        # Creating a variable named Grid
        grid = QGridLayout()

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 =  QPushButton("Three")
        button3 = QPushButton("Last")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())