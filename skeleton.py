import sys
from PyQt5 import QtCore, QtGui, uic
from library import HelpGUI
from library import XcpCom

qtCreatorFile = 'layout.ui'  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # initialize helpers
        self.helper = HelpGUI.AssistGUI()
        self.xcp_com = XcpCom.XcpCommunicator(0)

        # button callbacks
        self.pushButton.clicked.connect(self.load_a2l)
        self.pushButton_5.clicked.connect(self.print_test)

        # completer
        self.model = QtGui.QStringListModel(self)

        completer = QtGui.QCompleter(self)
        completer.setModel(self.model)

        self.lineEdit.setCompleter(completer)

    def load_a2l(self):
        """Method to parse selected A2L file into DB for DAQ purposes"""
        name = QtGui.QFileDialog.getOpenFileName(self, 'Please select an .a2l file')
        measurement_list = self.helper.parse_a2l(name)
        self.model.setStringList(measurement_list)
        self.lineEdit.setText('Please select a measurement to read')

    def start_daq(self):
        pass

    def print_test(self):
        x = []
        y = []
        for i in range(100):
            x.append(i)
            y.append(1)
            plt1 = self.graphicsView
            plt1.plot(x, y)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
