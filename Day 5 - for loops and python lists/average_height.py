total_of_student_heights = 0
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):

    total_of_student_heights = total_of_student_heights + int(student_heights[n])
    
    total_students = n + 1

print(round(total_of_student_heights / total_students))