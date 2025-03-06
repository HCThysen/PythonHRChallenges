# You are a doctor sorting through medical insurance cost data for some patients.
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
# Let’s add additional data to these lists:
# Append a new individual, "Priscilla", to names.
# Append her insurance cost, 8320.0, to insurance_costs.
names.append("Pricialla")
insurance_costs.append(8320.0)

# Currently, the names and insurance_costs lists are separate, but we want each insurance cost to be paired with a name.
medical_records = list(zip(insurance_costs,names))
print(medical_records)

# Create a variable called num_medical_records that stores the length of medical_records. 
num_medical_records = len(medical_records)

# Print num_medical_records with the following message:
# There are {number of medical records} medical records. 
print("There are " + str(num_medical_records) + " medical records.")

# Select the first medical record in medical_records, and save it to a variable called first_medical_record.
first_medical_record = medical_records[0]
print("Here is the first medical record:")
print(first_medical_record)

# Sort medical_records so that the individuals with the lowest insurance costs appear at the start of the list.
medical_records.sort()
print("Here are the medical records sorted by insurance cost:" + str(medical_records))

# Let’s look at the three cheapest insurance costs in our medical records.
# Slice the medical_records list, and store the three cheapest insurance costs in a list called cheapest_three.
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

# Let’s look at the three most expensive insurance costs in our medical records. 
priciest_three = medical_records[-3:]
print("Here are the three mst expensive insurance costs in our medical records: " + str(priciest_three))

# Count the number of occurrences of “Paul” in the names list, and store the result in a variable called occurrences_paul.
occurances_paul = names.count("Paul")
print("There are " + str(occurances_paul) + " individuals with the name Paul in our medical records.")