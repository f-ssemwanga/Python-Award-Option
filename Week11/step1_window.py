"""Step 1: an empty window. Run this file in Thonny with F5."""
import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My first window")
window.resize(400, 200)
window.show()

app.exec()          # wait here, handling clicks and key presses, until the window closes
print("Window closed")
