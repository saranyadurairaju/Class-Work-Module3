# Create a Python list to store your grocery list
my_Grocery_List = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]

# Print the grocery list
print(my_Grocery_List)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list
my_Grocery_List[3]= "Almond Butter"
print(my_Grocery_List)

# Remove "Jelly" from grocery list and print out the updated list
my_Grocery_List.remove("Jelly")
print(my_Grocery_List)

# Add "Coffee" to grocery list and print the updated list
my_Grocery_List.append("Coffee")
print(my_Grocery_List)

my_Grocery_List[0], my_Grocery_List[1] = my_Grocery_List[1], my_Grocery_List[0]
print(my_Grocery_List)

number_list=[4,2,5,7,4,65,5,5,54,5,5,5,5,5]
print(number_list)
# number_list.remove(5)

# Remove all numbers from list which are divisible by 5
mod_list = [elem for elem in number_list if elem % 5 != 0]
print(mod_list)

#[4, 2, 5, 7, 4, 65, 5, 5, 54, 5, 5, 5, 5, 5]
#[4, 2, 7, 4, 54]

# Remove all numbers equal to 5
#mod_list = [elem for elem in number_list if elem != 5]
#print(mod_list)

#[4, 2, 5, 7, 4, 65, 5, 5, 54, 5, 5, 5, 5, 5]
#[4, 2, 7, 4, 65, 54]

#Removes elements from index 1 to 3
#del number_list[1:4]
#print(number_list)

#[4, 2, 5, 7, 4, 65, 5, 5, 54, 5, 5, 5, 5, 5]
#[4, 4, 65, 5, 5, 54, 5, 5, 5, 5, 5]

#del number_list[1],number_list[2]
#print(number_list)

#[4, 2, 5, 7, 4, 65, 5, 5, 54, 5, 5, 5, 5, 5]
#[4, 5, 4, 65, 5, 5, 54, 5, 5, 5, 5, 5]

#del number_list[1],number_list[1]
#print(number_list)

#[4, 2, 5, 7, 4, 65, 5, 5, 54, 5, 5, 5, 5, 5]
#[4, 7, 4, 65, 5, 5, 54, 5, 5, 5, 5, 5]