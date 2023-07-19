student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for names in student_scores:
    if student_scores[names] >= 91 and student_scores[names] <= 100:
        student_grades[names] = "Outstanding"
    elif student_scores[names] >= 81 and student_scores[names] <= 90:
        student_grades[names] = "Exceeds Expectations"
    elif student_scores[names] >= 71 and student_scores[names] <= 80:
        student_grades[names] = "Acceptable"
    else:
        student_grades[names] = "Fail"
    
# 🚨 Don't change the code below 👇
print(student_grades)
