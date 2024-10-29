from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader

from PySide6.QtCore import QSettings, QTimer, QTime, Qt
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QGraphicsDropShadowEffect
import pytz
from datetime import datetime

class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow  # Store the mainwindow instance
        self.ui = MainWindow.ui  # Store the ui instance

        # Apply custom font
        self.loadRobotoFont()

        # Initialize app theme
        self.initialzieAppTheme()

        # Create real-time clock
        self.createRealTimeClock()

    # Create real-time clock
    def createRealTimeClock(self):
        """Initialize and update a real-time clock for Vietnam timezone"""
        # Create a QTimer that updates every minute
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateVietnamTime)
        self.timer.start(60000)  # Update every minute

        # Set initial time immediately
        self.updateVietnamTime()

    def updateVietnamTime(self):
        """Fetch and display current time in Vietnam (UTC+7)"""
        # Get current time in Vietnam timezone
        vn_timezone = pytz.timezone("Asia/Ho_Chi_Minh")
        vn_time = datetime.now(vn_timezone)

        # Format the time for display
        hours = vn_time.strftime("%I")  # 12-hour format
        minutes = vn_time.strftime("%M")
        am_pm = vn_time.strftime("%p")

        # Update the labels with the current time
        self.ui.labelHours.setText(hours)
        self.ui.labelMinutes.setText(minutes)
        self.ui.labelHolder.setText(am_pm)

    # Create a screen loader
    def createLoader(self):
        loader = QCustom3CirclesLoader(
            color=QColor(self.main.theme.COLOR_ACCENT_1),
            penWidth=20,
            animationDuration=400
        )

    # Initialize app theme
    def initialzieAppTheme(self):
        """Initialize the application theme from settings"""
        settings = QSettings()
        current_theme = settings.value("Theme")

        # Add theme to the theme list
        self.populateThemeList(current_theme)
        # Connect theme change signal to change app theme
        self.ui.themeList.currentTextChanged.connect(self.changeAppTheme)

    def populateThemeList(self, current_theme):
        """Populate the list from available app themes"""
        theme_count = -1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)
            # check default theme/current theme
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.themeList.setCurrentIndex(theme_count)  # select the theme

    # Change app theme
    def changeAppTheme(self):
        """Change app theme based on user selection"""
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme:
            # Apply new theme
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    # Apply custom font
    def loadRobotoFont(self):
        """Load and apply roboto font"""
        font_id = QFontDatabase.addApplicationFont("./font/roboto/Roboto-Regular.ttf")
        if font_id == -1:
            print("Failed to load Roboto font")
            return

        # Apply font
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        roboto = QFont(font_family[0]) if font_family else QFont("Roboto")
        self.main.setFont(roboto)
