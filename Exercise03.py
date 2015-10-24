# Purpose: create a function to

def convert(pounds) :
    kg = pounds * 0.453592
    return kg

# Weight in pounds
weight = 34
# Weight in kg
new_weight = convert(weight)

# Print weight in pounds and kg
print(str(weight) + " pounds is " + str(new_weight) + " kg")
