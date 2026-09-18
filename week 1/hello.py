#Activity 1
print("===================================")
print("Welcome here")
print("My first post!")
print("===================================")

#The program display exactly as written
#top to bottom
#Output shows in the terminal
#Activity 2
username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)

#The use of the variables is to assign value or str to them
#Yes the output changes when the value changes

#Activity 3
followers = 100

followers += 50
print("Day 1:", followers)

followers += 20
print("Day 2:", followers)

followers -= 10
print("Day 3:", followers)
#No we dont have to manually reassign the follower value
#Each operation affects the existing value of the followers
#+= is the plus and -= is the to minus

#Activity 4
username = input("Enter Username: ")
age = input("Enter Age: ")
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("==================")
print("Username:", username)
print("Age:", age)
print("Category:", category)

#Ask the user to input in the terminal
#the program is dynamics

#Activity 5
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("==================")
print("Username:", username)
print("Age:", age)
print("Category:", category)

if age>40 and category == "fun":
    print("You are old what is fun for you??")
#username is str, age is int, category is str
#if age>40 and category == "fun" print("You are old what is fun for you??") will happen
