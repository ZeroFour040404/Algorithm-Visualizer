from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer
import sys
import binary_search
import linear_search
import merge_sort

class AlgorithmVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Algorithm Visualizer')
        self.setGeometry(100, 100, 800, 600)
        # self.setWindowIcon(QIcon('icon.png'))

        self.titleLabel = QLabel('Algorithm Visualizer', self)
        self.titleLabel.setFont(QFont('Arial', 24))
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setGeometry(200, 50, 400, 50)

        self.linear_search_button = QPushButton('Linear Search', self)
        self.linear_search_button.setFont(QFont('Arial', 14))
        self.linear_search_button.setGeometry(250, 150, 300, 40)
        self.linear_search_button.clicked.connect(self.startVisualization)
        
        self.binary_search_button = QPushButton('Binary Search', self)
        self.binary_search_button.setFont(QFont('Arial', 14))
        self.binary_search_button.setGeometry(250, 200, 300, 40)
        self.binary_search_button.clicked.connect(self.startBinarySearch)
        
        self.binary_search_button = QPushButton('Merge Sort', self)
        self.binary_search_button.setFont(QFont('Arial', 14))
        self.binary_search_button.setGeometry(250, 250, 300, 40)
        self.binary_search_button.clicked.connect(self.startMergeSort)

        self.show()

    def startVisualization(self):
        self.linear_search_app = linear_search.LinearSearchApp()
        self.linear_search_app.show()

    def startBinarySearch(self):
        self.binary_search_app = binary_search.BinarySearchApp()
        self.binary_search_app.show()
        
    def startMergeSort(self):
        self.merge_sort_app = merge_sort.MergeSortApp()
        self.merge_sort_app.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlgorithmVisualizer()
    sys.exit(app.exec_()) 