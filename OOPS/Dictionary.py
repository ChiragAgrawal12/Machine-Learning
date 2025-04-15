my_dict = {
    "name": "Chirag",
    "age": 22,
    "state": "Jharkhand",
    "city": "Chaibasa"
}
my_dict['id'] = 2
my_dict.update({"state": "USA", "profession": "Engineer"})

print(my_dict)

my_dict2 = dict(name="Muskan", age=19, state="Rajasthan", city="Jaipur")
print(my_dict2)
# Using parentheses
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
my_list = ["Aadi", "Mussu", "Chiru", "Mahak"]
print(type(my_list))
x = 10
y = 20
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
x += 3
print(x)
a = 0
b = 1
print(a & b)
print(a | b)
print(a & a ^ b & b)
print(x is not y)
print(1 not in my_list)
if (x < y):
    print(a)
elif (x == y):
    print(b)
else:
    print(b)
if (x % 2 == 0):
    print("even")
else:
    print("odd")

d = 75
if (d >= 75):
    print("D")
elif (d <= 33):
    print("F")
else:
    print("P")
for i in range(10):
    print(i)
for n in my_tuple:
    print(n)
for n in my_dict.values():
    print(n)
for n in my_dict:
    print(n)


for n in my_tuple:
    if n == 5:
        print(f"Found {n}! Stopping the loop.")
        break
    print(f"Current number: {n}")

print("Loop ended.")

