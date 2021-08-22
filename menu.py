import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu, QWidget

#for menu bar
class menuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.menuS()

    def menuS(self):
        #Creates menu bar
        menu = self.menuBar()

        menu_file = menu.addMenu("File")
        menu_help = menu.addMenu("Help") 

        #menu_file
        file_new_file = QAction("New Window", self)
        file_new_file.setShortcut("Ctrl+K")
        file_open_folder = QMenu("Select", self)
        file_start = QAction("Start", self)
        file_how = QAction("How to Use", self)

        #menu_help
        file_about = QAction("About",self)
        file_terms = QAction("Terms Of Service", self)

        #add to sub menu
        file_open_folder.addAction(file_start)
        file_open_folder.addAction(file_how)

        #connect to menu bar
        menu_file.addAction(file_new_file)
        menu_file.addMenu(file_open_folder)

        menu_help.addAction(file_about)
        menu_help.addAction(file_terms)

        #when triggered
        #NOTE Will be added later on
    
        #screen
        self.setWindowTitle("Twitch Subscribed Video Downloader")
        self.resize(900,700)
        self.setFixedSize(900, 700)
        self.setWindowIcon(QIcon('img/TwitchLogo.png'))   #logo

