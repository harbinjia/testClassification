# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 513)
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(230, 350, 91, 26))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.result = QtWidgets.QTextBrowser(Form)
        self.result.setGeometry(QtCore.QRect(360, 170, 221, 311))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 40, 331, 31))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sub = QtWidgets.QPushButton(Form)
        self.sub.setGeometry(QtCore.QRect(80, 350, 91, 26))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.sub.setFont(font)
        self.sub.setObjectName("sub")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sele = QtWidgets.QPushButton(Form)
        self.sele.setGeometry(QtCore.QRect(230, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.sele.setFont(font)
        self.sele.setObjectName("sele")
        self.introduce = QtWidgets.QPushButton(Form)
        self.introduce.setGeometry(QtCore.QRect(70, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.introduce.setFont(font)
        self.introduce.setObjectName("introduce")

        self.retranslateUi(Form)
        self.sele.clicked.connect(Form.choose)
        self.sub.clicked.connect(Form.select)
        self.clear.clicked.connect(self.result.clear)
        self.introduce.clicked.connect(Form.do_show)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.sub, self.result)
        Form.setTabOrder(self.result, self.clear)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.clear.setText(_translate("Form", "清空"))
        self.label_2.setText(_translate("Form", "结果显示："))
        self.label_3.setText(_translate("Form", "MOOC平台讨论问题文本分类"))
        self.sub.setText(_translate("Form", "查询"))
        self.label.setText(_translate("Form", "请选择测试文本:"))
        self.sele.setText(_translate("Form", "choose"))
        self.introduce.setText(_translate("Form", "使用说明"))

