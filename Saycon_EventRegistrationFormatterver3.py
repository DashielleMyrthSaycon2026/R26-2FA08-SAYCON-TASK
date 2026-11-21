from datetime import datetime
first_name = input("Enter your given name: ")
last_name = input("Enter your last name: ")
section_ = input("Section: ")
event_title = input("Event Title: ")
year_ = input("Year: ")
month_ = input("Month: ")
day_ = input("Day: ")

full_name = first_name + "" + last_name
date_string = f"{year_} {month_} {day_}"
event_date = datetime.strptime(date_string, "%Y %B %d")

print("Student Name:", first_name.capitalize(), last_name.capitalize())
print("Student Code:", first_name.upper(), last_name.upper())
print("Section:", section_.upper())
print("Event:", event_title.title())
print("Date:", event_date.strftime("%B %d, %Y"))
print("Weekday:", event_date.strftime("%A"))
print("Language Used: Python")
print("String Feature Used: capitalize(), upper(), title(), strptime(), strftime()")
print("Date/Time Feature Used: datetime")
print()
print("Registration record created successfully")
