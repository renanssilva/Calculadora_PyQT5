# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 565)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: rgba(0, 0, 0, 200);\n"
"    font: 75 14pt \"DejaVu Sans\";\n"
"    border: 3px solid #DAA520;\n"
"    border-radius: 11px;\n"
"    background-color: rgb(154, 254, 214);\n"
"}\n"
"\n"
"#pb0, #pb1, #pb2, #pb3, #pb4, #pb5, #pb6, #pb7, #pb8, #pb9 {\n"
"    background-color: #FCFCFC;\n"
"}\n"
"\n"
"#pbIgual {    \n"
"    background-color: rgb(254, 121, 199);\n"
"}\n"
"\n"
"QLabel {\n"
"    \n"
"    color: #000000;\n"
"    border: 5px solid #DAA520;\n"
"    border-top-right-radius:70px;\n"
"    border-top-left-radius:70px;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frSinais = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frSinais.sizePolicy().hasHeightForWidth())
        self.frSinais.setSizePolicy(sizePolicy)
        self.frSinais.setMinimumSize(QtCore.QSize(551, 501))
        self.frSinais.setStyleSheet("#frSinais {\n"
"    background-color: rgb(89, 150, 177);\n"
"    border-top-right-radius:70px;\n"
"    border-top-left-radius:70px;\n"
"    border-bottom-right-radius:70px;\n"
"    border-bottom-left-radius:70px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:#DAA520;\n"
"}\n"
"")
        self.frSinais.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frSinais.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSinais.setObjectName("frSinais")
        self.pbIgual = QtWidgets.QPushButton(self.frSinais)
        self.pbIgual.setGeometry(QtCore.QRect(280, 390, 250, 50))
        self.pbIgual.setStyleSheet("")
        self.pbIgual.setObjectName("pbIgual")
        self.pb1 = QtWidgets.QPushButton(self.frSinais)
        self.pb1.setGeometry(QtCore.QRect(20, 330, 120, 50))
        self.pb1.setObjectName("pb1")
        self.pbFuncaoSubtracao = QtWidgets.QPushButton(self.frSinais)
        self.pbFuncaoSubtracao.setGeometry(QtCore.QRect(410, 270, 120, 50))
        self.pbFuncaoSubtracao.setObjectName("pbFuncaoSubtracao")
        self.pb4 = QtWidgets.QPushButton(self.frSinais)
        self.pb4.setGeometry(QtCore.QRect(20, 270, 120, 50))
        self.pb4.setObjectName("pb4")
        self.pb5 = QtWidgets.QPushButton(self.frSinais)
        self.pb5.setGeometry(QtCore.QRect(150, 270, 120, 50))
        self.pb5.setObjectName("pb5")
        self.pbFuncaoDivisao = QtWidgets.QPushButton(self.frSinais)
        self.pbFuncaoDivisao.setGeometry(QtCore.QRect(410, 210, 120, 50))
        self.pbFuncaoDivisao.setObjectName("pbFuncaoDivisao")
        self.pbFuncaoSoma = QtWidgets.QPushButton(self.frSinais)
        self.pbFuncaoSoma.setGeometry(QtCore.QRect(410, 330, 120, 50))
        self.pbFuncaoSoma.setObjectName("pbFuncaoSoma")
        self.pbClear = QtWidgets.QPushButton(self.frSinais)
        self.pbClear.setGeometry(QtCore.QRect(20, 150, 120, 50))
        self.pbClear.setObjectName("pbClear")
        self.pb7 = QtWidgets.QPushButton(self.frSinais)
        self.pb7.setGeometry(QtCore.QRect(20, 210, 120, 50))
        self.pb7.setStyleSheet("")
        self.pb7.setObjectName("pb7")
        self.pbPositivoNegativo = QtWidgets.QPushButton(self.frSinais)
        self.pbPositivoNegativo.setGeometry(QtCore.QRect(150, 150, 120, 50))
        self.pbPositivoNegativo.setObjectName("pbPositivoNegativo")
        self.pb9 = QtWidgets.QPushButton(self.frSinais)
        self.pb9.setGeometry(QtCore.QRect(280, 210, 120, 50))
        self.pb9.setStyleSheet("")
        self.pb9.setObjectName("pb9")
        self.pbFuncaoMutiplicacao = QtWidgets.QPushButton(self.frSinais)
        self.pbFuncaoMutiplicacao.setGeometry(QtCore.QRect(410, 150, 120, 50))
        self.pbFuncaoMutiplicacao.setObjectName("pbFuncaoMutiplicacao")
        self.pbPonto = QtWidgets.QPushButton(self.frSinais)
        self.pbPonto.setGeometry(QtCore.QRect(20, 390, 120, 50))
        self.pbPonto.setObjectName("pbPonto")
        self.pb2 = QtWidgets.QPushButton(self.frSinais)
        self.pb2.setGeometry(QtCore.QRect(150, 330, 120, 50))
        self.pb2.setObjectName("pb2")
        self.pb8 = QtWidgets.QPushButton(self.frSinais)
        self.pb8.setGeometry(QtCore.QRect(150, 210, 120, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pb8.setFont(font)
        self.pb8.setObjectName("pb8")
        self.lbMostraConta = QtWidgets.QLabel(self.frSinais)
        self.lbMostraConta.setGeometry(QtCore.QRect(20, 20, 510, 120))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.lbMostraConta.setFont(font)
        self.lbMostraConta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbMostraConta.setText("")
        self.lbMostraConta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbMostraConta.setObjectName("lbMostraConta")
        self.pbFuncaoPorcentagem = QtWidgets.QPushButton(self.frSinais)
        self.pbFuncaoPorcentagem.setGeometry(QtCore.QRect(280, 150, 120, 50))
        self.pbFuncaoPorcentagem.setObjectName("pbFuncaoPorcentagem")
        self.pb3 = QtWidgets.QPushButton(self.frSinais)
        self.pb3.setGeometry(QtCore.QRect(280, 330, 120, 50))
        self.pb3.setObjectName("pb3")
        self.lbContato = QtWidgets.QLabel(self.frSinais)
        self.lbContato.setGeometry(QtCore.QRect(26, 458, 500, 31))
        self.lbContato.setStyleSheet("#lbContato {\n"
"    border: 2px dashed #ffffff;\n"
"    color: #ffffff;\n"
"    border-top-right-radius:0px;\n"
"    border-top-left-radius:0px;\n"
"    border-bottom-right-radius: 30px;\n"
"    border-bottom-left-radius:30px;\n"
"    \n"
"}")
        self.lbContato.setObjectName("lbContato")
        self.pb6 = QtWidgets.QPushButton(self.frSinais)
        self.pb6.setGeometry(QtCore.QRect(280, 270, 120, 50))
        self.pb6.setObjectName("pb6")
        self.pb0 = QtWidgets.QPushButton(self.frSinais)
        self.pb0.setGeometry(QtCore.QRect(150, 390, 120, 50))
        self.pb0.setStyleSheet("")
        self.pb0.setObjectName("pb0")
        self.gridLayout.addWidget(self.frSinais, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbIgual.setText(_translate("MainWindow", "="))
        self.pb1.setText(_translate("MainWindow", "1"))
        self.pbFuncaoSubtracao.setText(_translate("MainWindow", "-"))
        self.pb4.setText(_translate("MainWindow", "4"))
        self.pb5.setText(_translate("MainWindow", "5"))
        self.pbFuncaoDivisao.setText(_translate("MainWindow", "/"))
        self.pbFuncaoSoma.setText(_translate("MainWindow", "+"))
        self.pbClear.setText(_translate("MainWindow", "C"))
        self.pb7.setText(_translate("MainWindow", "7"))
        self.pbPositivoNegativo.setText(_translate("MainWindow", "+/-"))
        self.pb9.setText(_translate("MainWindow", "9"))
        self.pbFuncaoMutiplicacao.setText(_translate("MainWindow", "X"))
        self.pbPonto.setText(_translate("MainWindow", "."))
        self.pb2.setText(_translate("MainWindow", "2"))
        self.pb8.setText(_translate("MainWindow", "8"))
        self.pbFuncaoPorcentagem.setText(_translate("MainWindow", "%"))
        self.pb3.setText(_translate("MainWindow", "3"))
        self.lbContato.setText(_translate("MainWindow", "                                  renan.silva.soares.br@gmail.com"))
        self.pb6.setText(_translate("MainWindow", "6"))
        self.pb0.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
