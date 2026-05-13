# 1) Create variables to store different types of values:
#    - `name` as text (string)
name = "Emaan"
#    - `age` as a whole number (integer)
age = 13
#    - `is_student` as True/False (boolean)
is_student = True
#    - `weight` as a decimal number (float)
weight = 38.5
# 2) Print each variable’s value.
print("name:",name,type(name))
print("age:",age,type(age))
print("is_student",is_student,type(is_student))
print("weight",weight,type(weight))
# 3) Print the datatype of each variable using `type()`.
# 4) Show a message that type casting will happen next.
print("after typecasting...")
# 5) Convert `age` from an integer to a string and store it back in `age`.
age = str(age)
print("age:",age,type(age))
# 6) Print `age` and print its datatype again to confirm it changed.
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
weight = int(weight)
print("weight",weight,type(weight))
# 8) Print `weight` and print its datatype again to confirm it changed.