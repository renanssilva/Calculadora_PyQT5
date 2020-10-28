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

        # ----Conectando Botão Ponto (.)
        self.pbPonto.clicked.connect(self.digitaPonto)

        # ----Conectando Botões +/- e Porcentagem (+/-, %)
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

    def digitaNumero(self):
        botao = self.sender()
        conteudo = self.lbMostraConta.text()
        print((conteudo))
        self.lbMostraConta.setText(conteudo + botao.text())

    def digitaPonto(self):
        pass

    def operadoresUnarios(self):
        pass

    def operadores(self):
        botao = self.sender()
        conteudo = self.lbMostraConta.text()
        self.lbMostraConta.setText(conteudo + botao.text())


    def digitaIgual(self):
        conteudo = self.lbMostraConta.text()
        if 'X' in conteudo:
            conteudo = conteudo.replace('X', '*')
            print(conteudo)
        igual = float(eval(conteudo))
        self.lbMostraConta.setText(f'{igual:.2f}')
        #self.lbMostraConta.setText(f'{igual:.3e}')

    def clear(self):
        self.lbMostraConta.setText('')


# Execute app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Calc()
    sys.exit(app.exec_())
