# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250*age - 128 *sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person´s insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age += 4
new_insurance_cost = 250*age - 128 *sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + "dollars.")
age = 28

# BMI Factor
bmi += 3.1
new_insurance_cost = 250*age - 128 *sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + "dollars.")
bmi = 26.2

# Male vs. Female Factor
sex =1
new_insurance_cost = 250*age - 128 *sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + "dollars.")
sex = 0

# Extra Practice
num_of_children += 1
new_insurance_cost = 250*age - 128 *sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance from having another child is " + str(change_in_insurance_cost) + "dollars.")

num_of_children = 3

smoker =1
new_insurance_cost = 250*age - 128 *sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being smoker instead of non-smoker is " + str(change_in_insurance_cost) + "dollars.")