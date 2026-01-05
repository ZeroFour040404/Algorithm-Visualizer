from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer
import math
import sys

class BinarySearchApp(QMainWindow):
    def __init__(self, my_list, target):
        super().__init__()
        self.my_list = [
            int(x.strip())
            for x in my_list.split(",")
            if x.strip()
        ]
        self.target = int(target)
        print(self.my_list, type(self.my_list))
        print(self.target, type(self.target))
        self.initUI()
        self.first = 0
        self.last = len(self.my_list) - 1
        

    def initUI(self):
        self.setWindowTitle('Binary Search Algorithm')
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon('icon.png'))

        self.label = QLabel('Binary Search Algorithm', self)
        self.label.setFont(QFont('Arial', 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 30, 300, 50)

        self.button = QPushButton('Start Search', self)
        self.button.setFont(QFont('Arial', 14))
        self.button.setGeometry(100, 100, 200, 40)
        self.button.clicked.connect(self.start_search)

        self.lower_bound = QLabel(str(self.my_list[0]), self)
        self.lower_bound.setFont(QFont('Arial', 14))    
        self.lower_bound.setGeometry(45, 150, 50, 50)
        self.lower_bound.setStyleSheet("""
                                       font-weight: bold;
                                       """)

        self.upper_bound = QLabel(str(self.my_list[len(self.my_list) - 1]), self)
        self.upper_bound.setFont(QFont('Arial', 14))
        self.upper_bound.setGeometry(340, 150, 50, 50)
        self.upper_bound.setStyleSheet("""
                                       font-weight: bold;
                                       """)

        self.box = QLabel('', self)
        self.box.setFont(QFont('Arial', 12))    
        self.box.setGeometry(50, 200, 300, 50)
        self.box.setAlignment(Qt.AlignCenter)
        self.box.setStyleSheet("""
                               border: 1px solid black;
                               background-color: green;
                               """)
        
        self.line = QLabel('', self)
        self.line.setGeometry(195, 195, 10, 60)
        self.line.setStyleSheet("""
                                background-color: yellow;
                                """)
        
        self.guess = QLabel('', self)
        self.guess.setFont(QFont('Arial', 12))
        self.guess.setGeometry(195, 250, 50, 50)
        self.guess.setStyleSheet("""
                                 color: blue;
                                 """)
        
        self.clock = QTimer(self)
        self.clock.timeout.connect(self.start_search)

    def start_search(self):
        # Placeholder for binary search logic
        mid = math.floor((self.first + self.last) // 2)
        if self.first > self.last:
            self.box.setText("Failed")
        
        print(f"Checking middle value: {self.my_list[mid]}")
        if self.my_list[mid] == self.target:
            self.line.setGeometry(50 + int(mid * 290 / (self.my_list[-1] - self.my_list[0])), 195 , 10, 60)
            self.guess.setGeometry(40 + int(mid * 290 / (self.my_list[-1] - self.my_list[0])), 250 , 50, 50)
            self.guess.setText(str(self.my_list[mid]))
            self.box.setText(f"Success | Found: {self.my_list[mid]}")
            self.clock.stop()
            return
        elif self.my_list[mid] > self.target:
            self.last = mid - 1
            print('self.last',self.last)
        else:
             self.first = mid + 1
             print('self.first',self.first)
             
        self.line.setGeometry(50 + int(mid * 290 / (self.my_list[-1] - self.my_list[0])), 195 , 10, 60)
        self.guess.setGeometry(40 + int(mid * 290 / (self.my_list[-1] - self.my_list[0])), 250 , 50, 50)
        self.guess.setText(str(self.my_list[mid]))
             
        self.clock.start(1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BinarySearchApp("1,2,3,4", "1")
    sys.exit(app.exec_())