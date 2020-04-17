import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, \
    QPushButton, QScrollArea, QWidget, QVBoxLayout, QComboBox, \
    QTableView
from PyQt5.QtCore import QAbstractTableModel
from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import Qt
import probabilities


def runGui():
    # Set up the basic layout
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')
    win = QWidget()
    layout = QVBoxLayout()

    # Create the basic widgets
    probTable = QTableView()
    win.setLayout(layout)
    comboBox1 = QComboBox()
    comboBox2 = QComboBox()
    probBtn = QPushButton('Calculate Probabilities')

    # Create the options for the combo boxes
    choices = probabilities.csvToDf('language_data.csv').columns
    listToComboBox(comboBox1, choices)
    listToComboBox(comboBox2, choices)

    # Add functionality to the button
    probBtn.clicked.connect(lambda: onProbBtnClicked(
                            str(comboBox1.currentText()),
                            str(comboBox2.currentText()),
                            probTable))

    # Add all the widgets to the layout
    layout.addWidget(comboBox2)
    layout.addWidget(comboBox1)
    layout.addWidget(probBtn)
    layout.addWidget(probTable)

    # Show everything
    win.show()
    app.exec_()
    sys.exit(app.exec_())


# IN: PyQt comboBox, list of choices for the combobox
# Functionality: adds the list to the combobox
def listToComboBox(comboBox, choices):
    for i in choices:
        comboBox.addItem(str(i))


# Custom model for the probability table
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
                return (str(self._data.iloc[index.row(), index.column()]) + "%")
        return None

    def headerData(self, i, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[i]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[i]
        return None


# IN: 2 choices as strings, a PyQt tableview
def onProbBtnClicked(choice1, choice2, probTable):
    print(str(choice1) + ' and ' + str(choice2))
    series = [str(choice1), str(choice2)]
    model = PandasModel(probabilities.
                        generatePDf(probabilities.csvToDf('language_data.csv'),
                                    series))
    probTable.setModel(model)
