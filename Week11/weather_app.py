"""Weather Explorer: pick a station and a year, see a summary and a chart.

Run this file in Thonny with F5. The challenges in week11-gui-guide.ipynb
build on it, so save a copy before you start changing it.
"""
import csv
import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QComboBox, QLineEdit, QPushButton, QLabel)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

sys.path.append("..")
from coursetools import data_file

STATIONS = ["Armagh", "Oxford", "Sheffield", "Lerwick", "Camborne"]


def load_year(station, year):
    """Return the months, maximum temperatures and rainfall for one station and year."""
    months = []
    tmax = []
    rain = []
    with open(data_file("uk_weather.csv")) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == station and row[1] == str(year) and row[3] != "" and row[6] != "":
                months.append(int(row[2]))
                tmax.append(float(row[3]))
                rain.append(float(row[6]))
    return months, tmax, rain


class WeatherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Explorer")
        self.resize(800, 600)

        self.station_box = QComboBox()
        self.station_box.addItems(STATIONS)
        self.year_box = QLineEdit()
        self.year_box.setPlaceholderText("Year, for example 2024")
        self.show_button = QPushButton("Show")
        self.show_button.clicked.connect(self.show_year)
        self.summary = QLabel("Pick a station and a year, then press Show")

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        controls = QHBoxLayout()
        controls.addWidget(self.station_box)
        controls.addWidget(self.year_box)
        controls.addWidget(self.show_button)

        layout = QVBoxLayout()
        layout.addLayout(controls)
        layout.addWidget(self.summary)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def show_year(self):
        station = self.station_box.currentText()
        try:
            year = int(self.year_box.text())
        except ValueError:
            self.summary.setText("The year must be a whole number, like 2024")
            return

        months, tmax, rain = load_year(station, year)
        if len(months) == 0:
            self.summary.setText(f"There is no data for {station} in {year}")
            return

        warmest = 0
        for i in range(len(tmax)):
            if tmax[i] > tmax[warmest]:
                warmest = i
        self.summary.setText(f"{station} {year}: {sum(rain):.1f} mm of rain, "
                             f"warmest month {months[warmest]} at {tmax[warmest]} C")

        self.figure.clear()
        axes = self.figure.add_subplot()
        axes.plot(months, tmax, marker="o")
        axes.set_xlabel("Month")
        axes.set_ylabel("Mean daily maximum (°C)")
        axes.set_title(f"{station}, {year}")
        self.figure.tight_layout()       # leave room for the axis labels
        self.canvas.draw()


app = QApplication(sys.argv)
window = WeatherWindow()
window.show()
app.exec()
