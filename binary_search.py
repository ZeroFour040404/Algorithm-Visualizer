from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer
import math
import sys

class BinarySearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clock = QTimer(self)
        self.clock.timeout.connect(self.continue_search)
        self.count = 0

    def initUI(self):
        self.setWindowTitle('Binary Search Algorithm')
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon('icon.png'))

        self.label = QLabel('Binary Search Algorithm', self)
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
        
        self.block2 = QLabel('', self)
        self.block2.setGeometry(50, 250, 0, 50)
        self.block2.setStyleSheet("""
                                  border: 1px solid black;
                                  background-color: gray;
                                  """)
        
        self.line = QLabel('', self)
        self.line.setGeometry(300, 245, 10, 60)
        self.line.setStyleSheet("""
                                background-color: yellow;
                                """)
        
        self.guess = QLabel('0', self)
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
        
    def start_search(self):
        self.box.setText('')
        self.count = 0
        self.attempts.setText('Number of Attempts: ')
        text = self.my_list.text()
        self.data = [int(x.strip()) for x in text.split(",") if x.strip()]
        self.value = int(self.target.text())
        self.first = 0
        self.last = len(self.data) - 1
        self.lower_bound.setText(str(self.data[0]))
        self.upper_bound.setText(str(self.data[len(self.data) - 1]))
                    
        self.clock.start(1000)

    def continue_search(self):
        # Placeholder for binary search logic
        self.count += 1
        mid = math.ceil((self.first + self.last) / 2)
        if self.first > self.last:
            self.box.setText("Failed")
            return -1
        
        print(f"Checking middle value: {self.data[mid]}")
        if self.data[mid] == self.value:
            self.line.setGeometry(50 + int(mid * 490 / (self.data[-1] - self.data[0])), 245 , 10, 60)
            self.guess.setGeometry(50 + int(mid * 490 / (self.data[-1] - self.data[0])), 300 , 50, 50)
            self.guess.setText(str(self.data[mid]))
            self.attempts.setText('Number of Attempts: ' + str(self.count))
            self.box.setText(f"Success | Found: {self.data[mid]}")
            self.clock.stop()
            return
        elif self.data[mid] > self.value:
            self.last = mid - 1
            print('self.last',self.last)
            self.block2.setGeometry(50 + int(mid * 500 / (self.data[-1] - self.data[0])), 250, int(500 - (int(mid * 500 / (self.data[-1] - self.data[0])))), 50)
        else:
             self.first = mid + 1
             print('self.first',self.first)
             
        self.line.setGeometry(50 + int(mid * 490 / (self.data[-1] - self.data[0])), 245 , 10, 60)
        self.guess.setGeometry(50 + int(mid * 490 / (self.data[-1] - self.data[0])), 300 , 50, 50)
        self.guess.setText(str(self.data[mid]))
            
        self.attempts.setText('Number of Attempts: ' + str(self.count))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BinarySearchApp()
    sys.exit(app.exec_())