import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import AutoDateLocator, DateFormatter, datestr2num, date2num, num2date
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree

class DigitalTwin:
    def __init__(self, column_list):
        self.column_list = column_list

    def total_scores(self, training_data):
        date_list = []
        mean_list = []
        antidepressant_list = []

        for entry_dict in training_data:
            counter = 0
            for column_name, value in entry_dict.items():
                if column_name in self.column_list:
                    counter += value
                if column_name == 'date':
                    date_list.append(value)
                if column_name == 'antidepressant':
                    antidepressant_list.append(value)
            mean_list.append(round((counter/len(self.column_list))))

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

    def fit_regression_model(self, dataset):
        models = dict()
        reformatted_dataset = dict()

        for drug, data in dataset.items():
            dates, scores = zip(*data)
            dates = datestr2num(dates)

            reformatted_dataset[drug] = (dates, scores)

            # Calculate weekly change in scores as the feature 
            scores = np.array(scores)

            # Weekly change 
            weekly_change = np.diff(scores, prepend=scores[0]).reshape(-1, 1)

            decision_tree = DecisionTreeRegressor()
            decision_tree.fit(weekly_change, scores)
            models[drug] = decision_tree

        fig, ax = plt.subplots()
        fig.canvas.setWindowTitle('Wellbeing Model')

        for drug in reformatted_dataset:
            data = reformatted_dataset[drug]
            colour = self.decide_colours(drug)
            ax.scatter(data[0], data[1], s=20, edgecolor="black", c=colour, label=str(drug))

            # Predict the scores for once a week for the next month
            end_date = date2num(dt.date.today() + dt.timedelta(weeks=4))
            all_dates = np.arange(date2num(dt.date.today()), end_date + 1, 7)
            all_dates = all_dates.reshape(-1, 1)

            # Calculate weekly change in scores for the next month
            initial_scores = np.array(data[1])[-1]
            next_week_scores = models[drug].predict([[initial_scores]])[0]
            predicted_scores = np.concatenate(([initial_scores], next_week_scores * np.ones(4)))
            weekly_change = np.diff(predicted_scores, prepend=predicted_scores[0]).reshape(-1, 1)
            predicted_dates = num2date(all_dates.flatten())

            # Use the appropriate decision tree model for each drug to make predictions
            predicted_scores = models[drug].predict(weekly_change)
            predicted_dates = num2date(all_dates.flatten())

            # Plot the predicted scores as a dashed line
            ax.plot(predicted_dates, predicted_scores, linestyle='dashed',  c=colour, label="Predicted wellbeing for " + str(drug))

        week_from_today = datestr2num((dt.date.today() + dt.timedelta(weeks=4)).strftime('%Y-%m-%d'))
        week_from_today = week_from_today.reshape(-1, 1)

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
        plt.show()