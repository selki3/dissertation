from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QVBoxLayout, QWidget, QMessageBox, QLabel, QRadioButton, QHBoxLayout, QGroupBox, QGridLayout, QPushButton, QButtonGroup

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.window = None  # No external window yet.
        self.exit = False 

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
        msg.buttonClicked.connect(self.button_clicked)
        msg.exec_()

    def button_clicked(self, button): 
        if (button.text() == "&Yes"): 
            sys.exit()
            app.exit()

    def show_new_window(self): 
        if self.window is None:
            self.window = QuestionnaireWindow()
        self.window.show()

class QuestionnaireWindow(QMainWindow):
    def generate_likert_scale(self, label, row):
        button_group = QButtonGroup()
        self.grid_layout.addWidget(label, row, 0)

        rb1 = QRadioButton('1')
        rb2 = QRadioButton('2')
        rb3 = QRadioButton('3')
        rb4 = QRadioButton('4')
        rb5 = QRadioButton('5')

        button_group.addButton(rb1)
        button_group.addButton(rb2)
        button_group.addButton(rb3)
        button_group.addButton(rb4)
        button_group.addButton(rb5)

        self.grid_layout.addWidget(rb1, row, 1)
        self.grid_layout.addWidget(rb2, row, 2)
        self.grid_layout.addWidget(rb3, row, 3)
        self.grid_layout.addWidget(rb4, row, 4)
        self.grid_layout.addWidget(rb5, row, 5)

        return button_group

    def __init__(self):
        super().__init__()
        self.group_box = QGroupBox("Grid")
#        
        windowLayout = QVBoxLayout()
        self.horizontalGroupBox = QGroupBox("Warwick-Edinburgh Mental Wellbeing Scale (WEMWBS)")
        windowLayout.addWidget(self.horizontalGroupBox)

        self.grid_layout = QGridLayout()
        self.grid_layout.setColumnStretch(1, 4)
        self.grid_layout.setColumnStretch(2, 4)
        
        # Headers
        self.grid_layout.addWidget(QLabel('Statements'), 0, 0)
        self.grid_layout.addWidget(QLabel('None of the time'), 0, 1)
        self.grid_layout.addWidget(QLabel('Rarely'), 0, 2)
        self.grid_layout.addWidget(QLabel('Some of the time'), 0, 3)
        self.grid_layout.addWidget(QLabel('Often'), 0, 4)
        self.grid_layout.addWidget(QLabel('All the time'), 0, 5)


        # Labels
        self.question1 = QLabel("I am feeling optimistic about the future")
        self.button_group1 = self.generate_likert_scale(self.question1, 1) # Necessary to store otherwise garbage collection

        self.question2 = QLabel("I've been feeling useful")
        self.button_group2 = self.generate_likert_scale(self.question2, 2)

        self.question3 = QLabel("I've been feeling relaxed")
        self.button_group3 = self.generate_likert_scale(self.question3, 3)

        self.question4 = QLabel("I've been feeling interested in other people")
        self.button_group4 = self.generate_likert_scale(self.question4, 4)
        
        self.question5 = QLabel("I've had energy to spare")
        self.button_group5 = self.generate_likert_scale(self.question5, 5)
        
        self.question6 = QLabel("I've been dealing with problems well")
        self.button_group6 = self.generate_likert_scale(self.question6, 6)
        
        self.question7 = QLabel("I've been thinking clearly")
        self.button_group7 = self.generate_likert_scale(self.question7, 7)
                
        self.question8 = QLabel("I've been feeling good about myself")
        self.button_group8 = self.generate_likert_scale(self.question8, 8)
                
        self.question9 = QLabel("I've been feeling close to other people")
        self.button_group9 = self.generate_likert_scale(self.question9, 9)

        self.question10 = QLabel("I've been feeling confident")
        self.button_group10 = self.generate_likert_scale(self.question10, 10)

        self.question11 = QLabel("I've been able to make up my own mind about things")
        self.button_group11 = self.generate_likert_scale(self.question11, 11)

        self.question12 = QLabel("I've been feeling loved")
        self.button_group12 =  self.generate_likert_scale(self.question12, 12)

        self.question13 = QLabel("I've been interested in new things")
        self.button_group13 = self.generate_likert_scale(self.question13, 13)

        self.question14 = QLabel("I've been feeling cheerful")
        self.button_group14 = self.generate_likert_scale(self.question14, 14)

        self.horizontalGroupBox.setLayout(self.grid_layout)
        self.horizontalGroupBox.show()

app = QApplication([])

window = MainWindow()
window.show()

# question1 = QLabel("I am feeling optimistic about the future")
# QuestionnaireWindow.generate_likert_scale(question1, 0)

app.exec()