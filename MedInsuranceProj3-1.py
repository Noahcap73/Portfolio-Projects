# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else: 
    print("Smoking is not an issue for you.")

def analyze_children(children_count):
  if children_count >= 3:
    print("To maintain your cost, you should consider not having more children.")
  if children_count <= 2: 
    print("If you want more children, your cost will increase.")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_children(num_of_children)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

#Estimate my own insurance cost
noah_insurance_cost = estimate_insurance_cost("Noah", 21, 1, 0, 0)