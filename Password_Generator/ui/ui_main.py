# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGridLayout,
        QHBoxLayout, QLabel, QLineEdit, QMainWindow,
        QPushButton, QSizePolicy, QSlider, QSpinBox,
        QWidget)
from ui import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(532, 363)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/icons/ic_vpn_key_128_28771.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidge = QWidget(MainWindow)
        self.centralwidge.setObjectName(u"centralwidge")
        self.centralwidge.setStyleSheet(u"QWidget{\n"
"    background-color: #673AB7;\n"
"    color: white;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 2px solid #2196F3;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lower, #btn_upper, #btn_digits, #btn_symbols{\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #2196F3;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 4px solid #2196F3;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #1A237E;\n"
"    border-color: #2196F3;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidge)
        self.gridLayout.setObjectName(u"gridLayout")
        self.layot_password = QFrame(self.centralwidge)
        self.layot_password.setObjectName(u"layot_password")
        self.layot_password.setStyleSheet(u"")
        self.frame_password = QHBoxLayout(self.layot_password)
        self.frame_password.setObjectName(u"frame_password")
        self.frame_password_2 = QFrame(self.layot_password)
        self.frame_password_2.setObjectName(u"frame_password_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_password_2.sizePolicy().hasHeightForWidth())
        self.frame_password_2.setSizePolicy(sizePolicy1)
        self.frame_password_2.setStyleSheet(u"QFrame{\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-left: 0;\n"
"}\n"
"\n"
"QFrame{\n"
"    border-color: #2196F3;\n"
"}")
        self.frame_password_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_password_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_password_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit = QLineEdit(self.frame_password_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.btn_visibility = QPushButton(self.frame_password_2)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton{\n"
"    border: none;\n"
"    margin: 0 ;\n"
"    background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/eye_slash_visible_hide_hidden_show_icon_145987.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/icons/eye_visible_hide_hidden_show_icon_145988.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_visibility.setIcon(icon1)
        self.btn_visibility.setIconSize(QSize(30, 30))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)

        self.horizontalLayout_5.addWidget(self.btn_visibility)


        self.frame_password.addWidget(self.frame_password_2)

        self.btn_refresh = QPushButton(self.layot_password)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"    margin-right: 0;\n"
"    margin-left: 0;\n"
"    border-color: #2196F3;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/twocirclingarrows1_120592.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_refresh.setIcon(icon2)
        self.btn_refresh.setIconSize(QSize(52, 52))

        self.frame_password.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.layot_password)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton{\n"
"    padding: 5px;\n"
"    margin-left: 0;\n"
"	border-color:  #2196F3;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/clipboard_89387.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_copy.setIcon(icon3)
        self.btn_copy.setIconSize(QSize(42, 42))

        self.frame_password.addWidget(self.btn_copy)


        self.gridLayout.addWidget(self.layot_password, 0, 0, 1, 1)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.label_strength = QLabel(self.centralwidge)
        self.label_strength.setObjectName(u"label_strength")
        sizePolicy1.setHeightForWidth(self.label_strength.sizePolicy().hasHeightForWidth())
        self.label_strength.setSizePolicy(sizePolicy1)
        self.label_strength.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_info.addWidget(self.label_strength)


        self.gridLayout.addLayout(self.layout_info, 1, 0, 1, 1)

        self.layout_length = QHBoxLayout()
        self.layout_length.setObjectName(u"layout_length")
        self.slider_length = QSlider(self.centralwidge)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slider_length.setStyleSheet(u"QSlider::groove:horizontal{\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
"    background-color: #2196F3;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"    background-color: white;\n"
"    width: 22px;\n"
"    border-radius: 10px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"}\n"
"")
        self.slider_length.setMaximum(80)
        self.slider_length.setValue(15)
        self.slider_length.setOrientation(Qt.Orientation.Horizontal)

        self.layout_length.addWidget(self.slider_length)

        self.spinbox_length = QSpinBox(self.centralwidge)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setStyleSheet(u"QSpinBox{\n"
"    border:2px solid #2196F3;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"    border-color: #2196F3;\n"
"}")
        self.spinbox_length.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinbox_length.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox_length.setMaximum(80)
        self.spinbox_length.setValue(15)

        self.layout_length.addWidget(self.spinbox_length)


        self.gridLayout.addLayout(self.layout_length, 2, 0, 1, 1)

        self.layout_character = QHBoxLayout()
        self.layout_character.setObjectName(u"layout_character")
        self.btn_lower = QPushButton(self.centralwidge)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_character.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidge)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_character.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidge)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_character.addWidget(self.btn_digits)

        self.btn_symbols = QPushButton(self.centralwidge)
        self.btn_symbols.setObjectName(u"btn_symbols")
        self.btn_symbols.setCheckable(True)

        self.layout_character.addWidget(self.btn_symbols)


        self.gridLayout.addLayout(self.layout_character, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidge)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
        self.btn_copy.setText("")
#if QT_CONFIG(shortcut)
        self.btn_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.label_strength.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_symbols.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
    # retranslateUi

