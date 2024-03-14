from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(400, 300))
        Frame.setMaximumSize(QtCore.QSize(400, 300))
        Frame.setBaseSize(QtCore.QSize(400, 300))
        self.groupBox = QtWidgets.QGroupBox(parent=Frame)
        self.groupBox.setGeometry(QtCore.QRect(100, 90, 191, 201))
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButton11 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton11.setGeometry(QtCore.QRect(10, 20, 50, 50))
        self.pushButton11.setCheckable(True)
        self.pushButton11.setObjectName("pushButton11")
        self.pushButton12 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton12.setGeometry(QtCore.QRect(70, 20, 50, 50))
        self.pushButton12.setCheckable(True)
        self.pushButton12.setObjectName("pushButton12")
        self.pushButton13 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton13.setGeometry(QtCore.QRect(130, 20, 50, 50))
        self.pushButton13.setText("")
        self.pushButton13.setCheckable(True)
        self.pushButton13.setObjectName("pushButton13")
        self.pushButton21 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton21.setGeometry(QtCore.QRect(10, 80, 50, 50))
        self.pushButton21.setText("")
        self.pushButton21.setCheckable(True)
        self.pushButton21.setObjectName("pushButton21")
        self.pushButton22 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton22.setGeometry(QtCore.QRect(70, 80, 50, 50))
        self.pushButton22.setText("")
        self.pushButton22.setCheckable(True)
        self.pushButton22.setObjectName("pushButton22")
        self.pushButton23 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton23.setGeometry(QtCore.QRect(130, 80, 50, 50))
        self.pushButton23.setText("")
        self.pushButton23.setCheckable(True)
        self.pushButton23.setObjectName("pushButton23")
        self.pushButton31 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton31.setGeometry(QtCore.QRect(10, 140, 50, 50))
        self.pushButton31.setText("")
        self.pushButton31.setCheckable(True)
        self.pushButton31.setObjectName("pushButton31")
        self.pushButton32 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton32.setGeometry(QtCore.QRect(70, 140, 50, 50))
        self.pushButton32.setText("")
        self.pushButton32.setCheckable(True)
        self.pushButton32.setObjectName("pushButton32")
        self.pushButton33 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton33.setGeometry(QtCore.QRect(130, 140, 50, 50))
        self.pushButton33.setText("")
        self.pushButton33.setCheckable(True)
        self.pushButton33.setObjectName("pushButton33")
        self.PlayerName = QtWidgets.QLabel(parent=Frame)
        self.PlayerName.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PlayerName.setFont(font)
        self.PlayerName.setObjectName("PlayerName")
        self.ComputerName = QtWidgets.QLabel(parent=Frame)
        self.ComputerName.setGeometry(QtCore.QRect(280, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ComputerName.setFont(font)
        self.ComputerName.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ComputerName.setObjectName("ComputerName")
        self.PlayerScore = QtWidgets.QLabel(parent=Frame)
        self.PlayerScore.setGeometry(QtCore.QRect(130, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PlayerScore.setFont(font)
        self.PlayerScore.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.PlayerScore.setScaledContents(False)
        self.PlayerScore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PlayerScore.setObjectName("PlayerScore")
        self.Colon = QtWidgets.QLabel(parent=Frame)
        self.Colon.setGeometry(QtCore.QRect(180, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Colon.setFont(font)
        self.Colon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Colon.setObjectName("Colon")
        self.ComputerScore = QtWidgets.QLabel(parent=Frame)
        self.ComputerScore.setGeometry(QtCore.QRect(220, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ComputerScore.setFont(font)
        self.ComputerScore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ComputerScore.setObjectName("ComputerScore")
        self.ComputerMark = QtWidgets.QLabel(parent=Frame)
        self.ComputerMark.setGeometry(QtCore.QRect(310, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ComputerMark.setFont(font)
        self.ComputerMark.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.ComputerMark.setScaledContents(False)
        self.ComputerMark.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ComputerMark.setObjectName("ComputerMark")
        self.PlayerMark = QtWidgets.QLabel(parent=Frame)
        self.PlayerMark.setGeometry(QtCore.QRect(50, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PlayerMark.setFont(font)
        self.PlayerMark.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.PlayerMark.setScaledContents(False)
        self.PlayerMark.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PlayerMark.setObjectName("PlayerMark")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "TicTacToe"))
        self.groupBox.setTitle(_translate("Frame", "Игровое поле"))
        self.pushButton11.setText(_translate("Frame", ""))
        self.pushButton12.setText(_translate("Frame", ""))
        self.PlayerName.setText(_translate("Frame", "ИГРОК"))
        self.ComputerName.setText(_translate("Frame", "3Ton"))
        self.PlayerScore.setText(_translate("Frame", ""))
        self.Colon.setText(_translate("Frame", ":"))
        self.ComputerScore.setText(_translate("Frame", ""))
        self.ComputerMark.setText(_translate("Frame", ""))
        self.PlayerMark.setText(_translate("Frame", ""))
