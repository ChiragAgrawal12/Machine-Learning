def even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

num = int(input("Enter a number: "))

print(even_odd(num))