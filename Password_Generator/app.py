import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

import button
import password
from ui.ui_main import Ui_MainWindow



class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_slider_to_spinbox()
        self.set_password() 
        self.password_edit() 

        for btn in button.GENERATE_PASSWORD:
            getattr(self.ui, btn).clicked.connect(self.set_password)

        self.ui.btn_visibility.clicked.connect(self.change_visibility_password)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

    def connect_slider_to_spinbox(self) -> None:
        self.ui.slider_length.valueChanged.connect(self.ui.spinbox_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.ui.slider_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.set_password)

    def password_edit(self) -> None:
        self.ui.lineEdit.textChanged.connect(self.set_strength)

    def get_characters(self) -> str:
        chars = ''
        for btn in button.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value
        return chars

    def set_password(self) -> None:
        try:
            self.ui.lineEdit.setText(
        password.create_new(
            length=self.ui.slider_length.value(), characters=self.get_characters()
        )
        )
        except IndexError:
            self.ui.lineEdit.clear()

        self.set_strength()

    def get_character_number(self) -> int:
        num = 0
        for btn in button.CHARACTER_NUMBER.items():
            if getattr(self.ui, btn[0]).isChecked():
                num += btn[1]
        return num

    def set_strength(self) -> None:
        password_text = self.ui.lineEdit.text()
        length = len(password_text)
        char_num = self.get_character_number()

        entropy = password.get_entropy(length, char_num)

        for strength in password.StrenthToEntropy:
            if entropy >= strength.value:
                self.ui.label_strength.setText(f'Уровень: {strength.name}') 


    def change_visibility_password(self) -> None:
        if self.ui.btn_visibility.isChecked():
            self.ui.lineEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.lineEdit.setEchoMode(QLineEdit.Password)

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec())
