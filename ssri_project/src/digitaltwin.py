import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import AutoDateLocator, DateFormatter, datestr2num, date2num
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

        return antidepressant_list, mean_list, date_list

    def decide_colours(self, drug):
        drug = drug.lower()
        if drug == "none":
            return "green"
        if drug == "citalopram": 
            return "magenta"
        if drug == "sertraline":
            return "blue"
        else:
            return "red"

    # X will be the overall score 
    def fit_regression_model(self, dataset):
        models = dict()
        reformatted_dataset = dict()

        for drug, data in dataset.items():
            dates, scores = zip(*data)
            dates = datestr2num(dates)
            
            reformatted_dataset[drug] = (dates, scores)

            # Convert to matplotlib's internal date format.
            x = np.array(dates).reshape(-1, 1)
            y = np.array(scores).reshape(-1, 1)

            decision_tree = DecisionTreeRegressor()
            decision_tree.fit(x, y)

            models[drug] = decision_tree

        #x_test = np.arange(x.all()).reshape(-1, 1)
        week_from_today = dt.date.today() + dt.timedelta(weeks=8)
        week_from_today = datestr2num(week_from_today.strftime('%Y-%m-%d'))
        week_from_today = np.array(week_from_today).reshape(-1, 1)
        predictions = dict()

        for drug in dataset:
            predictions[drug] = models[drug].predict(week_from_today)

        # Plot the results
        fig = plt.figure()
        fig.canvas.setWindowTitle('Wellbeing Model')

        ax = fig.add_subplot(1,1,1)

        for drug in reformatted_dataset:
            data = reformatted_dataset[drug]
            colour = self.decide_colours(drug)
            ax.scatter(data[0], data[1], s=20, edgecolor="black", c=colour, label=drug)
            ax.scatter(week_from_today, predictions[drug], s=20, marker="X", c=colour, label="wellbeing prediction for " + str(drug))

        ax.xaxis_date()  
        ax.set_title("Decision Tree Regression to show wellbeing results")
        ax.set_xlabel("Time")
        ax.set_ylabel("Overall Score")
        ax.set_ylim([0, 5])
        ax.xaxis.set_major_locator(
            AutoDateLocator(minticks = 3, interval_multiples = False))
        ax.set_xticklabels(ax.get_xticks(), rotation = 45)
        ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))

        ax.legend()
        fig.show()
    

            

