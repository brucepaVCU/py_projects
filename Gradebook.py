last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "Calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

grades.append(100)
subjects.append("Computer Science")

#print(subjects)
#print(grades)
gradebook = list(zip(subjects, grades))
gradebook.append(("Visual arts", 93))
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)