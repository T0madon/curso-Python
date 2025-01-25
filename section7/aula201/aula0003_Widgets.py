#type: ignore
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)

button = QPushButton('Button Text')
button.setStyleSheet('font-size: 40px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 80px;')

central_widget = QWidget()
layout = QVBoxLayout()

central_widget.setLayout(layout)
layout.addWidget(button)
layout.addWidget(button2)

central_widget.show()
app.exec()