from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QVBoxLayout, QWidget, QMessageBox, QLabel, QRadioButton, QHBoxLayout, QGroupBox, QGridLayout, QPushButton, QButtonGroup, QComboBox
from PyQt5 import QtGui


# Only needed for access to command line arguments
import sys
from information_processor_model import QuestionModel
from QuestionController import QuestionController


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

        question_model = QuestionModel()
        self.result_button = QPushButton("Show me my results")
        self.result_button.clicked.connect(lambda: question_model.digital_twin_training())

        self.exit_button = QPushButton("Exit")
        self.msg = QWidget()
        self.msg = self.exit_button.clicked.connect(self.generatePopUpBox)
    
        # Adding widgets to the layout 
        layout.addWidget(self.questionnaire_button)
        layout.addWidget(self.result_button)
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
    def generate_likert_scale(self, label, row, radio_number):
        button_group = QButtonGroup()
        self.grid_layout.addWidget(label, row, 0)

        for i in range(radio_number): 
            rb = QRadioButton(str(i))
            button_group.addButton(rb)
            self.grid_layout.addWidget(rb, row, i+1)

        return button_group

    def is_checked(self, button_group): 
        for button in button_group.findChildren(QRadioButton):
            if button.isChecked():
                return button 
    
    # hopefully a temporary function lol             

    def __init__(self):
        super().__init__()
        self.group_box = QGroupBox("Grid")
        q_controller = QuestionController(15) 
        question_model = QuestionModel()

        self.setWindowTitle("Enter your answers")
#        
        windowLayout = QVBoxLayout() 
        self.horizontalGroupBox = QGroupBox("Warwick-Edinburgh Mental Wellbeing Scale (WEMWBS)")
        windowLayout.addWidget(self.horizontalGroupBox)

        self.grid_layout = QGridLayout()
        self.grid_layout.setColumnStretch(1, 4)
        self.grid_layout.setColumnStretch(2, 4)
            
        # Antidepressant question and list
        antidepressants_list = ["None", "Fluoxetine", "Citalopram", "Sertraline"]
        self.model = QuestionModel(question="What type of antidepressant are you on?")
        self.question = QLabel(self.model.data())
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(antidepressants_list)
        self.grid_layout.addWidget(self.question, 0, 0)
        self.grid_layout.addWidget(self.combo_box, 0, 1)
        
        # Headers
        self.grid_layout.addWidget(QLabel('Statements'), 1, 0)
        self.grid_layout.addWidget(QLabel('None of the time'), 1, 1)
        self.grid_layout.addWidget(QLabel('Rarely'), 1, 2)
        self.grid_layout.addWidget(QLabel('Some of the time'), 1, 3)
        self.grid_layout.addWidget(QLabel('Often'), 1, 4)
        self.grid_layout.addWidget(QLabel('All the time'), 1, 5)

        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                widget.setFont(QtGui.QFont("Times",weight=QtGui.QFont.Bold))


        # Labels
        self.model = QuestionModel(question="I am feeling optimistic about the future")
        self.question1 = QLabel(self.model.data())
        self.button_group1 = self.generate_likert_scale(self.question1, 2, 5) # Necessary to store otherwise garbage collection
        
        self.button_group1.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group1.checkedId(), 1))

        self.model = QuestionModel(question="I've been feeling useful")
        self.question2 =QLabel(self.model.data())
        self.button_group2 = self.generate_likert_scale(self.question2, 3, 5)
        self.button_group2.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group2.checkedId(), 2))

        self.model = QuestionModel(question="I've been feeling relaxed")
        self.question3 = QLabel(self.model.data())
        self.button_group3 = self.generate_likert_scale(self.question3, 4, 5)
        self.button_group3.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group3.checkedId(), 3))


        self.model = QuestionModel(question="I've been feeling interested in other people")
        self.question4 = QLabel(self.model.data())
        self.button_group4 = self.generate_likert_scale(self.question4, 5,5 )
        self.button_group4.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group4.checkedId(), 4))

        self.model = QuestionModel(question="I've had energy to spare")
        self.question5 = QLabel(self.model.data())
        self.button_group5 = self.generate_likert_scale(self.question5, 6, 5)
        self.button_group5.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group5.checkedId(), 5))

        
        self.model = QuestionModel(question="I've been dealing with problems well")
        self.question6 = QLabel(self.model.data())
        self.button_group6 = self.generate_likert_scale(self.question6, 7, 5)
        self.button_group6.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group6.checkedId(), 6))

        
        self.question7 = QuestionModel(question="I've been thinking clearly")
        self.question7 = QLabel(self.model.data())
        self.button_group7 = self.generate_likert_scale(self.question7, 8, 5)
        self.button_group7.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group7.checkedId(), 7))


        self.model = QuestionModel(question="I've been feeling good about myself") 
        self.question8 = QLabel(self.model.data())
        self.button_group8 = self.generate_likert_scale(self.question8, 9, 5)
        self.button_group8.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group8.checkedId(), 8))

                
        self.model = QuestionModel(question="I've been feeling close to other people")
        self.question9 = QLabel(self.model.data())
        self.button_group9 = self.generate_likert_scale(self.question9, 10, 5)
        self.button_group9.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group9.checkedId(), 9))

        self.model = QuestionModel(question="I've been feeling confident")
        self.question10 = QLabel(self.model.data())
        self.button_group10 = self.generate_likert_scale(self.question10, 11, 5)
        self.button_group10.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group10.checkedId(), 10))


        self.model = QuestionModel(question="I've been able to make up my own mind about things")
        self.question11 = QLabel(self.model.data())
        self.button_group11 = self.generate_likert_scale(self.question11, 12, 5)
        self.button_group11.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group11.checkedId(), 11))


        self.model = QuestionModel(question="I've been feeling loved")
        self.question12 = QLabel(self.model.data())
        self.button_group12 =  self.generate_likert_scale(self.question12, 13, 5)
        self.button_group12.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group12.checkedId(), 12))


        self.model = QuestionModel(question="I've been interested in new things")
        self.question13 = QLabel(self.model.data())
        self.button_group13 = self.generate_likert_scale(self.question13, 14, 5)
        self.button_group13.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group13.checkedId(), 13))


        self.model = QuestionModel(question="I've been feeling cheerful")
        self.question14 = QLabel(self.model.data())
        self.button_group14 = self.generate_likert_scale(self.question14, 15, 5)
        self.button_group14.buttonClicked.connect(lambda: q_controller.extract_information(self.button_group14.checkedId(), 14))


        self.continue_button = QPushButton('Continue')
        self.grid_layout.addWidget(self.continue_button)
        self.continue_button.clicked.connect(lambda: question_model.digital_twin_training())

        self.horizontalGroupBox.setLayout(self.grid_layout)
        self.horizontalGroupBox.show()



app = QApplication([])

window = MainWindow()
window.show()

# question1 = QLabel("I am feeling optimistic about the future")
# QuestionnaireWindow.generate_likert_scale(question1, 0)

app.exec()