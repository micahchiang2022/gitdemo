import sys
from PyQt5.QtWidgets import QApplication, QMainwindowsdow,QLabel,QPushButton
app = QApplication(sys.argv)
windows = QMainwindowsdow()
windows.setGeometry(100, 100, 500, 500)
windows.setwindowsdowTitle('Demo Title')

btn = QPushButton("Text", windows)
btn.move(100, 100)

windows.show()
sys.exit(app.exec_())

def click():
    btn.setText("Clicked1")
    
btn.clicked.connect(click)