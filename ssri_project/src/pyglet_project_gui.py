from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QLabel, QRadioButton, QHBoxLayout

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.window = None  # No external window yet.

        self.setWindowTitle("SSRI Project")
        self.questionnaire_button = QPushButton("Answer a questionnaire")
        self.questionnaire_button.clicked.connect(self.show_new_window)

        self.exit_button = QPushButton("Exit")
        self.msg = QWidget()
        self.msg = self.exit_button.clicked.connect(self.generatePopUpBox)
    
        # Adding widgets to the layout 
        layout.addWidget(self.questionnaire_button)
        layout.addWidget(self.exit_button)
        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def generatePopUpBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Are you sure?")
        msg.setText("Are you sure you'd like to exit the program?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.show()
        retval = msg.exec_()

    def show_new_window(self): 
        if self.window is None:
            self.window = QuestionnaireWindow()
        self.window.show()

class QuestionnaireWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.group_box = QGroupBox("Grid")
        self.layout = QHBoxLayout()
        
        grid_layout = QGridLayout()
        grid_layout.setColumnStretch(0, 0)

        # Labels
        self.label = QLabel("I am feeling optimistic about the future")
        self.layout.addWidget(self.label)
        
        radio_button = QRadioButton("1")
        radio_button.value = "1"
        self.layout.addWidget(radio_button)

        radio_button = QRadioButton("2")
        radio_button.value = "2"
        self.layout.addWidget(radio_button)

        radio_button = QRadioButton("3")
        radio_button.value = "3"
        self.layout.addWidget(radio_button)

        radio_button = QRadioButton("4")
        radio_button.value = "4"
        self.layout.addWidget(radio_button)
        
        radio_button = QRadioButton("5")
        radio_button.value = "5"
        self.layout.addWidget(radio_button)

        self.horizontalGroupBox.setLayout(grid_layout)



app = QApplication([])

window = MainWindow()
window.show()

app.exec()
