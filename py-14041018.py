n = int(input("Enter number of lessons:"))
lesson_names = []
lesson_grades = []
lesson_units = []

sum_grade_unit = 0

for i in range(n):
    name = input("Enter lesson name:")
    grade = float(input("Enter lesson grade:"))
    unit = int(input("Enter lesson unit:"))
    lesson_names.append(name)
    lesson_grades.append(grade)
    lesson_units.append(unit)
    sum_grade_unit += grade * unit

avg = sum_grade_unit / sum(lesson_units)
row_col = "#"
name_col = "Name"
print("#\t", "Name\t", "Unit\t", "Grade")
print("-"*50)
for i in range(len(lesson_names)):
    print(i+1,"\t", lesson_names[i],"\t", lesson_units[i],"\t", lesson_grades[i])
print("-"*50)
print("Avg:", round(avg,2))

# x = "Hello"
# y = 15.245258486
# z = 1500000000
# print(f"{x:-^10} {y:^20.2f} {z:,}")