import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, \
    QPushButton, QScrollArea, QWidget, QVBoxLayout, QLabel, QComboBox, \
    QTableView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QAbstractTableModel
from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import QAbstractTableModel, Qt
import probabilities


app = QtWidgets.QApplication([])
app.setStyle('Fusion')
win = QWidget()
layout = QVBoxLayout()


probTable = QTableView()


def listToComboBox(comboBox, choices):
    for i in choices:
        comboBox.addItem(str(i))


class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, i, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[i]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[i]
        return None


def onProbBtnClicked(choice1, choice2):
    print(str(choice1) + ' and ' + str(choice2))
    series = [str(choice1), str(choice2)]
    model = PandasModel(probabilities.
                        generatePDf(probabilities.csvToDf('language_data.csv'),
                                    series))
    probTable.setModel(model)


win.setLayout(layout)
comboBox1 = QComboBox()
comboBox2 = QComboBox()
choices = probabilities.getSeries(probabilities.csvToDf('language_data.csv'))
listToComboBox(comboBox1, choices)
listToComboBox(comboBox2, choices)
layout.addWidget(comboBox2)
layout.addWidget(comboBox1)
probBtn = QPushButton('Calculate Probabilities')
probBtn.clicked.connect(lambda: onProbBtnClicked(str(comboBox1.currentText()), 
                                                 str(comboBox2.currentText())))
layout.addWidget(probBtn)
# model = PandasModel(probabilities.csvToDf('language_data.csv'))
# probTable.setModel(model)
layout.addWidget(probTable)
win.show()


def gui():
    app.exec_()
    sys.exit(app.exec_())
