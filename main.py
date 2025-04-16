# if 條件判斷
age =18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# for 迴圈
for i in range(5):
    print(f"Number {i}")

# 函式定義
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))

# 串列（list）
fruit = ["apple","banana","cherry"]
print(fruit[0])
fruit.append("orange")
print(fruit)

# 字典（dict）
person = {"name": "John", "age": 30}
print(person["name"])

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)