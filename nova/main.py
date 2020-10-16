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
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Botões
        self.result_fild = qtw.QLineEdit()
        result = qtw.QPushButton('Enter', clicked = self.func_result)
        clear = qtw.QPushButton('Limpar', clicked = self.clear_calc)
        pb_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        pb_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        pb_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        pb_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        pb_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        pb_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        pb_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        pb_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        pb_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        pb_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        pbSoma = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        pbSubtracao = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        pbMutiplicacao = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        pbDivisao = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))

        # Adicionando os Botões ao Layout
        container.layout().addWidget(self.result_fild, 0, 0, 1, 4)

        container.layout().addWidget(result, 1, 0,  1, 2)
        container.layout().addWidget(clear, 1, 2, 1, 2)
        container.layout().addWidget(pb_9, 2, 0)
        container.layout().addWidget(pb_8, 2, 1)
        container.layout().addWidget(pb_7, 2, 2)
        container.layout().addWidget(pb_6, 3, 0)
        container.layout().addWidget(pb_5, 3, 1)
        container.layout().addWidget(pb_4, 3, 2)
        container.layout().addWidget(pb_3, 4, 0)
        container.layout().addWidget(pb_2, 4, 1)
        container.layout().addWidget(pb_1, 4, 2)
        container.layout().addWidget(pb_0, 5, 0, 1, 3)
        container.layout().addWidget(pbSoma, 2, 3)
        container.layout().addWidget(pbSubtracao, 3, 3)
        container.layout().addWidget(pbMutiplicacao, 4, 3)
        container.layout().addWidget(pbDivisao, 5, 3)

        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_fild.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_fild.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_fild.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_fild.setText(fin_string)

    def clear_calc(self):
        self.result_fild.clear()
        self.temp_nums = []
        self.fin_nums = []


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
