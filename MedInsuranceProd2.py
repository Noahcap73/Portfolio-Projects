# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
    return estimated_cost

# Creating my own second function (Calculating insurance cost difference between any individual)
def calculate_insurance_difference(person1, name1, person2, name2):
     difference_cost = person1 - person2
     print("The difference in insurance cost between " + name1 + " AND "+  name2 + " is "+ str(difference_cost) + " dollars.")
     return difference_cost


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria")


# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, "Omar")

# Estimate my insurance cost
noah_insurance_cost = calculate_insurance_cost(21, 1, 23.2, 0, 0, "Noah" )

# Calculate difference between insruance costs
omar_maria_diff = calculate_insurance_difference(omar_insurance_cost, "Omar", maria_insurance_cost, "Maria")
omar_noah_diff = calculate_insurance_difference(omar_insurance_cost, "Omar", noah_insurance_cost, "Noah")
maria_noah_diff = calculate_insurance_difference(maria_insurance_cost, "Maria", noah_insurance_cost, "Noah" )