import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("12:00:00", self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Digital CLock")
        self.setGeometry(600, 400, 300, 100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "font-family: Inter;"
                                      "color: #42e372;"
                                      )
        
        self.setStyleSheet("background: black;")
    
if __name__ == "__main__":
      app = QApplication(sys.argv)
      clock = DigitalClock()
      clock.show()
      sys.exit(app.exec_())
        