from layout import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore


class Calc(QtWidgets.QMainWindow, Ui_MainWindow):

    primeiroNumero = None
    usandoSegundoNumero = False

    def __init__(self):
        super(Calc, self).__init__()
        self.setupUi(self)

        # Removendo titulo da janela
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Background Transparente
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Show Window
        self.show()

        # Conectando Botões Números (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
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

        # Conectando Botão Ponto (.)
        self.pbPonto.clicked.connect(self.digitaPonto)

        # Conectando Botões +/- e Porcentagem (+/-, %)
        self.pbPositivoNegativo.clicked.connect(self.operadoresUnarios)
        self.pbFuncaoPorcentagem.clicked.connect(self.operadoresUnarios)

        # Conectando Botões Operadores (+, -, *, /)
        self.pbFuncaoSoma.clicked.connect(self.operadores)
        self.pbFuncaoSubtracao.clicked.connect(self.operadores)
        self.pbFuncaoDivisao.clicked.connect(self.operadores)
        self.pbFuncaoMutiplicacao.clicked.connect(self.operadores)

        # Conectando Botão de Igualdade (=)
        self.pbIgual.clicked.connect(self.digitaIgual)

        # Conectando Botão de Limpar  Display (C)
        self.pbClear.clicked.connect(self.clear)

        self.pbFuncaoSoma.setCheckable(True)
        self.pbFuncaoSubtracao.setCheckable(True)
        self.pbFuncaoDivisao.setCheckable(True)
        self.pbFuncaoMutiplicacao.setCheckable(True)

    def digitaNumero(self):
        botao = self.sender()

        if (self.pbFuncaoSoma.isChecked() or self.pbFuncaoSubtracao.isChecked() or
                self.pbFuncaoSoma.isChecked() or self.pbFuncaoSubtracao.isChecked()) and (not self.usandoSegundoNumero):
            novoLabel = format(float(botao.text()), '.15g')
            self.usandoSegundoNumero = True
        else:
            if '.' in self.lbMostraConta.text() and botao.text()== '0':
                novoLabel = format(float(self.lbMostraConta.text() + botao.text()), '.15')
            else:
                novoLabel = format(float(self.lbMostraConta.text() + botao.text()), '.15g')
        self.lbMostraConta.setText(str(novoLabel))

    def digitaPonto(self):
        self.lbMostraConta.setText(self.lbMostraConta.text() + '.')

    def operadoresUnarios(self):
        botao = self.sender()
        labelNumber = float(self.lbMostraConta.text())

        if botao.text() == '+/-':
            labelNumber *= - 1
        else: # botao.text() == '%'
            labelNumber *= 0.01

        novoLabel = format(labelNumber, '15g')
        self.lbMostraConta.setText(novoLabel)

    def operadores(self):
        pass

    def digitaIgual(self):
        pass

    def clear(self):
        pass


# Execute app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Calc()
    sys.exit(app.exec_())
