#! /usr/bin/python3

from PyQt5.Qtcore import QUrl
from PyQt5.QtWidgets import *


class Page(QWidget):
    def __init__(self, parent=None):
        super(Page, self).__init__(parent)

        my_label = QLabel("This is my label")
        layout = QVBoxLayout()

        layout.addWidget(my_label)

        mainLayout = QGridLayout()
        mainLayout.addLayout(layout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My first Qt App")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = Page()
    window.show()

    sys.exit(app.exec_())

