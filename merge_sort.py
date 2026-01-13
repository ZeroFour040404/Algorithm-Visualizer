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
        
        self.index0 = QLabel('0', self)
        self.index0.setFont(QFont('Arial', 12))
        self.index0.setGeometry(50, 150, 50, 50)
        self.index0.setAlignment(Qt.AlignCenter)
        self.index0.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index1 = QLabel('1', self)
        self.index1.setFont(QFont('Arial', 12))
        self.index1.setGeometry(100, 150, 50, 50)
        self.index1.setAlignment(Qt.AlignCenter)
        self.index1.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index2 = QLabel('2', self)
        self.index2.setFont(QFont('Arial', 12))
        self.index2.setGeometry(150, 150, 50, 50)
        self.index2.setAlignment(Qt.AlignCenter)
        self.index2.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index3 = QLabel('3', self)
        self.index3.setFont(QFont('Arial', 12))
        self.index3.setGeometry(200, 150, 50, 50)
        self.index3.setAlignment(Qt.AlignCenter)
        self.index3.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index4 = QLabel('4', self)
        self.index4.setFont(QFont('Arial', 12))
        self.index4.setGeometry(250, 150, 50, 50)
        self.index4.setAlignment(Qt.AlignCenter)
        self.index4.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index5 = QLabel('5', self)
        self.index5.setFont(QFont('Arial', 12))
        self.index5.setGeometry(300, 150, 50, 50)
        self.index5.setAlignment(Qt.AlignCenter)
        self.index5.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index6 = QLabel('6', self)
        self.index6.setFont(QFont('Arial', 12))
        self.index6.setGeometry(350, 150, 50, 50)
        self.index6.setAlignment(Qt.AlignCenter)
        self.index6.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index7 = QLabel('7', self)
        self.index7.setFont(QFont('Arial', 12))
        self.index7.setGeometry(400, 150, 50, 50)
        self.index7.setAlignment(Qt.AlignCenter)
        self.index7.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index8 = QLabel('8', self)
        self.index8.setFont(QFont('Arial', 12))
        self.index8.setGeometry(450, 150, 50, 50)
        self.index8.setAlignment(Qt.AlignCenter)
        self.index8.setStyleSheet("""
                                    border: 1px solid black;
                                    """)
        
        self.index9 = QLabel('9', self)
        self.index9.setFont(QFont('Arial', 12))
        self.index9.setGeometry(500, 150, 50, 50)
        self.index9.setAlignment(Qt.AlignCenter)
        self.index9.setStyleSheet("""
                                    border: 1px solid black;
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