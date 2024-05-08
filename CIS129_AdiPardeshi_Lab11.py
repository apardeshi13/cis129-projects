# Define Function 9.1
def writing_grades():
    # Print message to explain how to exit loop
    print('Enter grades(To exit enter -1)')
    # Open file grades.txt in write mode assigned to 'file'
    file = open("grades.txt", 'w')
    # Create a loop till -1 is entered
    while True:
        # Take imput for grades
        grades = int(input())
        # Check for -1
        if grades == -1:
            # If -1, then break loop
            break
        # Enter the grade entered to the file 'grades.txt' is -1 not entered
        else:
            file.writelines(f'{grades}\n')
    # Close the file when loop is broken
    file.close()

    return

# Define 9.2
def count_average():
    # Create grades
    grades = None
    # Open 'grades.txt' in read mode as file
    file = open('grades.txt', 'r')
    # Read all the lines from the file opened
    grades = file.readlines()
    # Create variable total with value of 0
    total = 0
    # Create a loop for the grades in file
    for grade in grades:
        # Iterate over each line of grade and remove whitespace then print
        grade = int(grade.strip())
        print(grade)
        # Add the grade to total
        total += grade
    # Print total
    # Print the count which is length of grades lines
    # Calculate and print average with 2 digits decimal rounded
    print(f"total: {total}")
    print(f"count: {len(grades)}")
    print(f"average: {total/len(grades) : .2f}")

    return
# Import csv module to read and write in csv
import csv
# Define 9.3
def csv_store():
    # Variable n to store input "number of students"
    n = int(input("Number of Students: "))
    # Create list 'rows' to store first name, last name and 3 exam grades
    rows = [["First Name", "Last Name", "Exam I Grade", "Exam 2 Grade", "Exam 3 Grade"]]
    # Iterate over for each number of student and take input for each
    for i in range(n):
        # For each times it itereates, store the inputs in the variables
        firstname = input("\n Enter Student's First Name: "+str(i+1)+": ")
        lastname = input("Enter Student's Last Name " + str(i + 1) + ": ")
        exam1grade = int(input("Enter exam 1 grade for student "+str(i+1)+": "))
        exam2grade = int(input("Enter exam 2 grade for student "+str(i+1)+": "))
        exam3grade = int(input("Enter exam 3 grade for student "+str(i+1)+": "))
        # After the variables have values stored, append it to the list 'rows'
        rows.append([firstname, lastname, exam1grade, exam2grade, exam3grade])
    # Create/open grades.csv in write mode to edit
    # use newline to handle new lines correctly
    file = open("grades.csv", 'w', newline = '')
    file = csv.writer(file)
    # iterate over each item in the list made earlier
    # then write the item in each row with writerow(i)
    for i in rows:
        file.writerow(i)
    # Print a completion message
    print("\n Complete.")

    return