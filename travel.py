# Create a function called trip_planner_welcome() that takes one parameter called name. The function should use print() to output a message like this: 
# Welcome to tripplanner v1.0 <Name Here>
def trip_planner_welcome(name):
  print('Welcome to tripplanner v1.0 ' + name)

# Call trip_planner_welcome(), passing your name as an argument.
trip_planner_welcome('Heidi')

# Next, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our user’s trip.
# Define the function estimated_time_rounded() with a single parameter estimated_time. The function should do two things:
# 1. Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time.
# 2. Return rounded_time.
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

# After the function definition, call estimated_time_rounded() with a decimal argument and save the result to a variable called estimate.
estimate = estimated_time_rounded(3.4)

# Create a function called destination_setup() that will have four parameters in this exact order:
# 1. origin
# 2. destination
# 3. estimated_time
# 4. mode_of_transport
# Give the parameter mode_of_transport a default value of "Car"
# we are going to write four print() statements in our function. The output on this function call should look like this: 
# Your trip starts off in <origin>
# And you are traveling to <destination>
# You will be traveling by <mode_of_transport>
# It will take approximately <estimated_time> hours
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Aarhus", "Copenhagen", estimate)