from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt6.QtCore import QRect, QCoreApplication


class UiLoginWindow(object):
    def setup_ui(self, login_window):
        if not login_window.objectName():
            login_window.setObjectName(u"LoginWindow")
        login_window.resize(316, 123)
        self.LoginButton = QPushButton(login_window)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(20, 90, 75, 24))
        self.CancelButton = QPushButton(login_window)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(100, 90, 75, 24))
        self.NewUser = QPushButton(login_window)
        self.NewUser.setObjectName(u"NewUser")
        self.NewUser.setGeometry(QRect(220, 90, 91, 24))
        self.UserName = QLineEdit(login_window)
        self.UserName.setObjectName(u"UserName")
        self.UserName.setGeometry(QRect(111, 11, 133, 22))
        self.LabelUserName = QLabel(login_window)
        self.LabelUserName.setObjectName(u"LabelUserName")
        self.LabelUserName.setGeometry(QRect(41, 11, 65, 16))
        self.LabelUserPassword = QLabel(login_window)
        self.LabelUserPassword.setObjectName(u"LabelUserPassword")
        self.LabelUserPassword.setGeometry(QRect(41, 39, 42, 16))
        self.UserPassword = QLineEdit(login_window)
        self.UserPassword.setObjectName(u"UserPassword")
        self.UserPassword.setGeometry(QRect(111, 39, 133, 22))

        self.retranslate_ui(login_window)
        self.CancelButton.clicked.connect(login_window.close)

    def retranslate_ui(self, login_window):
        login_window.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Widget", None))
        # self.LoginButton.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u0445\u043e\u0434", None))
        self.LoginButton.setText(QCoreApplication.translate("LoginWindow", "Вход", None))
        self.CancelButton.setText(QCoreApplication.translate("LoginWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430",
                                                             None))
        self.NewUser.setText(QCoreApplication.translate("LoginWindow", u"\u041d\u043e\u0432\u044b\u0439"
                                                                       u" \u0438\u0433\u0440\u043e\u043a", None))
        self.LabelUserName.setText(QCoreApplication.translate("LoginWindow", u"\u0418\u043c\u044f"
                                                                u" \u0438\u0433\u0440\u043e\u043a\u0430", None))
        self.LabelUserPassword.setText(QCoreApplication.translate("LoginWindow",
                                                                  u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
