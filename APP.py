from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
 
def on_button_click():
    print("Hello, PyQt!")
 
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Friendwork")
 
button = QPushButton("Click me!", window)
button.clicked.connect(on_button_click)
button.show()
 
window.show()
sys.exit(app.exec_())