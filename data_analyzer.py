import sys
from utils import greet_user, calculate_sum

#variables
name = "Pasindu"
age = 25
scores = [85, 90, 78, 92]
person = {"name": "Pasindu", "age": 25, "city": "Colombo"}

#Tuple
grades = (85, 90, 78, 92)

#string to int casting
age_str = "25"
age_int = int(age_str)

#built in functions: enumerate, range, id
print("Enumerate scores:")
for index, score in enumerate(scores):
    print(f"Index: {index}, Score: {score}")

print("\nUsing range:")
for i in range(5):
    print(f"Range value: {i}")

print(f"\nID of name variable: {id(name)}")

#conditional statements
if age >= 30:
    print(f"{name} is a professional.")
elif 20 <= age < 30:
    print(f"{name} is a young professional.")
else:
    print(f"{name} is a student.")

#loops
count=0
while count < 3:
    print(f"Count is: {count}")
    count += 1

#imported functions
print(greet_user(name))
print(f"Sum of scores: {calculate_sum(scores)}")

#command line arguments handling
if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_arg = sys.argv[1]
        print(f"\nArgument received: {user_arg}")
    else:
        print("\nNo command line arguments provided.")