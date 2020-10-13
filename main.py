import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []

        self.show()

    def keypad(self):
        # Container
        recebeComponentes = qtw.QWidget()
        recebeComponentes.setLayout(qtw.QGridLayout())

        # Botões
        self.leCampo = qtw.QLineEdit()
        pbResultado = qtw.QPushButton('Enter')
        pbLimpar = qtw.QPushButton('Limpar')
        pb_9 = qtw.QPushButton('9', clicked = lambda : self.precionaNumero('9'))
        pb_8 = qtw.QPushButton('8', clicked = lambda : self.precionaNumero('8'))
        pb_7 = qtw.QPushButton('7', clicked = lambda : self.precionaNumero('7'))
        pb_6 = qtw.QPushButton('6', clicked = lambda : self.precionaNumero('6'))
        pb_5 = qtw.QPushButton('5', clicked = lambda : self.precionaNumero('5'))
        pb_4 = qtw.QPushButton('4', clicked = lambda : self.precionaNumero('4'))
        pb_3 = qtw.QPushButton('3', clicked = lambda : self.precionaNumero('3'))
        pb_2 = qtw.QPushButton('2', clicked = lambda : self.precionaNumero('2'))
        pb_1 = qtw.QPushButton('1', clicked = lambda : self.precionaNumero('1'))
        pb_0 = qtw.QPushButton('0', clicked = lambda : self.precionaNumero('0'))
        pbSoma = qtw.QPushButton('+', clicked = lambda : self.pressionaFuncao('+'))
        pbSubtracao = qtw.QPushButton('-', clicked = lambda : self.pressionaFuncao('-'))
        pbMutiplicacao = qtw.QPushButton('*', clicked = lambda : self.pressionaFuncao('*'))
        pbDivisao = qtw.QPushButton('/', clicked = lambda : self.pressionaFuncao('/'))

        # Adicionando os Botões ao Layout
        recebeComponentes.layout().addWidget(self.leCampo, 0, 0, 1, 4)
        recebeComponentes.layout().addWidget(pbResultado, 1, 0,  1, 2)
        recebeComponentes.layout().addWidget(pbLimpar, 1, 2, 1, 2)
        recebeComponentes.layout().addWidget(pb_9, 2, 0)
        recebeComponentes.layout().addWidget(pb_8, 2, 1)
        recebeComponentes.layout().addWidget(pb_7, 2, 2)
        recebeComponentes.layout().addWidget(pb_6, 3, 0)
        recebeComponentes.layout().addWidget(pb_5, 3, 1)
        recebeComponentes.layout().addWidget(pb_4, 3, 2)
        recebeComponentes.layout().addWidget(pb_3, 4, 0)
        recebeComponentes.layout().addWidget(pb_2, 4, 1)
        recebeComponentes.layout().addWidget(pb_1, 4, 2)
        recebeComponentes.layout().addWidget(pb_0, 5, 0, 1, 3)
        recebeComponentes.layout().addWidget(pbSoma, 2, 3)
        recebeComponentes.layout().addWidget(pbSubtracao, 3, 3)
        recebeComponentes.layout().addWidget(pbMutiplicacao, 4, 3)
        recebeComponentes.layout().addWidget(pbDivisao, 5, 3)

        self.layout().addWidget(recebeComponentes)

    def precionaNumero(self, numero):
        self.temp_nums.append(numero)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.leCampo.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.leCampo.setText(temp_string)

    def pressionaFuncao(self, operador):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operador)
        self.temp_nums = []
        self.leCampo.setText(''.join(self.fin_nums))

    def resultado(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        resutado_string = eval(fin_string)
        fin_string += '='
        fin_string += str(resutado_string)
        self.leCampo.setText(fin_string)

    def limpaCampo(self):
        self.leCampo.clear()
        self.temp_nums = []
        self.fin_nums = []


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
