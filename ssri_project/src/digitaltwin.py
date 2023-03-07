import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import AutoDateLocator, DateFormatter, datestr2num
from sklearn.tree import DecisionTreeRegressor

# Doing a regression predictor 
# Using a decision tree 
class DigitalTwin: 
    # Possibly consider using a dictionary instead of a list for mean? 
    def __init__(self, column_list):
        self.column_list = column_list
        
    # Average the score
    def total_scores(self, training_data): 
        # List that will contain the mean score 
        date_list = [] 
        mean_list = [] 
        antidepressant_list = []

        # Can't guarantee entries will be a certain order in a dictionary 
        for entry_dict in training_data:
            # Making an assumption that there will always be one date and one score
            counter = 0
            for column_name, value in entry_dict.items():
                if column_name in self.column_list:
                    counter += value
                if column_name == 'date': 
                    date_list.append(value)
                if column_name == 'antidepressant':
                    antidepressant_list.append(value)
            mean_list.append(counter/len(self.column_list))
            print(date_list)

        self.fit_regression_model(mean_list, date_list)
        return antidepressant_list, mean_list, date_list


    # X will be the overall score 
    def fit_regression_model(self, dataset, dates):
        y = np.array(dataset).reshape(-1, 1)
        # Convert to matplotlib's internal date format.
        x = np.array(datestr2num(dates)).reshape(-1, 1)
        print(x)

        # Max depth = max depth of the tree 
        regr_1 = DecisionTreeRegressor()
        regr_1.fit(x, y)
        
        # x_test = np.arange(x.all()).reshape(-1, 1)
        # x_test = np.sort(x_test).reshape(-1, 1)
        week_from_today = dt.date.today() + dt.timedelta(days=7)
        week_from_today = week_from_today.strftime('%Y-%m-%d')
        x_test = [datestr2num(week_from_today)]
        y_1 = regr_1.predict(np.array(x_test).reshape(1, -1))

        print(y_1)

        # Plot the results
        fig = plt.figure()
        fig.canvas.setWindowTitle('Wellbeing Model')
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(x, y, s=20, edgecolor="black", c="darkorange", label="data")
        ax.scatter(x_test, y_1, s=20, edgecolor="black", c="cornflowerblue", label="wellbeing prediction")

        ax.set_title("Decision Tree Regression to show wellbeing results")
        ax.set_xlabel("Time")
        ax.set_ylabel("Overall Score")
        ax.set_ylim([0, 5])
        ax.xaxis_date() 
        ax.xaxis.set_major_locator(
            AutoDateLocator(minticks = 3, interval_multiples = False))
        ax.set_xticklabels(ax.get_xticks(), rotation = 45)
        ax.xaxis.set_major_formatter(DateFormatter("%d/%m/%y"))

        ax.legend()
        fig.show()
    

            

