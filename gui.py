import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, \
    QPushButton, QScrollArea, QWidget, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets

def langComboBoxes(layout, choices):
    comboBox = QComboBox()
    for i in range(choices):
        comboBox.addItem(str(i))
    layout.addWidget(comboBox)


def gui():
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')
    win = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Bottom'))
    win.setLayout(layout)
    langComboBoxes(layout)
    win.show()
    app.exec_()
    sys.exit(app.exec_())
