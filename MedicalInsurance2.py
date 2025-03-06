# In this project, you will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
#Create a list called names and fill it with the names of the individuals you are estimating insurance costs for:
# "Maria"
# "Rohan"
# "Valentina"
names = ["Maria", "Rohan", "Valentina"]

# Next, create a list called insurance_costs and fill it with the actual amounts that Maria, Rohan, and Valentina paid for insurance:
# 4150.0
# 5320.0
# 35210.0
insurance_costs = [4150.0, 5320.0, 35210.0]

# Create a new variable called insurance_data that combines names and insurance_costs using the zip() function.
# Print this new variable.
insurance_data = list(zip(names, insurance_costs))
print(insurance_data)

# Next, create an empty list called estimated_insurance_data. 
estimated_insurance_data = []

# Use .append() to add ("Maria", maria_insurance_cost) to estimated_insurance_data. Do the same for Rohan and Valentina. 
estimated_insurance_data.append(["Maria", maria_insurance_cost])
estimated_insurance_data.append(["Rohan", rohan_insurance_cost])
estimated_insurance_data.append(["Valentina", valentina_insurance_cost])

# Print estimated_insurance_data. 
print(estimated_insurance_data)

# In the output, you should see two lists. The first one represents the actual insurance cost data and the second one represents the estimated insurance cost data. 
# However, it’s difficult to know this just by looking at the output. As a data scientist, you want to make sure that your data is clean and easy to understand.
# Add to the print statement for insurance_data so that it’s clear what the list contains. The output of the print statement should look like:
print("Here is the actual insurance cost data:" + str(insurance_data))

# Do the same for the print statement that prints estimated_insurance_data. 
print("Here is the estimated insurance cost data:" + str(estimated_insurance_data))
