import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, \
    QPushButton, QScrollArea, QWidget, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets
import probabilities

def listToComboBox(comboBox, choices):
    for i in choices:
        comboBox.addItem(str(i))


def onProbBtnClicked(choice1, choice2):
    print(str(choice1) + ' and ' + str(choice2))
    series = [str(choice1), str(choice2)]
    probabilities.generatePDf(probabilities.csvToDf('language_data.csv'), series)


def gui():
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')
    win = QWidget()
    layout = QVBoxLayout()
    win.setLayout(layout)

    choices = probabilities.getSeries(probabilities.csvToDf('language_data.csv'))
    comboBox1 = QComboBox()
    comboBox2 = QComboBox()
    listToComboBox(comboBox1, choices)
    listToComboBox(comboBox2, choices)
    layout.addWidget(comboBox1)
    layout.addWidget(comboBox2)

    probBtn = QPushButton('Calculate Probabilities')
    probBtn.clicked.connect(lambda: onProbBtnClicked(str(comboBox1.currentText()), 
                                                     str(comboBox2.currentText())))
    layout.addWidget(probBtn)

    win.show()
    app.exec_()
    sys.exit(app.exec_())
