import sys
from PyQt5.QtWidgets import QApplication, QWidget

from pygdk.constants import window

def init():
    global window
    
    app = QApplication(sys.argv)
    window = QWidget()
    
    window.show()
    sys.exit(app.exec_())