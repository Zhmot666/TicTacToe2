import sys
from PyQt6 import QtWidgets
import main_window
import login
import db_client


class LoginWindow(QtWidgets.QMainWindow, login.UiLoginWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui(self)
        self.setWindowTitle('TicTacToe - Логин')

    def press_login(self):
        # if connection_db.verify_user():
        pass

    def press_new_user(self):
        pass

    def press_cancel(self):
        pass


class MainApp(QtWidgets.QMainWindow, main_window.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TicTacToe 2')
        self.buttons = [child for child in self.groupBox.children() if child.objectName().find('pushButton') != -1]
        for but in self.buttons:
            but.clicked.connect(self.on_button_clicked)
        connection_db = db_client.SqliteDB()
        self.login(connection_db)


    def login(self, connection_db):
        log_win = LoginWindow(self)
        log_win.show()

    def on_button_clicked(self):
        button = self.sender()
        button.setDisabled(True)

    def reset_button(self):
        self.buttons = [child for child in self.groupBox.children() if child.objectName().find('pushButton') != -1]
        for but in self.buttons:
            but.setText('')
            but.setDisabled(False)
            but.setDown(False)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
