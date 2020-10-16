from layout import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets, QtCore


class Calc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Calc, self).__init__()
        self.setupUi(self)

        # Removendo titulo da janela
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Background Transparente
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Show Window
        self.show()


# Execute app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Calc()
    sys.exit(app.exec_())
