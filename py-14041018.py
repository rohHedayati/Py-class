# n = int(input("Enter number of lessons:"))
# lesson_names = []
# lesson_grades = []
# lesson_units = []

# sum_grade_unit = 0

# for i in range(n):
#     name = input("Enter lesson name:")
#     grade = float(input("Enter lesson grade:"))
#     unit = int(input("Enter lesson unit:"))
#     lesson_names.append(name)
#     lesson_grades.append(grade)
#     lesson_units.append(unit)
#     sum_grade_unit += grade * unit

# avg = sum_grade_unit / sum(lesson_units)
# row_col = "#"
# name_col = "Name"
# unit_col = "Unit"
# grade_col = "Grade"
# print(f"{row_col:5}{name_col:^25}{unit_col:^10}{grade_col:^10}")
# print("-"*50)
# for i in range(len(lesson_names)):
#     print(f"{i+1:<5}{lesson_names[i]:^25}{lesson_units[i]:^10}{lesson_grades[i]:^10.2f}")
# print("-"*50)
# print("Avg:", round(avg,2))

# # x = "Hello"
# # y = 15.245258486
# # z = 1500000000
# # print(f"{x:-^10} {y:^20.2f} {z:,}")
# -----------------------------------------


# Find item index
# number_list = [10,15,20,3,14,16,20,14,5,15]
# x = 10
# print(number_list.count(x))
# print(number_list.index(x))
# index_list = []
# for i, item in enumerate(number_list):
#     if x == item:
#         index_list.append(i)
# print(index_list)

# -----------------------------------------
# Sort List
# number_list = [10,15,20,3,14,16,20,14,5,15]
# number_list.sort(reverse=True)
# x = sorted(number_list)
# print(number_list)
# print(x)

# --------------------------------------------
# Tuple -> (1,2,3,4,5)
# my_tuple = (10,20,15,61,20)
# my_tuple[1] = 1000
# print(my_tuple[1])

# --------------------------------------------
# Set -> {10,25,16,18,70}
# my_set1 = {10,25,16,18,70}
# my_set2 = {100,25,116,18,70}
# print(my_set1.union(my_set2))
# print(my_set1.intersection(my_set2))
# print(my_set1.difference(my_set2))

# print(my_set1)
# -----------------------------------------
# unique_numbers = []
# number_list = [10,15,20,3,14,16,20,14,5,15]
# 1
# print(list(set(number_list)))

# 2
# for x in number_list:
#     if x not in unique_numbers:
#         unique_numbers.append(x)
# print(unique_numbers)
# -----------------------------------------
# Dictionary -> key: value
x = 33
info = {
    "fname": "Roullah",
    "lname": "Hedayati",
    "age": x   
}
# print(info["lname"])
# for x,y in info.items():
#     print(x,y)

