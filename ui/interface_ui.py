# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import _icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1374, 823)
        MainWindow.setStyleSheet(u"/*#centralwidget{\n"
"background-color: rgb(31, 35, 58);\n"
"}*/")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1374, 823))
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.leftHeader_Menu = QWidget(self.leftMenu)
        self.leftHeader_Menu.setObjectName(u"leftHeader_Menu")
        self.verticalLayout_2 = QVBoxLayout(self.leftHeader_Menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.widget = QWidget(self.leftHeader_Menu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(33, 29))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 0, 5)
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.verticalLayout_5.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignRight|Qt.AlignTop)

        self.frameClock = QFrame(self.leftHeader_Menu)
        self.frameClock.setObjectName(u"frameClock")
        self.frameClock.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frameClock)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelHours = QLabel(self.frameClock)
        self.labelHours.setObjectName(u"labelHours")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(30)
        self.labelHours.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelHours)

        self.labelColon = QLabel(self.frameClock)
        self.labelColon.setObjectName(u"labelColon")
        self.labelColon.setMaximumSize(QSize(16777215, 16777215))
        self.labelColon.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelColon)

        self.labelMinutes = QLabel(self.frameClock)
        self.labelMinutes.setObjectName(u"labelMinutes")
        self.labelMinutes.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelMinutes)

        self.labelHolder = QLabel(self.frameClock)
        self.labelHolder.setObjectName(u"labelHolder")
        self.labelHolder.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelHolder)


        self.verticalLayout_2.addWidget(self.frameClock, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.leftHeader_Menu, 0, Qt.AlignTop)

        self.section2 = QWidget(self.leftMenu)
        self.section2.setObjectName(u"section2")
        self.verticalLayout_3 = QVBoxLayout(self.section2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 0, 5)
        self.frame_10 = QFrame(self.section2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_8 = QFrame(self.frame_10)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(45, 45))
        self.label_13.setMaximumSize(QSize(45, 45))
        self.label_13.setPixmap(QPixmap(u":/feather/icons/feather/cloud.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_11.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_10.addWidget(self.label_12)


        self.horizontalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame_10)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(9)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_3.addWidget(self.frame_3, 0, Qt.AlignVCenter)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignVCenter)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_3.addWidget(self.frame_12, 0, Qt.AlignVCenter)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)


        self.horizontalLayout_3.addWidget(self.frame_7, 0, Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_10, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.section2)

        self.verticalSpacer = QSpacerItem(10, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.section3 = QWidget(self.leftMenu)
        self.section3.setObjectName(u"section3")
        self.verticalLayout_25 = QVBoxLayout(self.section3)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 0, 5)
        self.frame_2 = QFrame(self.section3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/feather/icons/feather/user.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelUsername = QLabel(self.frame)
        self.labelUsername.setObjectName(u"labelUsername")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.labelUsername.setFont(font4)

        self.verticalLayout_4.addWidget(self.labelUsername)

        self.labelEmail = QLabel(self.frame)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setFont(font3)

        self.verticalLayout_4.addWidget(self.labelEmail)


        self.horizontalLayout_4.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/feather/icons/feather/log-out.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_25.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.section3, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout_11 = QVBoxLayout(self.mainBody)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerMenu = QWidget(self.mainBody)
        self.headerMenu.setObjectName(u"headerMenu")
        self.horizontalLayout_8 = QHBoxLayout(self.headerMenu)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.pagesBtn = QFrame(self.headerMenu)
        self.pagesBtn.setObjectName(u"pagesBtn")
        self.pagesBtn.setFrameShape(QFrame.StyledPanel)
        self.pagesBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.pagesBtn)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 0, 5)
        self.homeBtn = QPushButton(self.pagesBtn)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setFont(font2)

        self.horizontalLayout_6.addWidget(self.homeBtn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.voiceBtn = QPushButton(self.pagesBtn)
        self.voiceBtn.setObjectName(u"voiceBtn")
        self.voiceBtn.setFont(font2)

        self.horizontalLayout_6.addWidget(self.voiceBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.scenarioBtn = QPushButton(self.pagesBtn)
        self.scenarioBtn.setObjectName(u"scenarioBtn")
        self.scenarioBtn.setFont(font2)

        self.horizontalLayout_6.addWidget(self.scenarioBtn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.settingBtn = QPushButton(self.pagesBtn)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setFont(font2)

        self.horizontalLayout_6.addWidget(self.settingBtn)


        self.horizontalLayout_8.addWidget(self.pagesBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.frame_15 = QFrame(self.headerMenu)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(15)
        font5.setBold(False)
        self.label_18.setFont(font5)

        self.verticalLayout_14.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(12)
        font6.setBold(False)
        self.label_19.setFont(font6)

        self.verticalLayout_14.addWidget(self.label_19)


        self.horizontalLayout_9.addWidget(self.frame_14, 0, Qt.AlignVCenter)

        self.label_20 = QLabel(self.frame_15)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(60, 60))
        self.label_20.setMaximumSize(QSize(60, 60))
        self.label_20.setPixmap(QPixmap(u":/feather/icons/feather/user.png"))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_20)


        self.horizontalLayout_8.addWidget(self.frame_15, 0, Qt.AlignRight|Qt.AlignTop)

        self.actionsBtn = QFrame(self.headerMenu)
        self.actionsBtn.setObjectName(u"actionsBtn")
        self.actionsBtn.setFrameShape(QFrame.StyledPanel)
        self.actionsBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.actionsBtn)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.minimizeBtn = QPushButton(self.actionsBtn)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.actionsBtn)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.actionsBtn)
        self.closeBtn.setObjectName(u"closeBtn")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon3)
        self.closeBtn.setAutoDefault(False)

        self.horizontalLayout_7.addWidget(self.closeBtn)


        self.horizontalLayout_8.addWidget(self.actionsBtn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.headerMenu, 0, Qt.AlignTop)

        self.stackPages = QWidget(self.mainBody)
        self.stackPages.setObjectName(u"stackPages")
        self.stackPages.setStyleSheet(u"/*#stackPages {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#homePage {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#voiceassisPage {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#scenarioPage {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#settingPage {\n"
"    background-color: rgb(255, 255, 255);\n"
"}*/\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.stackPages)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.mainPages = QCustomQStackedWidget(self.stackPages)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_15 = QVBoxLayout(self.homePage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_3 = QWidget(self.homePage)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_16 = QVBoxLayout(self.widget_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_5)


        self.verticalLayout_15.addWidget(self.widget_3, 0, Qt.AlignTop)

        self.widget_6 = QWidget(self.homePage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_17 = QVBoxLayout(self.widget_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_6)

        self.verticalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)


        self.verticalLayout_15.addWidget(self.widget_6)

        self.mainPages.addWidget(self.homePage)
        self.voiceassisPage = QWidget()
        self.voiceassisPage.setObjectName(u"voiceassisPage")
        self.verticalLayout_18 = QVBoxLayout(self.voiceassisPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_5 = QWidget(self.voiceassisPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_19 = QVBoxLayout(self.widget_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_16)


        self.verticalLayout_18.addWidget(self.widget_5)

        self.mainPages.addWidget(self.voiceassisPage)
        self.scenarioPage = QWidget()
        self.scenarioPage.setObjectName(u"scenarioPage")
        self.verticalLayout_20 = QVBoxLayout(self.scenarioPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_7 = QWidget(self.scenarioPage)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_21 = QVBoxLayout(self.widget_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_17 = QLabel(self.widget_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_17)


        self.verticalLayout_20.addWidget(self.widget_7)

        self.mainPages.addWidget(self.scenarioPage)
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_23 = QVBoxLayout(self.settingPage)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_9 = QWidget(self.settingPage)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_22 = QVBoxLayout(self.widget_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_21 = QLabel(self.widget_9)
        self.label_21.setObjectName(u"label_21")
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        self.label_21.setFont(font7)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_21)

        self.frame_13 = QFrame(self.widget_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_22 = QLabel(self.frame_13)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font7)

        self.horizontalLayout_10.addWidget(self.label_22)

        self.themeList = QComboBox(self.frame_13)
        self.themeList.setObjectName(u"themeList")

        self.horizontalLayout_10.addWidget(self.themeList)


        self.verticalLayout_22.addWidget(self.frame_13)


        self.verticalLayout_23.addWidget(self.widget_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPages.addWidget(self.settingPage)

        self.verticalLayout_13.addWidget(self.mainPages)


        self.verticalLayout_11.addWidget(self.stackPages)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.labelHours.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.labelColon.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.labelMinutes.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.labelHolder.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#757778;\">AM</span></p></body></html>", None))
        self.label_13.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Mostly Cloudy", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ho Chi Minh City, Viet Nam", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"16\u00b0C", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Feels like", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"81%", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"1.54 Km/h", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Wind", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"1011", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.label.setText("")
        self.labelUsername.setText(QCoreApplication.translate("MainWindow", u"Pham Phuong Minh Tri", None))
        self.labelEmail.setText(QCoreApplication.translate("MainWindow", u"21522708@gm.uit.edu.vn", None))
        self.label_2.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"HomePage", None))
        self.voiceBtn.setText(QCoreApplication.translate("MainWindow", u"Voice Assistant", None))
        self.scenarioBtn.setText(QCoreApplication.translate("MainWindow", u"Scenario", None))
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Hello Tri,", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Welcome Home!", None))
        self.label_20.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Room Placeholder", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Devices Placehoder", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Voice Assistant PlaceHolder", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Scenario Placeholder", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Setting PlaceHolder", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

