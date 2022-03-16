import sys
from PyQt5.QtWidgets import QApplication
from window import modWindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = modWindow()
    window.show()
    sys.exit(app.exec_())