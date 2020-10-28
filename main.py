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
        self.pbPonto.clicked.connect(self.simbolos)

        # ----Conectando Botões +/- e Porcentagem (X², %)
        self.pbQuadrado.clicked.connect(self.simbolos)
        self.pbFuncaoPorcentagem.clicked.connect(self.simbolos)

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
        self.lbMostraConta.setText(conteudo + botao.text())

    def digitaPonto(self):
        pass

    def simbolos(self):
        conteudo = self.lbMostraConta.text()
        if conteudo:
            botao = self.sender()
            if botao.text() == 'X²':
                botao = '²'
                print(botao)
                self.lbMostraConta.setText(conteudo + botao)
            elif botao.text() == '.':
                self.lbMostraConta.setText(conteudo + botao.text())
            else:  # botao.text() == '%'
                conteudo = float(self.lbMostraConta.text())
                conteudo *= 0.01
                self.lbMostraConta.setText(str(conteudo))

    def operadores(self):
        botao = self.sender()
        conteudo = self.lbMostraConta.text()
        if conteudo:
            self.lbMostraConta.setText(conteudo + botao.text())
        if botao.text() == '-':
            self.lbMostraConta.setText(conteudo + botao.text())

    def digitaIgual(self):
        conteudo = self.lbMostraConta.text()
        if conteudo:
            if 'X' in conteudo:
                conteudo = conteudo.replace('X', '*')
                print(conteudo)
            if '²' in conteudo:
                # O back-end entendera que X² como dois elementos
                conteudo = conteudo.replace('²', '**2')
                print(conteudo)
            igual = float(eval(conteudo))
            self.lbMostraConta.setText(f'{igual:.2f}')

    def clear(self):
        self.lbMostraConta.setText('')


# Execute app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Calc()
    sys.exit(app.exec_())
