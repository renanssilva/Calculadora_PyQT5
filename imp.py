from layout import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore


class Calc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Calc, self).__init__()
        self.setupUi(self)

        # Removendo titulo da janela
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Background Transparente
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Show Window
        self.show()

        # Conectando Botões
        self.pb0.clicked.connect(self.digitaNumero)
        self.pb1.clicked.connect(self.digitaNumero)
        self.pb2.clicked.connect(self.digitaNumero)
        self.pb3.clicked.connect(self.digitaNumero)
        self.pb4.clicked.connect(self.digitaNumero)
        self.pb5.clicked.connect(self.digitaNumero)
        self.pb6.clicked.connect(self.digitaNumero)
        self.pb7.clicked.connect(self.digitaNumero)
        self.pb8.clicked.connect(self.digitaNumero)
        self.pb9.clicked.connect(self.digitaNumero)

    def digitaNumero(self):
        botao = self.sender()
        self.lbMostraConta.setText(botao.text())


# Execute app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Calc()
    sys.exit(app.exec_())
