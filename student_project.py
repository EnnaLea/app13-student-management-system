import sys

from PyQt6.QtWidgets import QApplication, QLabel, \
    QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox


class AverageSpeedCalculator(QWidget):
    def __init__(self):

        super().__init__()

        self.setWindowTitle("Average Speed Calculator")

        grid = QGridLayout()

        # Create widgets
        self.distance_label = QLabel("Distance:")
        self.distance_label_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Metric(km)', 'Imperial(miles)'])

        self.times_hours_label = QLabel("Time(hours):")
        self.times_hours_label_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)

        self.output_label = QLabel("")

        # Add widgets to the grid
        grid.addWidget(self.distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(self.times_hours_label, 1, 0)
        grid.addWidget(self.times_hours_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1,)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)



    def calculate_speed(self):
        distance = float(self.distance_label_edit.text())
        time = float(self.times_hours_label_edit.text())


        if self.combo.currentText() == 'Metric(km)':
            average_speed = round(distance / time, 2)
            self.output_label.setText(f"Average speed: {average_speed} km/h.")

        if self.combo.currentText() == 'Imperial(miles)':
            distance_converted = distance * 0.6214
            average_speed = round(distance_converted / time, 2)
            self.output_label.setText(f"Average speed: {average_speed} mph.")








app = QApplication(sys.argv)
speed_calculator = AverageSpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())

