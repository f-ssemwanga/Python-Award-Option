"""Step 2: a button that does something. Run this file in Thonny with F5."""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class ConverterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Celsius to Fahrenheit")

        self.celsius_box = QLineEdit()
        self.celsius_box.setPlaceholderText("Temperature in C")
        self.button = QPushButton("Convert")
        self.result = QLabel("Type a temperature and press Convert")

        self.button.clicked.connect(self.convert)     # no brackets: we pass the method, not call it

        layout = QVBoxLayout()
        layout.addWidget(self.celsius_box)
        layout.addWidget(self.button)
        layout.addWidget(self.result)
        self.setLayout(layout)

    def convert(self):
        try:
            celsius = float(self.celsius_box.text())
        except ValueError:
            self.result.setText("Please type a number")
            return
        fahrenheit = celsius * 9 / 5 + 32
        self.result.setText(f"{celsius:.1f} C is {fahrenheit:.1f} F")


app = QApplication(sys.argv)
window = ConverterWindow()
window.show()
app.exec()
