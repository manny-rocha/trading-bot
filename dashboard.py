from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Automated Stock Trading Program')
        layout = QVBoxLayout()
        label = QLabel("Stock Information will be displayed here.")
        start_button = QPushButton('Start Trading')
        stop_button = QPushButton('Stop Trading')
        layout.addWidget(label)
        layout.addWidget(start_button)
        layout.addWidget(stop_button)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setStyleSheet("""
        QWidget {
            background-color: #2b2b2b;
        }
        QLabel {
            color: #fafafa;
        }
        QPushButton {
            background-color: #3d3d3d;
            color: #fafafa;
            border: 2px solid #fafafa;
            padding: 10px;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: #fafafa;
            color: #2b2b2b;
        }
        """)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
