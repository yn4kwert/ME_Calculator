# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wado9\PycharmProjects\EXS_calculator\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 470)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutOverall = QtWidgets.QVBoxLayout()
        self.verticalLayoutOverall.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayoutOverall.setSpacing(20)
        self.verticalLayoutOverall.setObjectName("verticalLayoutOverall")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(14)
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
        self.windowName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowName.sizePolicy().hasHeightForWidth())
        self.windowName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.windowName.setFont(font)
        self.windowName.setAlignment(QtCore.Qt.AlignCenter)
        self.windowName.setObjectName("windowName")
        self.horizontalLayout.addWidget(self.windowName)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
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
        self.label.setAlignment(QtCore.Qt.AlignCenter)
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
        self.labelCurrentUser.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCurrentUser.setObjectName("labelCurrentUser")
        self.verticalLayout.addWidget(self.labelCurrentUser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayoutOverall.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayoutOverall.addItem(spacerItem)
        self.pushButtonChiefTech = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonChiefTech.sizePolicy().hasHeightForWidth())
        self.pushButtonChiefTech.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonChiefTech.setFont(font)
        self.pushButtonChiefTech.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonChiefTech.setObjectName("pushButtonChiefTech")
        self.verticalLayoutOverall.addWidget(self.pushButtonChiefTech)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutOverall.addItem(spacerItem1)
        self.pushButtonChekConstValues = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonChekConstValues.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonChekConstValues.sizePolicy().hasHeightForWidth())
        self.pushButtonChekConstValues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonChekConstValues.setFont(font)
        self.pushButtonChekConstValues.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonChekConstValues.setObjectName("pushButtonChekConstValues")
        self.verticalLayoutOverall.addWidget(self.pushButtonChekConstValues)
        self.pushButtonAboutProg = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAboutProg.sizePolicy().hasHeightForWidth())
        self.pushButtonAboutProg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAboutProg.setFont(font)
        self.pushButtonAboutProg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAboutProg.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButtonAboutProg.setObjectName("pushButtonAboutProg")
        self.verticalLayoutOverall.addWidget(self.pushButtonAboutProg)
        self.pushButtonPumpCalc = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPumpCalc.sizePolicy().hasHeightForWidth())
        self.pushButtonPumpCalc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPumpCalc.setFont(font)
        self.pushButtonPumpCalc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonPumpCalc.setObjectName("pushButtonPumpCalc")
        self.verticalLayoutOverall.addWidget(self.pushButtonPumpCalc)
        self.verticalLayout_3.addLayout(self.verticalLayoutOverall)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????? ????????"))
        self.putImageHere.setText(_translate("MainWindow", "??????????????"))
        self.windowName.setText(_translate("MainWindow", "?????????????? ????????"))
        self.label.setText(_translate("MainWindow", "?????? ????????????????????????:"))
        self.labelCurrentUser.setText(_translate("MainWindow", "????????????????"))
        self.pushButtonChiefTech.setText(_translate("MainWindow", "?????????? \"?????????????? ????????????????\""))
        self.pushButtonChekConstValues.setText(_translate("MainWindow", "?????????????????????? ??????????????????"))
        self.pushButtonAboutProg.setText(_translate("MainWindow", "?? ??????????????????"))
        self.pushButtonPumpCalc.setText(_translate("MainWindow", "???????????? ??????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
