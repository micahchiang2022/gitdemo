import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(100, 100, 500, 500)
win.setWindowTitle('Demo Title')

btn = QPushButton("Text", win)
btn.move(100, 100)

win.show()
sys.exit(app.exec_())

def click():
    btn.setText("Clicked")
    
btn.clicked.connect(click)