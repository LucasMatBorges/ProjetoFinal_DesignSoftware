# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignCircuit.ui'
#
# Created: Mon Jun 15 09:47:52 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
ok="teste"
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ResistorLab(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, ResistorLab):
        ResistorLab.setObjectName(_fromUtf8("ResistorLab"))
        ResistorLab.resize(384, 424)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        ResistorLab.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS UI Gothic"))
        ResistorLab.setFont(font)
        self.ThirdColor5 = QtGui.QComboBox(ResistorLab)
        self.ThirdColor5.setGeometry(QtCore.QRect(260, 100, 69, 22))
        self.ThirdColor5.setObjectName(_fromUtf8("ThirdColor5"))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.ThirdColor5.addItem(_fromUtf8(""))
        self.FourthColor5 = QtGui.QComboBox(ResistorLab)
        self.FourthColor5.setGeometry(QtCore.QRect(100, 130, 69, 22))
        self.FourthColor5.setObjectName(_fromUtf8("FourthColor5"))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.FourthColor5.addItem(_fromUtf8(""))
        self.Cores4 = QtGui.QLabel(ResistorLab)
        self.Cores4.setGeometry(QtCore.QRect(150, 190, 181, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Levenim MT"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Cores4.setFont(font)
        self.Cores4.setTextFormat(QtCore.Qt.PlainText)
        self.Cores4.setObjectName(_fromUtf8("Cores4"))
        self.Cores5 = QtGui.QLabel(ResistorLab)
        self.Cores5.setGeometry(QtCore.QRect(140, 30, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Eras Demi ITC"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Cores5.setFont(font)
        self.Cores5.setObjectName(_fromUtf8("Cores5"))
        self.FirstColor4 = QtGui.QComboBox(ResistorLab)
        self.FirstColor4.currentIndexChanged.connect(self.teste)
        self.FirstColor4.setGeometry(QtCore.QRect(120, 240, 69, 22))
        self.FirstColor4.setObjectName(_fromUtf8("FirstColor4"))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.FirstColor4.addItem(_fromUtf8(""))
        self.SecondColor4 = QtGui.QComboBox(ResistorLab)
        self.SecondColor4.currentIndexChanged.connect(self.teste2)
        self.SecondColor4.setGeometry(QtCore.QRect(200, 240, 69, 22))
        self.SecondColor4.setObjectName(_fromUtf8("SecondColor4"))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.SecondColor4.addItem(_fromUtf8(""))
        self.Titulo = QtGui.QLabel(ResistorLab)
        self.Titulo.setGeometry(QtCore.QRect(100, 0, 201, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KaiTi"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setObjectName(_fromUtf8("Titulo"))
        self.ThirdColor4 = QtGui.QComboBox(ResistorLab)
        self.ThirdColor4.currentIndexChanged.connect(self.teste3)
        self.ThirdColor4.setGeometry(QtCore.QRect(110, 280, 69, 22))
        self.ThirdColor4.setObjectName(_fromUtf8("ThirdColor4"))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.FourthColor4 = QtGui.QComboBox(ResistorLab)
        self.FourthColor4.currentIndexChanged.connect(self.teste4)
        self.FourthColor4.setGeometry(QtCore.QRect(220, 280, 69, 22))
        self.FourthColor4.setObjectName(_fromUtf8("FourthColor4"))
        self.FourthColor4.addItem(_fromUtf8(""))
        self.FourthColor4.addItem(_fromUtf8(""))
        self.FourthColor4.addItem(_fromUtf8(""))
        self.FourthColor4.addItem(_fromUtf8(""))
        self.FourthColor4.addItem(_fromUtf8(""))
        self.FourthColor4.addItem(_fromUtf8(""))
        self.FourthColor4.addItem(_fromUtf8(""))
        self.FourthColor4.addItem(_fromUtf8(""))
        self.FirstColor5 = QtGui.QComboBox(ResistorLab)
        self.FirstColor5.setGeometry(QtCore.QRect(60, 100, 69, 22))
        self.FirstColor5.setObjectName(_fromUtf8("FirstColor5"))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.FirstColor5.addItem(_fromUtf8(""))
        self.SecondColor5 = QtGui.QComboBox(ResistorLab)
        self.SecondColor5.setGeometry(QtCore.QRect(160, 100, 69, 22))
        self.SecondColor5.setObjectName(_fromUtf8("SecondColor5"))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.SecondColor5.addItem(_fromUtf8(""))
        self.FifthColor5 = QtGui.QComboBox(ResistorLab)
        self.FifthColor5.setGeometry(QtCore.QRect(220, 130, 69, 22))
        self.FifthColor5.setObjectName(_fromUtf8("FifthColor5"))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.FifthColor5.addItem(_fromUtf8(""))
        self.Result5cores = QtGui.QPushButton(ResistorLab)
        self.Result5cores.setDisabled(True)
        self.Result5cores.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.Result5cores.setCheckable(False)
        self.Result5cores.setDefault(False)
        self.Result5cores.setObjectName(_fromUtf8("Result5cores"))
        self.Result4cores = QtGui.QPushButton(ResistorLab)
        self.Result4cores.setDisabled(True)
        self.Result4cores.setGeometry(QtCore.QRect(100, 340, 75, 23))
        self.Result4cores.setAutoDefault(True)
        self.Result4cores.setDefault(False)
        self.Result4cores.setObjectName(_fromUtf8("Result4cores"))
        self.Result5cores_2 = QtGui.QPushButton(ResistorLab)
        self.Result5cores_2.setDisabled(True)
        self.Result5cores_2.setGeometry(QtCore.QRect(200, 160, 75, 23))
        self.Result5cores_2.setCheckable(False)
        self.Result5cores_2.setDefault(False)
        self.Result5cores_2.setObjectName(_fromUtf8("Result5cores_2"))
        self.Result5cores_3 = QtGui.QPushButton(ResistorLab)
        self.Result5cores_3.setDisabled(True)
        self.Result5cores_3.setGeometry(QtCore.QRect(220, 340, 75, 23))
        self.Result5cores_3.setCheckable(False)
        self.Result5cores_3.setDefault(False)
        self.Result5cores_3.setObjectName(_fromUtf8("Result5cores_3"))

        self.retranslateUi(ResistorLab)
        QtCore.QMetaObject.connectSlotsByName(ResistorLab)

    def retranslateUi(self, ResistorLab):
        ResistorLab.setWindowTitle(_translate("ResistorLab", "WizardPage", None))
        self.ThirdColor5.setItemText(0, _translate("ResistorLab", "PRETO", None))
        self.ThirdColor5.setItemText(1, _translate("ResistorLab", "MARROM", None))
        self.ThirdColor5.setItemText(2, _translate("ResistorLab", "VERMELHO", None))
        self.ThirdColor5.setItemText(3, _translate("ResistorLab", "LARANJA", None))
        self.ThirdColor5.setItemText(4, _translate("ResistorLab", "AMARELO", None))
        self.ThirdColor5.setItemText(5, _translate("ResistorLab", "VERDE", None))
        self.ThirdColor5.setItemText(6, _translate("ResistorLab", "AZUL", None))
        self.ThirdColor5.setItemText(7, _translate("ResistorLab", "VIOLETA", None))
        self.ThirdColor5.setItemText(8, _translate("ResistorLab", "CINZA", None))
        self.ThirdColor5.setItemText(9, _translate("ResistorLab", "BRANCO", None))
        self.FourthColor5.setItemText(0, _translate("ResistorLab", "PRETO", None))
        self.FourthColor5.setItemText(1, _translate("ResistorLab", "MARROM", None))
        self.FourthColor5.setItemText(2, _translate("ResistorLab", "VERMELHO", None))
        self.FourthColor5.setItemText(3, _translate("ResistorLab", "LARANJA", None))
        self.FourthColor5.setItemText(4, _translate("ResistorLab", "AMARELO", None))
        self.FourthColor5.setItemText(5, _translate("ResistorLab", "VERDE", None))
        self.FourthColor5.setItemText(6, _translate("ResistorLab", "AZUL", None))
        self.FourthColor5.setItemText(7, _translate("ResistorLab", "VIOLETA", None))
        self.FourthColor5.setItemText(8, _translate("ResistorLab", "DOURADO", None))
        self.FourthColor5.setItemText(9, _translate("ResistorLab", "PRATEADO", None))
        self.Cores4.setText(_translate("ResistorLab", "4 CORES", None))
        self.Cores5.setText(_translate("ResistorLab", "5 CORES", None))
        self.FirstColor4.setItemText(0, _translate("ResistorLab", "PRETO", None))
        self.FirstColor4.setItemText(1, _translate("ResistorLab", "MARROM", None))
        self.FirstColor4.setItemText(2, _translate("ResistorLab", "VERMELHO", None))
        self.FirstColor4.setItemText(3, _translate("ResistorLab", "LARANJA", None))
        self.FirstColor4.setItemText(4, _translate("ResistorLab", "AMARELO", None))
        self.FirstColor4.setItemText(5, _translate("ResistorLab", "VERDE", None))
        self.FirstColor4.setItemText(6, _translate("ResistorLab", "AZUL", None))
        self.FirstColor4.setItemText(7, _translate("ResistorLab", "VIOLETA", None))
        self.FirstColor4.setItemText(8, _translate("ResistorLab", "CINZA", None))
        self.FirstColor4.setItemText(9, _translate("ResistorLab", "BRANCO", None))
        self.SecondColor4.setItemText(0, _translate("ResistorLab", "PRETO", None))
        self.SecondColor4.setItemText(1, _translate("ResistorLab", "MARROM", None))
        self.SecondColor4.setItemText(2, _translate("ResistorLab", "VERMELHO", None))
        self.SecondColor4.setItemText(3, _translate("ResistorLab", "LARANJA", None))
        self.SecondColor4.setItemText(4, _translate("ResistorLab", "AMARELO", None))
        self.SecondColor4.setItemText(5, _translate("ResistorLab", "VERDE", None))
        self.SecondColor4.setItemText(6, _translate("ResistorLab", "AZUL", None))
        self.SecondColor4.setItemText(7, _translate("ResistorLab", "VIOLETA", None))
        self.SecondColor4.setItemText(8, _translate("ResistorLab", "CINZA", None))
        self.SecondColor4.setItemText(9, _translate("ResistorLab", "BRANCO", None))
        self.Titulo.setText(_translate("ResistorLab", "Resistor Lab", None))
        self.ThirdColor4.setItemText(0, _translate("ResistorLab", "MARROM", None))
        self.ThirdColor4.setItemText(1, _translate("ResistorLab", "VERMELHO", None))
        self.ThirdColor4.setItemText(2, _translate("ResistorLab", "VERDE", None))
        self.ThirdColor4.setItemText(3, _translate("ResistorLab", "AZUL", None))
        self.ThirdColor4.setItemText(4, _translate("ResistorLab", "VIOLETA", None))
        self.ThirdColor4.setItemText(5, _translate("ResistorLab", "CINZA", None))
        self.ThirdColor4.setItemText(6, _translate("ResistorLab", "DOURADO", None))
        self.ThirdColor4.setItemText(7, _translate("ResistorLab", "PRATEADO", None))
        self.FourthColor4.setItemText(0, _translate("ResistorLab", "MARROM", None))
        self.FourthColor4.setItemText(1, _translate("ResistorLab", "VERMELHO", None))
        self.FourthColor4.setItemText(2, _translate("ResistorLab", "VERDE", None))
        self.FourthColor4.setItemText(3, _translate("ResistorLab", "AZUL", None))
        self.FourthColor4.setItemText(4, _translate("ResistorLab", "VIOLETA", None))
        self.FourthColor4.setItemText(5, _translate("ResistorLab", "CINZA", None))
        self.FourthColor4.setItemText(6, _translate("ResistorLab", "DOURADO", None))
        self.FourthColor4.setItemText(7, _translate("ResistorLab", "PRATEADO", None))
        self.FirstColor5.setItemText(0, _translate("ResistorLab", "PRETO", None))
        self.FirstColor5.setItemText(1, _translate("ResistorLab", "MARROM", None))
        self.FirstColor5.setItemText(2, _translate("ResistorLab", "VERMELHO", None))
        self.FirstColor5.setItemText(3, _translate("ResistorLab", "LARANJA", None))
        self.FirstColor5.setItemText(4, _translate("ResistorLab", "AMARELO", None))
        self.FirstColor5.setItemText(5, _translate("ResistorLab", "VERDE", None))
        self.FirstColor5.setItemText(6, _translate("ResistorLab", "AZUL", None))
        self.FirstColor5.setItemText(7, _translate("ResistorLab", "VIOLETA", None))
        self.FirstColor5.setItemText(8, _translate("ResistorLab", "CINZA", None))
        self.FirstColor5.setItemText(9, _translate("ResistorLab", "BRANCO", None))
        self.SecondColor5.setItemText(0, _translate("ResistorLab", "PRETO", None))
        self.SecondColor5.setItemText(1, _translate("ResistorLab", "MARROM", None))
        self.SecondColor5.setItemText(2, _translate("ResistorLab", "VERMELHO", None))
        self.SecondColor5.setItemText(3, _translate("ResistorLab", "LARANJA", None))
        self.SecondColor5.setItemText(4, _translate("ResistorLab", "AMARELO", None))
        self.SecondColor5.setItemText(5, _translate("ResistorLab", "VERDE", None))
        self.SecondColor5.setItemText(6, _translate("ResistorLab", "AZUL", None))
        self.SecondColor5.setItemText(7, _translate("ResistorLab", "VIOLETA", None))
        self.SecondColor5.setItemText(8, _translate("ResistorLab", "CINZA", None))
        self.SecondColor5.setItemText(9, _translate("ResistorLab", "BRANCO", None))
        self.FifthColor5.setItemText(0, _translate("ResistorLab", "PRETO", None))
        self.FifthColor5.setItemText(1, _translate("ResistorLab", "MARROM", None))
        self.FifthColor5.setItemText(2, _translate("ResistorLab", "VERMELHO", None))
        self.FifthColor5.setItemText(3, _translate("ResistorLab", "LARANJA", None))
        self.FifthColor5.setItemText(4, _translate("ResistorLab", "AMARELO", None))
        self.FifthColor5.setItemText(5, _translate("ResistorLab", "VERDE", None))
        self.FifthColor5.setItemText(6, _translate("ResistorLab", "AZUL", None))
        self.FifthColor5.setItemText(7, _translate("ResistorLab", "VIOLETA", None))
        self.FifthColor5.setItemText(8, _translate("ResistorLab", "DOURADO", None))
        self.FifthColor5.setItemText(9, _translate("ResistorLab", "PRATEADO", None))
        self.Result5cores.setText(_translate("ResistorLab", "Valor ", None))
        self.Result4cores.setText(_translate("ResistorLab", "Valor", None))
        self.Result5cores_2.setText(_translate("ResistorLab", "Tolerância", None))
        self.Result5cores_3.setText(_translate("ResistorLab", "Tolerância", None))
    
    def teste(self):
        print(self.FirstColor4.currentIndex())
        self.botao = QtGui.QPushButton()
        self.botao.setDisabled(True)
        self.botao.setText('{0}'.format(50))
        self.botao.setStyleSheet('color: black')
    
    def teste2(self):
        print(self.SecondColor4.currentIndex())
        self.botao = QtGui.QPushButton()
        self.botao.setDisabled(True)
        self.botao.setText('{0}'.format(50))
        self.botao.setStyleSheet('color: black')
    
    def teste3(self):
        print(self.ThirdColor4.currentIndex())
        self.botao = QtGui.QPushButton()
        self.botao.setDisabled(True)
        self.botao.setText('{0}'.format(50))
        self.botao.setStyleSheet('color: black')
    
    def teste4(self):
        print(self.FourthColor4.currentIndex())        
        self.Result4cores.setStyleSheet('color: black')        
        self.Result4cores.setText('{0}'.format(self.FourthColor4.currentIndex()))
        

if __name__	== "__main__":	
	app	=     QtGui.QApplication(sys.argv)	
	win	=	Ui_ResistorLab()	
	win.show()	
	sys.exit(app.exec_())