# Prerequisites
This project was developed on Python 3.8 so to run this project, this would be recommended, but later versions should be fine as well. 

# Installation
Please use pip to install the following libraries:
- Matplotlib 3.7.1
- Scikit-learn 1.0.2 
- PyQt5 5.15.9
- PyQt5-Qt5 5.15.2
- PyQt5-sip 12.12.1
- pytest 7.3.2
- python-dateutil 2.8.2
- numpy 1.22.3
- DateTime 5.1
- bcrypt 4.0.1

Please, in case, also have:
- sqlite3 3.31.1 

# How to Run
Once you have installed the above libraries, navigate to the ssri_project folder, open a command terminal and type in python project_gui.py. Then, you can navigate around the application.

# What the Warwick and Edinburgh Mental Wellbeing Scale Is
This is the 14-item-scale questionnaire that you will be filling out. This tracks mental wellbeing within the general population and was developed by Warwick and Edinburgh University. Responses for this are on a five-point scale ranging from 'None of the Time' to 'All of the Time'. You will need to sign up an account to  answer the questionnaire. On the questionnaire, there will be some statements about feelings and thoughts. Please select the answer that best describes your experience of each over the last 2 weeks. 

# How your data is used
By signing up with a username and password, the data you enter will be used in the program to predict future wellbeing based on the quantitative data entered. If you want your data deleted, as this is a proof-of-concept, you will have to delete the entries manually from antidepressant.db. The data is completely offline and does not go anywhere outside of this program.
