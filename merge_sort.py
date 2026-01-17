from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer
import sys
import show_merge_sort

class MergeSortApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Merge Sort Algorithm')
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon('icon.png'))
        
        self.label = QLabel('Merge Sort Algorithm', self)
        self.label.setFont(QFont('Arial', 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 30, 600, 50)
        
        self.my_list = QLineEdit(self)
        self.my_list.setFont(QFont('Arial', 12))   
        self.my_list.setPlaceholderText('Enter list of values')
        self.my_list.setGeometry(100, 100, 400, 50)
        
        self.button = QPushButton('Start Sort', self)
        self.button.setFont(QFont('Arial', 14))
        self.button.setGeometry(200, 160, 200, 40)
        self.button.clicked.connect(self.start_sort)
        
        self.error = QLabel('', self)
        self.error.setFont(QFont('Arial', 12))   
        self.error.setGeometry(50, 230, 400, 50)
        self.error.setStyleSheet("""
                                        font-weight: bold;
                                        color: red;
                                        """)
        
        
        self.show()
        
    def start_sort(self):
        self.error.setText('')
        text = self.my_list.text()
        try:
            self.data = [int(x.strip()) for x in text.split(",") if x.strip()]
        except ValueError:
            self.error.setText('Use comma-separated numbers only!!')
            return -1
       
        sms = show_merge_sort.ShowMergeSort(self.data)
        sms.sort()       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MergeSortApp()
    sys.exit(app.exec_()) 