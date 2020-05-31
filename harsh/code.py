# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class=class_1+class_2

# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}


# Slice the dict and stores  the all subjects marks in variable
marks=courses.values()

# Store the all the subject in one variable `Total`
Total=sum(marks)

# Print the total
print("the total marks is ",Total)
# Insert percentage formula
percentage=(Total/500)*100
# Print the percentage
print("the percentage of Geoffrey Hinton is ",percentage,"%")




# Create the Dictionary
 
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50}

topper=max(mathematics,key=mathematics.get)
print("the topper in mathematic is ",topper)


# Given string


# Create variable first_name 
first_name=topper.split()[0]

# Create variable Last_name and store last two element in the list
Last_name=topper.split()[1]
# Concatenate the string
full_name=Last_name+' '+first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print('the certificate name is ',certificate_name)
# Code ends here


