from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer
import sys

class MergeSortApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Merge Sort Algorithm')
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon('icon.png'))
        
        self.label = QLabel('Merge Sort Algorithm', self)
        self.label.setFont(QFont('Arial', 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 30, 600, 50)
        
        self.my_list = QLineEdit(self)
        self.my_list.setFont(QFont('Arial', 12))   
        self.my_list.setPlaceholderText('Enter list of values (max. 10)')
        self.my_list.setGeometry(100, 100, 400, 50)
        
        self.sorted = QLabel('Number of Attempts: ', self)
        self.sorted.setFont(QFont('Arial', 12))
        self.sorted.setGeometry(50, 350, 500, 50)
        self.sorted.setStyleSheet("""
                                    font-weight: bold;
                                    """)
        
        self.show()
        
    def merge_sort(self):
        text = self.my_list.text()
        try:
            self.data = [int(x.strip()) for x in text.split(",") if x.strip()]
        except ValueError:
            self.sorted.setText('Use comma-separated numbers only!!')
            self.sorted.setStyleSheet("""
                                        font-weight: bold
                                        color: red;
                                        """)
            return -1
        
        mid = len(self.data)//2
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MergeSortApp()
    sys.exit(app.exec_()) 