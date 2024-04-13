#Loading Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

students = pd.read_csv("Student_Data/students.csv")

#Inspecting first few rows of data
print(tabulate(students.head(), headers="keys"))

#Printing out summary statistics for the dataset
print(tabulate(students.describe(include="all"), headers="keys"))

#Calculating the mean value for math_grade
math_mean = students.math_grade.mean()
print(f"The mean value for math grades is {math_mean}")

#Calculating the median value for math_grade
math_median = students.math_grade.median()
print(f"The median value for math grades is {math_median}")

#Calculating the mode value for math_grade
math_mode = students.math_grade.mode()[0]
print(f"The mode value for math  grade is {math_mode}")

#Calculating the range of math_grade
math_range = students.math_grade.max() - students.math_grade.min()
print(f"The range of math grades is {math_range}")

#Calculating the standard deviation of math_grade
math_std = students.math_grade.std()
print(f"The standard deviation of math grades is {math_std}")

#Calculating the mean absolute deviation of math_grade
math_mad = np.sum(students.math_grade) / students.math_grade.count()
print(f"The mean absolute deviation of math grades is {math_mad}")

#Visualizing the distribution with a Histogram
sns.histplot(x="math_grade", data=students)
plt.show()
plt.clf()

#Visualizing the distribution for quantitative variables with Boxplot
sns.boxplot(x="math_grade", data=students)
plt.show()
plt.clf()

#Calculating the proportion of student's mother's jobs
print(students.Mjob.value_counts(normalize=True))

#Visualizing the relative frequencies of different mother's jobs with a bar chart
sns.countplot(x="Mjob", data=students)
plt.show()
plt.clf()

#Visualizing the relative frequencies of different mother's jobs with a pie chart
students.Mjob.value_counts().plot.pie()
plt.show()
plt.clf()

#Calculating the proportion of student's father's jobs
print(students.Fjob.value_counts(normalize=True))

#Visualizing the relative frequencies of different father's jobs with a pie chart
students.Fjob.value_counts().plot.pie()
plt.show()
plt.clf()

#Visualizing the number of times a student was absent during the school year
sns.histplot(x="absences", data=students)
plt.show()
plt.clf()

#Calculating the mean value for students absences
absences_mean = students.absences.mean()
print(f"The mean value for absences is {absences_mean}")

#Visualizing the proportions of student's addresses
labels = ["Urban", "Rural"]
students.address.value_counts().plot.pie(y="", autopct='%1.1f%%', title="Student's Addresses", labels=labels, legend=True)
plt.show()
plt.clf()