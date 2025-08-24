# Dictionary for grades
grades = {
    "1": 4.0, "A+": 4.0,
    "2": 4.0, "A": 4.0,
    "3": 3.7, "A-": 3.7,
    "4": 3.3, "B+": 3.3,
    "5": 3.0, "B": 3.0,
    "6": 2.7, "B-": 2.7
}

GPA = 0
subject = int(input("Enter your number of subjects (max 6): "))

if subject > 6:
    print("You cannot enter more than 6 subjects!")
    subject = 0

x = 0
sumhours = 0
subjects_data = []  # to store grades & hours

while subject > 0:
    user = input(f"Enter grade for subject {x+1} (1- 'A+'  2- 'A'  3- 'A-'  4- 'B+'  5- 'B'  6- 'B-'): ")
    
    if user in grades:
        grade_value = grades[user]
    else:
        print("Invalid grade! Try again.")
        continue 
    
    try:
        hours = int(input(f"Enter credit hours for subject {x+1} (1, 2, or 3): "))
        if hours not in [1, 2, 3]:
            print("Invalid hours! Must be 1, 2, or 3.")
            continue
    except ValueError:
        print("Invalid input! Hours must be a number.")
        continue
    
    GPA += (grade_value * hours) #Calc GPA
    sumhours += hours
    subjects_data.append((user, grade_value, hours))
    
    x += 1
    subject -= 1

if sumhours > 0:
    GPA = GPA / sumhours
    GPA_20 = GPA * 5 
    
    print("\n--- Results ---")
    for idx, (g, val, h) in enumerate(subjects_data, start=1):
        print(f"Subject {idx}: Grade = {g} ({val}), Hours = {h}")
    print(f"\nFinal GPA (out of 4): {round(GPA, 2)}")
    print(f"Final GPA (out of 20): {round(GPA_20, 2)}")
else:
    print("No valid subjects entered.")
