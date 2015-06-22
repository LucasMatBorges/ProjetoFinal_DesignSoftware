# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
total=0
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
        self.ThirdColor5.currentIndexChanged.connect(self.Total5)
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
        self.FourthColor5.currentIndexChanged.connect(self.Total5)
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
        self.FirstColor4.currentIndexChanged.connect(self.Total4)
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
        self.SecondColor4.currentIndexChanged.connect(self.Total4)
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
        self.ThirdColor4.currentIndexChanged.connect(self.Total4)
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
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.ThirdColor4.addItem(_fromUtf8(""))
        self.FourthColor4 = QtGui.QComboBox(ResistorLab)
        self.FourthColor4.currentIndexChanged.connect(self.Tolerancia4)
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
        self.FirstColor5.currentIndexChanged.connect(self.Total5)
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
        self.SecondColor5.currentIndexChanged.connect(self.Total5)
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
        self.FifthColor5.currentIndexChanged.connect(self.Tolerancia5)
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
        self.ThirdColor4.setItemText(0, _translate("ResistorLab", "PRETO", None))
        self.ThirdColor4.setItemText(1, _translate("ResistorLab", "MARROM", None))
        self.ThirdColor4.setItemText(2, _translate("ResistorLab", "VERMELHO", None))
        self.ThirdColor4.setItemText(3, _translate("ResistorLab", "LARANJA", None))
        self.ThirdColor4.setItemText(4, _translate("ResistorLab", "AMARELO", None))
        self.ThirdColor4.setItemText(5, _translate("ResistorLab", "VERDE", None))
        self.ThirdColor4.setItemText(6, _translate("ResistorLab", "AZUL", None))
        self.ThirdColor4.setItemText(7, _translate("ResistorLab", "VIOLETA", None))
        self.ThirdColor4.setItemText(8, _translate("ResistorLab", "DOURADO", None))
        self.ThirdColor4.setItemText(9, _translate("ResistorLab", "PRATEADO", None))
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

    def Total4(self):
        total1=0
        cor1 = self.FirstColor4.currentIndex()    
        if cor1==0:
            total1+=0
        elif cor1==1:
            total1+=10
        elif cor1==2:
            total1+=20    
        elif cor1==3:
            total1+=30
        elif cor1==4:
            total1+=40
        elif cor1==5:
            total1+=50        
        elif cor1==6:
            total1+=60
        elif cor1==7:
            total1+=70        
        elif cor1==8:
            total1+=80
        elif cor1==9:
            total1+=90
        total2=0
        cor2 = self.SecondColor4.currentIndex()            
        if cor2==0:
            total2+=0
        elif cor2==1:
            total2+=1
        elif cor2==2:
            total2+=2
        elif cor2==3:
            total2+=3      
        elif cor2==4:
            total2+=4
        elif cor2==5:
            total2+=5
        elif cor2==6:
            total2+=6
        elif cor2==7:
            total2+=7
        elif cor2==8:
            total2+=8
        elif cor2==9:
            total2+=9
        multiplicador= self.ThirdColor4.currentIndex()
        if multiplicador==0:
            mult = 1
        elif multiplicador==1:
            mult=10
        elif multiplicador==2:
            mult=100
        elif multiplicador==3:
            mult=1000
        elif multiplicador==4:
            mult=10000
        elif multiplicador==5:
            mult=100000
        elif multiplicador==6:
            mult=1000000
        elif multiplicador==7:
            mult=10000000
        elif multiplicador==8:
            mult=0.1
        elif multiplicador==9:
            mult=0.01         
        total = (total1 + total2)*mult
        self.Result4cores.setStyleSheet('color: black')        
        self.Result4cores.setText('{0}'.format(total))          
        
    def Tolerancia4(self):
        tolerancia = self.FourthColor4.currentIndex()
        if tolerancia==0:
            toleran=1
        elif tolerancia==1:
            toleran=2
        elif tolerancia==2:
            toleran=0.5
        elif tolerancia==3:
            toleran=0.25
        elif tolerancia==4:
            toleran=0.1
        elif tolerancia==5:
            toleran=0.05
        elif tolerancia==6:
            toleran=5
        elif tolerancia==7:
            toleran=10  
        self.Result5cores_3.setStyleSheet('color: black')        
        self.Result5cores_3.setText('{0}'.format(toleran)) 
        
    def Total5(self):
        total1=0
        cor1 = self.FirstColor5.currentIndex()    
        if cor1==0:
            total1+=0
        elif cor1==1:
            total1+=100
        elif cor1==2:
            total1+=200    
        elif cor1==3:
            total1+=300
        elif cor1==4:
            total1+=400
        elif cor1==5:
            total1+=500        
        elif cor1==6:
            total1+=600
        elif cor1==7:
            total1+=700        
        elif cor1==8:
            total1+=800
        elif cor1==9:
            total1+=900
        total2=0
        cor2 = self.SecondColor5.currentIndex()            
        if cor2==0:
            total2+=0
        elif cor2==1:
            total2+=10
        elif cor2==2:
            total2+=20
        elif cor2==3:
            total2+=30        
        elif cor2==4:
            total2+=40
        elif cor2==5:
            total2+=50
        elif cor2==6:
            total2+=60
        elif cor2==7:
            total2+=70
        elif cor2==8:
            total2+=80
        elif cor2==9:
            total2+=90
        total3=0
        cor3 = self.ThirdColor5.currentIndex()            
        if cor3==0:
            total3+=0
        elif cor3==1:
            total3+=10
        elif cor3==2:
            total3+=20
        elif cor3==3:
            total3+=30        
        elif cor3==4:
            total3+=40
        elif cor3==5:
            total3+=50
        elif cor3==6:
            total3+=60
        elif cor3==7:
            total3+=70
        elif cor3==8:
            total3+=80
        elif cor3==9:
            total3+=90
        multiplicador= self.FourthColor5.currentIndex()
        if multiplicador==0:
            mult = 1
        elif multiplicador==1:
            mult=10
        elif multiplicador==2:
            mult=100
        elif multiplicador==3:
            mult=1000
        elif multiplicador==4:
            mult=10000
        elif multiplicador==5:
            mult=100000
        elif multiplicador==6:
            mult=1000000
        elif multiplicador==7:
            mult=10000000
        elif multiplicador==8:
            mult=0.1
        elif multiplicador==9:
            mult=0.01         
        total = (total1 + total2 + total3)*mult
        self.Result5cores.setStyleSheet('color: black')        
        self.Result5cores.setText('{0}'.format(total))          
        
    def Tolerancia5(self):
        tolerancia = self.FifthColor5.currentIndex()
        if tolerancia==0:
            toleran=1
        elif tolerancia==1:
            toleran=2
        elif tolerancia==2:
            toleran=0.5
        elif tolerancia==3:
            toleran=0.25
        elif tolerancia==4:
            toleran=0.1
        elif tolerancia==5:
            toleran=0.05
        elif tolerancia==6:
            toleran=5
        elif tolerancia==7:
            toleran=10  
        self.Result5cores_2.setStyleSheet('color: black')        
        self.Result5cores_2.setText('{0}'.format(toleran)) 
        
print("Rodou com sucesso")        
if __name__	== "__main__":	
	app	=     QtGui.QApplication(sys.argv)	
	win	=	Ui_ResistorLab()	
	win.show()	
	sys.exit(app.exec_())
