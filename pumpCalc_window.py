# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wado9\PycharmProjects\EXS_calculator\pumpCalc_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PumpCalcWindow(object):
    def setupUi(self, PumpCalcWindow):
        PumpCalcWindow.setObjectName("PumpCalcWindow")
        PumpCalcWindow.resize(518, 373)
        self.centralwidget = QtWidgets.QWidget(PumpCalcWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutOverall = QtWidgets.QVBoxLayout()
        self.verticalLayoutOverall.setObjectName("verticalLayoutOverall")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.putImageHere = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.putImageHere.sizePolicy().hasHeightForWidth())
        self.putImageHere.setSizePolicy(sizePolicy)
        self.putImageHere.setMinimumSize(QtCore.QSize(200, 80))
        self.putImageHere.setMaximumSize(QtCore.QSize(200, 80))
        self.putImageHere.setBaseSize(QtCore.QSize(200, 80))
        self.putImageHere.setObjectName("putImageHere")
        self.horizontalLayout.addWidget(self.putImageHere)
        self.windowName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowName.sizePolicy().hasHeightForWidth())
        self.windowName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.windowName.setFont(font)
        self.windowName.setObjectName("windowName")
        self.horizontalLayout.addWidget(self.windowName)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.labelCurrentUser = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCurrentUser.sizePolicy().hasHeightForWidth())
        self.labelCurrentUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.labelCurrentUser.setFont(font)
        self.labelCurrentUser.setObjectName("labelCurrentUser")
        self.verticalLayout.addWidget(self.labelCurrentUser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayoutOverall.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutOverall.addItem(spacerItem)
        self.pushButtonClose = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButtonClose.setFont(font)
        self.pushButtonClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.verticalLayoutOverall.addWidget(self.pushButtonClose)
        self.verticalLayout_3.addLayout(self.verticalLayoutOverall)
        PumpCalcWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PumpCalcWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 26))
        self.menubar.setObjectName("menubar")
        PumpCalcWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PumpCalcWindow)
        self.statusbar.setObjectName("statusbar")
        PumpCalcWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PumpCalcWindow)
        QtCore.QMetaObject.connectSlotsByName(PumpCalcWindow)

    def retranslateUi(self, PumpCalcWindow):
        _translate = QtCore.QCoreApplication.translate
        PumpCalcWindow.setWindowTitle(_translate("PumpCalcWindow", "?????????????????????? ??????"))
        self.putImageHere.setText(_translate("PumpCalcWindow", "??????????????"))
        self.windowName.setText(_translate("PumpCalcWindow", "???????????? ??????"))
        self.label.setText(_translate("PumpCalcWindow", "?????? ????????????????????????"))
        self.labelCurrentUser.setText(_translate("PumpCalcWindow", "????????????????"))
        self.pushButtonClose.setText(_translate("PumpCalcWindow", "??????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PumpCalcWindow = QtWidgets.QMainWindow()
    ui = Ui_PumpCalcWindow()
    ui.setupUi(PumpCalcWindow)
    PumpCalcWindow.show()
    sys.exit(app.exec_())
