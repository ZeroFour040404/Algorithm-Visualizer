from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer

class LinearSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clock = QTimer(self)
        self.clock.timeout.connect(self.continue_search)
        self.count = 0
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Linear Search Algorithm')
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon('icon.png'))
        
        self.label = QLabel('Linear Search Algorithm', self)
        self.label.setFont(QFont('Arial', 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 30, 600, 50)
        
        self.my_list = QLineEdit(self)
        self.my_list.setFont(QFont('Arial', 12))   
        self.my_list.setPlaceholderText('Enter list of values')
        self.my_list.setGeometry(75, 100, 200, 50)
        
        self.target = QLineEdit(self)
        self.target.setFont(QFont('Arial', 12))
        self.target.setPlaceholderText('Enter target value')
        self.target.setGeometry(325, 100, 200, 50)
        
        self.button = QPushButton('Start Search', self)
        self.button.setFont(QFont('Arial', 14))
        self.button.setGeometry(200, 160, 200, 40)
        self.button.clicked.connect(self.start_search)
        
        self.lower_bound = QLabel('0', self)
        self.lower_bound.setFont(QFont('Arial', 14))    
        self.lower_bound.setGeometry(50, 200, 50, 50)
        self.lower_bound.setStyleSheet("""
                                       font-weight: bold;
                                       """)

        self.upper_bound = QLabel('0', self)
        self.upper_bound.setFont(QFont('Arial', 14))
        self.upper_bound.setGeometry(540, 200, 50, 50)
        self.upper_bound.setStyleSheet("""
                                       font-weight: bold;
                                       """)

        self.box = QLabel('', self)
        self.box.setFont(QFont('Arial', 12))    
        self.box.setGeometry(50, 250, 500, 50)
        self.box.setAlignment(Qt.AlignCenter)
        self.box.setStyleSheet("""
                               border: 1px solid black;
                               background-color: green;
                               """)
        
        self.block1 = QLabel('', self)
        self.block1.setGeometry(50, 250, 0, 50)
        self.block1.setStyleSheet("""
                                  border: 1px solid black;
                                  background-color: gray;
                                  """)
        
        self.line = QLabel('', self)
        self.line.setGeometry(300, 245, 0, 60)
        self.line.setStyleSheet("""
                                background-color: yellow;
                                """)
        
        self.guess = QLabel('', self)
        self.guess.setFont(QFont('Arial', 12))
        self.guess.setGeometry(300, 300, 50, 50)
        self.guess.setStyleSheet("""
                                 color: blue;
                                 """)
        
        self.attempts = QLabel('Number of Attempts: ', self)
        self.attempts.setFont(QFont('Arial', 12))
        self.attempts.setGeometry(50, 350, 500, 50)
        self.attempts.setStyleSheet("""
                                    font-weight: bold;
                                    """)
        
        self.range_low = QLabel('a', self)
        self.range_low.setFont(QFont('Arial', 10)) 
        self.range_low.setGeometry(50, 200, 0, 50)
        self.range_low.setStyleSheet("""
                                     color: red;
                                     """)
        
    def start_search(self):
        self.count = 0
        self.attempts.setText('Number of Attempts: ')
        self.attempts.setStyleSheet("""
                                    font-weight: bold;
                                    color: black;
                                        """)
        text = self.my_list.text()
        try:
            self.data = [int(x.strip()) for x in text.split(",") if x.strip()]
            self.value = int(self.target.text())
        except ValueError:
            self.attempts.setText('Use comma-separated numbers only!!')
            self.attempts.setStyleSheet("""
                                        font-weight: bold;
                                        color: red;
                                        """)
            return -1
        self.first = 0
        self.last = len(self.data) - 1
        try:
            self.lower_bound.setText(str(self.data[0]))
            self.upper_bound.setText(str(self.data[len(self.data) - 1]))
        except IndexError:
            self.attempts.setText('Do not leave any areas blank!!')
            self.attempts.setStyleSheet("""
                                        font-weight: bold;
                                        color: red;
                                        """)
            return -1
        
        self.line.setGeometry(300, 245, 0, 60)
        self.guess.setText('')
        self.block1.setGeometry(50, 250, 0, 50)
                    
        self.clock.start(1000)
    

    def continue_search(self):
        self.count += 1
        if self.count > len(self.data):
            self.attempts.setText('Number of Attempts: ' + str(self.count))
            self.attempts.setText(self.attempts.text() + ' | Failed | Not in List')
            self.clock.stop()
            return
        
        if self.value == self.data[self.count - 1]:
            try:
                self.line.setGeometry(50 + int((self.count - 1) * 490 / (len(self.data) - 1)), 245 , 10, 60)
                self.guess.setGeometry(50 + int((self.count - 1) * 490 / (len(self.data) - 1)), 300 , 50, 50)
            except ZeroDivisionError:
                self.line.setGeometry(295, 245 , 10, 60)
                self.guess.setGeometry(295, 300 , 50, 50)
            self.guess.setText(str(self.data[self.count - 1]))
            self.attempts.setText('Number of Attempts: ' + str(self.count))
            self.attempts.setText(f"{self.attempts.text()} | Success | Found: {self.data[self.count - 1]}")
            self.clock.stop()
            return
        else:
            try:
                self.line.setGeometry(50 + int((self.count - 1) * 490 / (len(self.data) - 1)), 245 , 10, 60)
                self.guess.setGeometry(50 + int((self.count - 1) * 490 / (len(self.data) - 1)), 300 , 50, 50)
            except ZeroDivisionError:
                self.line.setGeometry(295, 245 , 10, 60)
                self.guess.setGeometry(295, 300 , 50, 50)
                self.attempts.setText('Number of Attempts: ' + str(self.count))
                self.attempts.setText(self.attempts.text() + ' | Failed | Not in List')
                self.clock.stop()
                return
            self.guess.setText(str(self.data[self.count - 1]))
            self.attempts.setText('Number of Attempts: ' + str(self.count))
            self.block1.setGeometry(50, 250, int((self.count - 1) * 490 / (len(self.data) - 1)), 50)