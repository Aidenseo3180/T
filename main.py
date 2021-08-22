import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor,QGuiApplication, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar,QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox, QTextEdit, QFileDialog
import menu
import os, subprocess
from checkFileDirec import check_dir
import random


#when close the window, shows the first page
class backToFirst:
    def closeEvent(self, QCloseEvent):
        os.chdir(owd)
        self.firstWin = FirstWindow()
        self.firstWin.show()

#fist tab
class FirstWindow(QMainWindow, menu.menuBar):
    def __init__(self):
        super().__init__()
        self.firstUI()

    def firstUI(self):
        #label
        label_1 = QLabel("Twitch Subscribed Video Downloader",self)
        label_1.move(120,80)
        label_1.resize(700,300)
        label_1.setAlignment(Qt.AlignCenter)
        label_1.setWordWrap(True)   #multiple line
        label_1.setFont(QFont("Arial", 13, QFont.Black))
        label_1.setStyleSheet("background-image : url(img/TitleBackground.png); background-repeat : no-repeat;")

        #copyright
        label_2 = QLabel("Copyright @ 2021 by AidenSeo", self)
        label_2.move(10,620)
        label_2.resize(300,100)
        label_2.setFont(QFont("Arial", 6))

        #buttons
        t_btn_1 = QPushButton("Start",self)
        t_btn_1.resize(200,200)
        t_btn_1.move(100,400)

        t_btn_2 = QPushButton("How to Use",self)
        t_btn_2.resize(200,200)
        t_btn_2.move(350,400)

        t_btn_3 = QPushButton("About",self)
        t_btn_3.resize(200,200)
        t_btn_3.move(600,400)

        self.dark_theme = QPushButton(self)
        self.dark_theme.resize(40,35)
        self.dark_theme.setIcon(menu.QIcon('img/dark-mode.png'))
        self.dark_theme.move(60,60)
        self.dark_theme.clicked.connect(self.darkmodeClick)

        self.light_theme = QPushButton(self)
        self.light_theme.resize(40,35)
        self.light_theme.setIcon(menu.QIcon('img/light-mode.png'))
        self.light_theme.clicked.connect(self.lightmodeClick)
        self.light_theme.move(10,60)
        
        self.default_palette = QGuiApplication.palette()    #for theme

        #page transition 
        #when clicked, move to second page
        t_btn_1.clicked.connect(self.secondPage)

        #screen
        self.show()

    def closeEvent(self, QCloseEvent):   #X 누를떄 나오는 이벤트를 QCloseEvent라고 함(closeEvent를 오버라이드 함)
        ans = QMessageBox.question(self,"Twitch Sub-Only Video Downloader", "Quit the program?", 
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  #문제 형식으로 메세지 박스를 띄움
        #(자기 자신, 창 이름, 창 내용, 버튼들을 쭉 나열, 기본값 (기본적으로 YES,NO로 지정되있는거처럼))
        #기본값은 처음 창이 뜰 때 버튼이 음영처리 되어있는거!
        #근데 Yes,No버튼을 설정 안해놔서 해줘야함. 그래서 버튼의 Yes,No값을 변수로 받을 수 있음
        if ans ==QMessageBox.Yes :  #QMessageBox.Yes는 상수라서 이렇게 비교 가능
            QCloseEvent.accept()    #이벤트를 accept함
        else:
            QCloseEvent.ignore()    #아니면 이벤트를 무시 (창이 안꺼짐!)
            #근데 이 QCloseEvent하고 .quit하곤 다른 이벤트임!

    def secondPage(self):
        self.hide()
        self.secondWindow = secondWindow()     #self.secondWindow is the name of the variable
        self.secondWindow.show()               #show the second window
        if self.secondWindow == False:
            self.show()

    #dark theme
    def darkmodeClick(self):
        darkpalette = QPalette()
        darkpalette.setColor(QPalette.Window, QColor(41, 44, 51))
        darkpalette.setColor(QPalette.WindowText, Qt.white)
        darkpalette.setColor(QPalette.Base,QColor(15, 15, 15))
        darkpalette.setColor(QPalette.AlternateBase, QColor(41, 44, 51))
        darkpalette.setColor(QPalette.ToolTipBase, Qt.white)
        darkpalette.setColor(QPalette.ToolTipText, Qt.white)
        darkpalette.setColor(QPalette.Text, Qt.white)
        darkpalette.setColor(QPalette.Button, QColor(41, 44, 51))
        darkpalette.setColor(QPalette.ButtonText, Qt.white)
        darkpalette.setColor(QPalette.BrightText, Qt.red)
        darkpalette.setColor(QPalette.Highlight, QColor(100, 100, 225))
        darkpalette.setColor(QPalette.HighlightedText, Qt.blue)
        QGuiApplication.setPalette(darkpalette)
    
    #light theme
    def lightmodeClick(self):
        lightpalette = QPalette()
        lightpalette.setColor(QPalette.Window, QColor(244, 244, 245))
        lightpalette.setColor(QPalette.WindowText, Qt.black)
        lightpalette.setColor(QPalette.Base, QColor(244, 244, 245))
        lightpalette.setColor(QPalette.AlternateBase, QColor(222, 220, 220))
        lightpalette.setColor(QPalette.ToolTipBase, Qt.black)
        lightpalette.setColor(QPalette.ToolTipText, Qt.black)
        lightpalette.setColor(QPalette.Text, Qt.black)
        lightpalette.setColor(QPalette.Button, QColor(222, 220, 220))
        lightpalette.setColor(QPalette.ButtonText, Qt.black)
        lightpalette.setColor(QPalette.BrightText, Qt.blue)
        lightpalette.setColor(QPalette.Highlight, QColor(146, 146, 230))
        lightpalette.setColor(QPalette.HighlightedText, Qt.blue)
        QGuiApplication.setPalette(lightpalette)        


#second page
class secondWindow(QMainWindow, menu.menuBar, backToFirst):
    def __init__(self):
        super(secondWindow, self).__init__()
        self.secondUI()
        self.lastWin = download()   #download 페이지에 link, browsed file를 전달하기 위해 만듦
        
    def secondUI(self):
        #label
        lt_label = QLabel("Paste Link in the box", self)
        lt_label.move(10,50)
        lt_label.resize(150,100)
        lt_label.setAlignment(Qt.AlignCenter)
        lt_label.setWordWrap(True)
        #lt_label.setFont(QFont("Arial",7, QFont.Black))   #font

        #link box
        self.text_edit_1 = QTextEdit(self)
        self.text_edit_1.resize(600,100)
        self.text_edit_1.move(200,60)

        #show how it would look like
        self.text_edit_2 = QTextEdit(self)       #to show how link looks like before conntinuing
        self.text_edit_2.resize(600,150)      #somehow fix auto resize!
        self.text_edit_2.move(200,175)
        self.text_edit_2.setStyleSheet("border: 1px solid black;")

        #set the directory
        self.dir_storage = QTextEdit(self)
        self.dir_storage.resize(720,150)
        self.dir_storage.move(20,400)

        #button (to confirm the link that we put in to the label)
        convertButton = QPushButton("Convert", self)
        convertButton.resize(80,100)
        convertButton.move(810,60)
        convertButton.setFont(QFont("Arial", 6))
        convertButton.clicked.connect(self.onChanged)   #convert
        
        ##confirm
        pcdButton = QPushButton("Confirm/Download\nthe Video", self)
        pcdButton.resize(350,100)
        pcdButton.move(100,575)
        pcdButton.clicked.connect(self.downloadPage) 

        ##Cancel
        cancelButton = QPushButton("Cancel", self)
        cancelButton.resize(350,100)
        cancelButton.move(500,575)
        cancelButton.clicked.connect(self.close)

        ##Browse
        browser = QPushButton("Browse", self)
        browser.resize(140,70)
        browser.move(750,475)
        browser.clicked.connect(self.openFile)

        statusLabel = QLabel("Status",self)
        statusLabel.setAlignment(Qt.AlignCenter)
        statusLabel.resize(90,50)
        statusLabel.move(800,200)

        self.checkText = QTextEdit("",self) #링크 : 노란색 status
        self.checkText.setStyleSheet("background-color: rgb(255, 255, 51);")
        self.checkText.setAlignment(Qt.AlignCenter)
        self.checkText.resize(100,50)
        self.checkText.move(800,240)

        self.expLabel = QLabel("Browse the location of ffmpeg.exe from your computer :", self)
        self.expLabel.resize(700,50)
        self.expLabel.move(30,350)
        
        self.browseSt = QTextEdit(self) # 파일 노란색 status
        self.browseSt.setStyleSheet("background-color: rgb(255, 255, 51);")
        self.browseSt.setFont(QFont("Arial", 8))   #font
        self.browseSt.setAlignment(Qt.AlignCenter)
        self.browseSt.resize(140,50)
        self.browseSt.move(750,370)

        browserCh = QPushButton("Check", self)
        browserCh.setFont(QFont("Arial", 6))   #font
        browserCh.resize(140,45)
        browserCh.move(750,425)
        browserCh.clicked.connect(self.checkFile)


    def onChanged(self):          #when the text in box changes, it also changes what's inside the label (텍스트가 바뀌는걸 보여주는것)
        try:
            imageURL = self.text_edit_1.toPlainText()
            x = imageURL.split('/')
            front_x = x[2].split('.')   #shows d1m7j... thing
            if front_x[0][0] != 'd':    #if first letter of front_x is not 'd'
                self.linkChecker('NOT OKAY')
                return
            
            vidName = self.randomName() #use random number for video name
            self.text_edit_2.setText(f'.\\ffmpeg -headers "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36" -i "https://{front_x[0]}.cloudfront.net/{x[3]}/chunked/index-dvr.m3u8" -c copy -bsf:a aac_adtstoasc "{vidName}.mp4"' )    
            #print(self.text_edit_2.toPlainText())
            self.linkChecker('OK')
        except IndexError:
            self.linkChecker('NOT OKAY')

    def openFile(self): #browse for files
        fname = QFileDialog.getExistingDirectory(self)
        self.dir_storage.setText(fname)

    def checkFile(self):
        value = self.dir_storage.toPlainText()
        res = check_dir(self, value)
        if res == 'True':
            self.browseSt.setText('OK')
            self.browseSt.setAlignment(Qt.AlignCenter)
            self.browseSt.setStyleSheet("background-color: rgb(113, 218, 71);")
        else:
            self.browseSt.setText('X')
            self.browseSt.setAlignment(Qt.AlignCenter)
            self.browseSt.setStyleSheet("background-color: rgb(217, 67, 67);")

    def downloadPage(self):
        if (self.checkText.toPlainText() == 'OK' and self.browseSt.toPlainText() == 'OK'):
            self.lastWin.input1.setText(self.text_edit_2.toPlainText()) #링크 정보를 옮김
            self.lastWin.input2.setText(self.dir_storage.toPlainText()) #browse한 파일 위치를 옮김
            self.lastWin.displayInfo()
            self.hide()

        elif (self.checkText.toPlainText() != 'OK' and self.browseSt.toPlainText() == 'OK'):  #만약 status가 OK가 아니면 :
            QMessageBox.about(self, "Warning", "The Format of ffmpeg link is incorrect. Check 'How to Use' for more information")

        elif (self.browseSt.toPlainText() != 'O' and self.checkText.toPlainText() == 'OK'):   #<= 여기엔 browse한 곳에 ffmpeg가 없을때
            QMessageBox.about(self, "Warning", "The file location doesn't contain ffmpeg.exe, ffplay.exe and ffprobe.exe. Please reselect the directory")

        else:   #둘 다 아니면
            QMessageBox.about(self, "Warning", "Both the file directory and the format of ffmpeg link are incorrect. Check 'How to Use' for more information")

    def linkChecker(self, text):    #check if the link is legit (status를 색깔로 표시)
        if (text=="OK"):
            self.checkText.setText("OK")
            self.checkText.setAlignment(Qt.AlignCenter)
            self.checkText.setStyleSheet("background-color: rgb(113, 218, 71);")
        else:
            self.checkText.setText("X")
            self.checkText.setAlignment(Qt.AlignCenter)
            self.checkText.setStyleSheet("background-color: rgb(217, 67, 67);")

    def randomName(self):           #generates random number for vid name
        n = random.randint(1000,9999)
        return n

class download(QMainWindow, menu.menuBar, backToFirst):
    def __init__(self):
        super().__init__()
        self.downloadPage()
        self.input1 = QLineEdit()  #link를 받음
        self.input2 = QLineEdit()  #directory 정보를 받음
        #self.hide()

    def downloadPage(self):
        self.progressBar = QProgressBar(self)
        self.progressBar.resize(875,70)
        self.progressBar.move(50,400)

        self.pauButton = QPushButton("Start Downloading", self)
        self.pauButton.resize(800,150)
        self.pauButton.move(50,500)
        self.pauButton.clicked.connect(self.downloadProgress)

        ''' NOTE : Cancel Button
        self.cancButton = QPushButton("Cancel", self)
        self.cancButton.resize(200,150)
        self.cancButton.move(680,500)
        self.cancButton.clicked.connect(self.cancelProgress)
        '''

        self.se = QLabel("Download Progress: ",self)
        self.se.resize(250,50)
        self.se.move(50,50)

        self.te = QTextEdit(self)   #NOTE To show cmd downloading progress, but not for now (Might Update later)
        self.te.resize(800,275)
        self.te.move(50,100)

    def displayInfo(self):
        self.show()

    ''' NOTE : Cancel Progress Function
    def cancelProgress(self):   #cancel 버튼 누르면 진짜로 그만할거냐고 물어봄
        cac = QMessageBox.question(self,"Twitch Sub-Only Video Downloader", "If you leave now, the current download progress will be discarded. Are you sure?", 
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  #문제 형식으로 메세지 박스를 띄움
        #(자기 자신, 창 이름, 창 내용, 버튼들을 쭉 나열, 기본값 (기본적으로 YES,NO로 지정되있는거처럼))
        #기본값은 처음 창이 뜰 때 버튼이 음영처리 되어있는거!
        #근데 Yes,No버튼을 설정 안해놔서 해줘야함. 그래서 버튼의 Yes,No값을 변수로 받을 수 있음
        if cac == QMessageBox.Yes :  #QMessageBox.Yes는 상수라서 이렇게 비교 가능
            #self.download_dir()

            #self.download_dir(self,None,None)  NOTE 이건 아직 모르겠음... 어떻게 이걸 해야할지 (nested function으로 가능하게 할 수 있을듯?)

            self.progressBar.setMaximum(100)    #만약 취소되었을땐 progressBar을 아예 멈춤
            self.progressBar.setValue(0)
            QMessageBox.about(self,"Cancelled", "Download Cancelled. You'll be headed back to the main menu")
            self.close()
        else:
            return
    '''

    def downloadProgress(self):  #Download 버튼을 눌렀을때 실행
        self.pauButton.clicked.disconnect() #원래 connection을 끊음
        self.pauButton.setEnabled(False)    #버튼 다시 못누르게 함
        self.pauButton.setText("Downloading...")

        self.progressBar.setTextVisible(False)  #무한로딩을 보여줌

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)

        #얻어온 정보들
        text_inf = self.input1.text()       #정보를 얻어서, 이걸 download_dir에 넣어 사용함
        file_inf = self.input2.text()       #file
        self.download_dir(text_inf, file_inf)

    def download_dir(self, linkVal, browseVal):

        if linkVal is not None and browseVal is not None:
            link = linkVal
            indexx = link.find('\\')
            final_link = link[:indexx]+'\\'+link[indexx:]   #NOTE : 파일의 네임은 아직 지정 못함.. (나중에 기능을 더해야 함)

            x = subprocess.Popen(final_link, cwd = browseVal, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = x.communicate()
            exit_code = x.wait()    #저장 될 떄까지 기다림

            #NOTE stdout을 하나씩 읽으면 output 윈도우에 보이게 할 수도 있음!

            if x.poll() is not None:  #subprocess가 끝나면
                self.progressBar.setMaximum(100)    #만약 다 되었을땐 progressBar을 아예 멈춤
                self.progressBar.setValue(0)
                self.pauButton.setText("Done")
                QMessageBox.about(self, "Alert", "Successfully Downloaded. Press 'Done' to go back to the main menu")
                self.pauButton.setEnabled(True)     #다시 누를 수 있게 함

                self.pauButton.clicked.connect(self.close)




#main code
if __name__ =='__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    owd = os.getcwd()
    firstPage = FirstWindow()    #first page
    sys.exit(app.exec_())

