student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)

student_scores.sort(reverse = True)
highest_score = student_scores[0]

print("The highest score in the class is : " + str(highest_score))