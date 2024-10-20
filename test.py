import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QVBoxLayout, QWidget

class DropdownExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dropdown Example')
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.label = QLabel('Select an option:', self)
        layout.addWidget(self.label)

        self.dropdown = QComboBox(self)
        self.dropdown.addItems(['MontBlanc', 'Aces', 'Spnniers', 'Unicorns'])
        self.dropdown.currentIndexChanged.connect(self.selection_changed)
        layout.addWidget(self.dropdown)

        self.central_widget.setLayout(layout)

    def selection_changed(self, index):
        self.label.setText(f'Selected: {self.dropdown.currentText()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DropdownExample()
    ex.show()
    sys.exit(app.exec_())
