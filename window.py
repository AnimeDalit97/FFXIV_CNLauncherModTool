import sys, os, configparser
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QFileDialog, QMessageBox, QCheckBox
from utils import backupLauncher, replaceFile, backupLauncherAll

class modWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.cfgPath = './settings.ini'
        self.ffXivRootdir = ''
        self.modFilePath = ''
        self.cfg = configparser.ConfigParser()
        self.initUI()
    
    def loadCfg(self, ffxivRootTextItem):
        self.cfg.read(self.cfgPath, encoding='ANSI')
        for item in self.cfg.items('paths'):
            if item[0]=='ffxivrootdir':
                self.ffXivRootdir = item[1]
                ffxivRootTextItem.setPlainText(self.ffXivRootdir)
    
    def getPath(self, textEfitItem):
        self.ffXivRootdir = QFileDialog.getExistingDirectory(None, "选择FF14根目录", "C:/")
        if self.ffXivRootdir != '':
            self.cfg.set('paths', 'ffxivrootdir', self.ffXivRootdir)
            self.cfg.write(open(self.cfgPath, 'w'), 'w')
        textEfitItem.setPlainText(self.ffXivRootdir)

    def getFile(self, textEfitItem):
        self.modFilePath = QFileDialog.getOpenFileName(self, "选择待替换文件", "C:/", "Zip Files(*.zip)")[0]
        textEfitItem.setPlainText(self.modFilePath)

    def saveBackup(self):
        saveDir = ''
        saveDir = QFileDialog.getExistingDirectory(None, "选择备份路径", "C:/")
        if saveDir=='' or not os.path.exists(os.path.join(self.ffXivRootdir, 'uninst.exe')):
            return
        elif self.backupAllCb.isChecked():
            backupLauncherAll(self.ffXivRootdir, saveDir)
            QMessageBox.information(self,'备份完成', f'备份文件保存在:{saveDir}',QMessageBox.Ok, QMessageBox.Ok)
        else:
            backupLauncher(self.ffXivRootdir, saveDir)
            QMessageBox.information(self,'备份完成', f'备份文件保存在:{saveDir}',QMessageBox.Ok, QMessageBox.Ok)
    
    def replaceLauncher(self):
        if self.modFilePath== '' or not os.path.exists(os.path.join(self.ffXivRootdir, 'uninst.exe')):
            return
        else:
            replaceFile(self.ffXivRootdir, self.modFilePath)
            QMessageBox.information(self,'替换完成', f'使用{self.modFilePath}替换完成',QMessageBox.Ok, QMessageBox.Ok)

    def initUI(self):
        self.resize(1000,300)
        self.setWindowTitle('FF14国服启动器替换')

        thisfont = QtGui.QFont()
        thisfont.setFamily("宋体")
        thisfont.setPointSize(18)

        #ffxiv根目录
        ##按钮
        ffxivRootBtn = QPushButton('选择FF14根目录',self)
        ffxivRootBtn.resize(120,40)
        ffxivRootBtn.setStyleSheet("QPushButton{font-family:'宋体';font-size:16px;}")
        ffxivRootBtn.move(30,30)
        ##文本框
        ffxivRootText = QTextEdit(self)
        ffxivRootText.resize(700, 40)
        ffxivRootText.setStyleSheet("QPushButton{font-family:'Times New Roman';font-size:16px;}")
        ffxivRootText.move(200, 30)
        ffxivRootText.setReadOnly(True)
        ##回调
        ffxivRootBtn.clicked.connect(lambda: self.getPath(ffxivRootText))

        ##待替换文件目录
        ##按钮
        modFileBtn = QPushButton('选择待替换文件',self)
        modFileBtn.resize(120,40)
        modFileBtn.setStyleSheet("QPushButton{font-family:'宋体';font-size:16px;}")
        modFileBtn.move(30,80)
        ##文本框
        modFileText = QTextEdit(self)
        modFileText.resize(700, 40)
        modFileText.setStyleSheet("QPushButton{font-family:'Times New Roman';font-size:16px;}")
        modFileText.move(200, 80)
        modFileText.setReadOnly(True)
        ##回调
        modFileBtn.clicked.connect(lambda: self.getFile(modFileText))

        #开始替换
        ##按钮
        replaceBtn = QPushButton('开始替换',self)
        replaceBtn.resize(120,40)
        replaceBtn.setStyleSheet("QPushButton{font-family:'宋体';font-size:16px;}")
        replaceBtn.move(200,200)
        replaceBtn.clicked.connect(self.replaceLauncher)

        #备份启动器
        ##按钮
        backupBtn = QPushButton('备份启动器',self)
        backupBtn.resize(120,40)
        backupBtn.setStyleSheet("QPushButton{font-family:'宋体';font-size:16px;}")
        backupBtn.move(500,200)
        ##回调
        backupBtn.clicked.connect(self.saveBackup)

        #全量备份
        ## 复选框
        self.backupAllCb = QCheckBox('全量备份', self)
        self.backupAllCb.setStyleSheet("QCheckBox::indicator { width: 40px; height: 40px; font-size:32px;}")
        self.backupAllCb.setFont(thisfont)
        self.backupAllCb.move(650, 200)

        # 读取cfg
        if os.path.exists(self.cfgPath):
            self.loadCfg(ffxivRootText)




        

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = modWindow()
    window.show()
    sys.exit(app.exec_())