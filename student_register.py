# request number of students from user
num_of_students = int(input("How many students are registering for the exam? "))

with open("reg_form.txt", "w") as file: # opens in write mode
    for student in range(num_of_students):
        student_id = input("Enter the student ID: ")
        student_id = student_id + " ................" # add dotted line to the student id where student will sign
        file.write(student_id + "\n") # "\n" each string appears on a separate line