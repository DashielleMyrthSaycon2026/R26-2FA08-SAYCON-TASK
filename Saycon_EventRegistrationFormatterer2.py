from datetime import datetime
first_name = input("Enter your given name: ")
last_name = input("Enter your last name: ")
section_ = input("Section: ")
fav_sub = input("Favorite subject: ")
event_title = input("Event Title: ")
year_ = input("Year: ")
month_ = input("Month: ")
day_ = input("Day: ")

full_name = first_name + "" + last_name
date_string = f"{year_} {month_} {day_}"

print("Student Name:", first_name.capitalize(), last_name.capitalize())
print("Student Code:", first_name.upper(), last_name.upper())
print("Section:", section_.upper())
print("Student's Favorite Subject:", fav_sub.title())
print("Character Count:", len(full_name))   

