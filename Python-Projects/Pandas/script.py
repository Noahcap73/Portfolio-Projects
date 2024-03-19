import pandas as pd
from tabulate import tabulate

#This gets rid of errors trying to tabulate unicode characters
import sys
sys.stdout.reconfigure(encoding='utf-8')

pd.set_option('display.max_colwidth', None)

jeopardy = pd.read_csv("Data_Manipulation/jeopardy.csv")

#Renaming all of the column names
jeopardy = jeopardy.rename(columns={"Show Number": "Show_Number", 
                                    " Air Date": "Air_Date", 
                                    " Round": "Round", 
                                    " Category": "Category", 
                                    " Value": "Value",
                                    " Question": "Question",
                                    " Answer": "Answer"})
#print(tabulate(jeopardy.head(), headers="keys"))

#Changing all of the values from strings to floats

jeopardy["Float_Value"] = jeopardy["Value"].apply(lambda x: float(x.replace("$", "").replace(",", "")) if x != "no value" else 0)


#Creating a function that filters the dataset for questions that contain words in a list of words
def questionFilter(wordList, dataFrame):
  
  #This lowercases all words in wordList and the Questions
  filtered_df = dataFrame.loc[dataFrame["Question"].apply(lambda x: all(word.lower() in x.lower() for word in wordList))] 
  return filtered_df


#Testing questionFilter function
filtered_jeopardy = (questionFilter(["king"], jeopardy))

#Finding the average value for questions that contain a word
print(f"The average value of question that has the word 'king' is {filtered_jeopardy["Float_Value"].mean()}") #Avg value was 771.883

#Creating a function that counts all the unique answers for the filtered dataframe
def uniqueAnswers(dataFrame):
  return dataFrame["Answer"].value_counts()
  
print(uniqueAnswers(filtered_jeopardy))#Henry VIII was the most common answer at 55 times being the answer

#Filtering the dataset to only the 90's
nineties_jeopardy = jeopardy.loc[(jeopardy["Air_Date"] >= "1990-01-01") & (jeopardy["Air_Date"] < "1999-12-31")]
#print(tabulate(date_jeopardy))

#Filtering the 90's dataframe with only the word "Computer" in the question
nineties_computer_questions = questionFilter(["Computer"], nineties_jeopardy)
#print(tabulate(ninetys_computer_questions))

#Filtering the dataset to only the 2000's
thousands_jeopardy = jeopardy.loc[jeopardy["Air_Date"] >= "2000-01-01"]
#print(tabulate(thousands_jeopardy))

#Filtering the 2000's dataframe with only the word "Computer" in the question
thousands_computer_questions = questionFilter(["Computer"], thousands_jeopardy)
#print(tabulate(thousands_computer_questions))


print(f"The 90's had {len(nineties_computer_questions["Question"])} questions with the word 'computer' in it") #98 Questions had "Computer" in the 90's
print(f"The 2000's had {len(thousands_computer_questions["Question"])} questions with the word 'computer' in it") #327 Questions had "Computer" in the 2000's

#Creating a function that filters the dataset for certain Categories 
def categoryFilter(wordList, dataFrame):
  #This lowercases all words in wordList and the Category
  filtered_df = dataFrame.loc[dataFrame["Category"].apply(lambda x: all(word.lower() in x.lower() for word in wordList))]
  return filtered_df

literature = categoryFilter(["Literature"], jeopardy)
#print(tabulate(literature["Category"]))

#Creating a function that counts how many Rounds are for the filtered dataframe
def roundTypes(dataFrame):
  return dataFrame["Round"].value_counts()

print(roundTypes(literature)) #Literature Category was in Double Jeopardy! 1054 times
                                                         #Jeopardy! 423 times
                                                         #Final Jeopardy! 82 times