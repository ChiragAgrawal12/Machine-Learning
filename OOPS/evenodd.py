def check_even_odd(numbers):
    return ["Even" if num % 2 == 0 else "Odd" for num in numbers]

num_list = list(map(int, input("Enter numbers separated by space: ").split()))

result = check_even_odd(num_list)
print("Results:", result)
