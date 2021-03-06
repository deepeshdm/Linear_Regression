import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def PredictSalary(experience):
    df = pd.read_csv("Salary_Data.csv")

    x_values = np.array(df["YearsExperience"].values)
    y_values = np.array(df["Salary"].values)

    # Calculating Slope & Intercept using the formula.
    n = len(x_values)
    x_mean = np.mean(x_values)
    y_mean = np.mean(y_values)
    numerator_value = 0
    denominator_value = 0

    for i in range(n):
        numerator_value += (x_values[i] - x_mean) * (y_values[i] - y_mean)
        denominator_value += (x_values[i] - x_mean) ** 2

    m = numerator_value / denominator_value
    b = y_mean - (m * x_mean)

    # Parameter passed to the function.
    x = experience
    y = m * x + b

    y_rounded = round(y, 0)
    print("Salary for a Candidate with Experience of {} is {} ".format(x, y_rounded))

    # Plots the dataset in a scatterplot.
    plt.scatter(x_values, y_values, edgecolors="red", color="blue", alpha=0.6)
    plt.xlabel("Experience (years)")
    plt.ylabel("Salary")
    plt.title("Salary Per Month")
    plt.legend()
    plt.show()


PredictSalary(7)

