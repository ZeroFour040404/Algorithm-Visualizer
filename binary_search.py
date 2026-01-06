from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer
import math
import sys
import tkinter

class BinarySearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clock = QTimer(self)
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
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
        self.line.setGeometry(300, 245, 0, 60)
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
        
        self.range_low = QLabel('a', self)
        self.range_low.setFont(QFont('Arial', 10)) 
        self.range_low.setGeometry(50, 200, 0, 50)
        self.range_low.setStyleSheet("""
                                     color: red;
                                     """)   
        
        self.range_high = QLabel('a', self)
        self.range_high.setFont(QFont('Arial', 10)) 
        self.range_high.setGeometry(540, 200, 0, 50)
        self.range_high.setStyleSheet("""
                                     color: red;
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
        self.block1.setGeometry(50, 250, 0, 50)
        self.block2.setGeometry(50, 250, 0, 50)
        self.line.setGeometry(300, 245, 0, 60)
        self.range_high.setText('')
        self.range_low.setText('')
        self.guess.setText('')
                    
        self.clock.start(1000)

    def continue_search(self):
        # Placeholder for binary search logic
        self.count += 1
        self.mid = math.floor((self.first + self.last) / 2)
        if self.first > self.last:
            self.box.setText("Failed")
            self.attempts.setText(self.attempts.text() + ' | Failed')
            self.clock.stop()
            return
        
        print(f"Checking self.middle value: {self.data[self.mid]}")
        if self.data[self.mid] == self.value:
            self.line.setGeometry(50 + int(self.mid * 490 / (self.data[-1] - self.data[0])), 245 , 10, 60)
            self.guess.setGeometry(50 + int(self.mid * 490 / (self.data[-1] - self.data[0])), 300 , 50, 50)
            self.guess.setText(str(self.data[self.mid]))
            self.attempts.setText('Number of Attempts: ' + str(self.count))
            self.attempts.setText(f"{self.attempts.text()} | Success | Found: {self.data[self.mid]}")
            self.clock.stop()
            return
        elif self.data[self.mid] > self.value:
            self.last = self.mid - 1
            print('self.last',self.last)
            self.timer2.start(990)
            self.timer2.timeout.connect(self.set_block2)
        else:
             self.first = self.mid + 1
             print('self.first',self.first)
             self.timer1.start(990)
             self.timer1.timeout.connect(self.set_block1)
             
        self.line.setGeometry(50 + int(self.mid * 490 / (self.data[-1] - self.data[0])), 245 , 10, 60)
        self.guess.setGeometry(50 + int(self.mid * 490 / (self.data[-1] - self.data[0])), 300 , 50, 50)
        self.guess.setText(str(self.data[self.mid]))
            
        self.attempts.setText('Number of Attempts: ' + str(self.count))
        
        
    def set_block1(self):
        self.block1.setGeometry(50, 250, int(self.mid * 500 / (self.data[-1] - self.data[0])), 50)
        self.range_low.setGeometry(50 + int(self.mid * 500 / (self.data[-1] - self.data[0])), 200, 50, 50)
        self.range_low.setText(str(self.data[self.mid]))
        self.timer1.stop()
        
    
    def set_block2(self):
        self.block2.setGeometry(50 + int(self.mid * 500 / (self.data[-1] - self.data[0])), 250, int(500 - (int(self.mid * 500 / (self.data[-1] - self.data[0])))), 50)
        self.range_high.setGeometry(50 + int(self.mid * 500 / (self.data[-1] - self.data[0])), 200, 50, 50)
        self.range_high.setText(str(self.data[self.mid]))
        self.timer2.stop()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BinarySearchApp()
    sys.exit(app.exec_())