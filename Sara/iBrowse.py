
import imp
from pydoc import importfile
from turtle import home
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWebEngineWidgets import *
import ctypes

# set the console window title
title = 'Console'
ctypes.windll.kernel32.SetConsoleTitleW(title)

class MainWindow(QMainWindow):
    def __init__(self):
        # main window
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        ref_btn = QAction('Refresh', self)
        ref_btn.triggered.connect(self.browser.reload)
        navbar.addAction(ref_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        fow_btn = QAction('Forward', self)
        fow_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fow_btn)

        # urlbar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.updateUrl)

        #go_btn = QAction('Go!', self)
        #go_btn.triggered.connect(self.browser.)
        #navbar.addAction(fow_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl('https://' + url))
    def updateUrl(self, url):
        self.url_bar.setText(url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('iBrowse')
window = MainWindow()            
app.exec()
