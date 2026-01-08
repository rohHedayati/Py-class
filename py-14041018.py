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
unit_col = "Unit"
grade_col = "Grade"
print(f"{row_col:5}{name_col:^25}{unit_col:^10}{grade_col:^10}")
print("-"*50)
for i in range(len(lesson_names)):
    print(f"{i+1:<5}{lesson_names[i]:^25}{lesson_units[i]:^10}{lesson_grades[i]:^10.2f}")
print("-"*50)
print("Avg:", round(avg,2))

# x = "Hello"
# y = 15.245258486
# z = 1500000000
# print(f"{x:-^10} {y:^20.2f} {z:,}")