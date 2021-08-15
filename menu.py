import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow,QAction, QWidget

class menuBar(QWidget):     #for menu bar
    def __init__(self):
        super().__init__()
        self.menuS()

    def menuS(self):
        menu = self.menuBar()   #메뉴바 생성
        menu_file = menu.addMenu("File")   #큰 그룹 생성 (File, Edit같이)
        menu_edit = menu.addMenu("Edit")
        menu_view = menu.addMenu("View")
        menu_help = menu.addMenu("Help") 

        #menu_file
        file_new_file = QAction("New File", self)
        file_new_file.setShortcut("Ctrl+N")
        file_new_window = QAction("New Window", self)
        file_new_window.setShortcut("Ctrl+Shift+N")
        file_open_file = QAction("Open File", self)
        file_open_file.setShortcut("Ctrl+O")
        file_open_folder = QAction("Open Folder", self)
        file_open_folder.setShortcut("Ctrl+K+Ctrl+O")

        #menu_edit


        #menu_view


        #menu_help


        #connect to menu bar
        menu_file.addAction(file_new_file)
        menu_file.addAction(file_new_window)
        menu_file.addAction(file_open_file)
        menu_file.addAction(file_open_folder)

        #screen
        self.setWindowTitle("Twitch Subscribed Video Downloader")
        self.resize(900,700)
        self.setFixedSize(900, 700)
        self.setWindowIcon(QtGui.QIcon('img/TwitchLogo.png'))   #logo





