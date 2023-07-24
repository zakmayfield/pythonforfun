
from typing import List, Dict

# Working with Numbers

# Program
# ✅ Should ask for interger numbers. Program will exit on 0.
# ✅ Should print the count how many numbers were entered, not including 0.
# ✅ Should print the sum of all valid numbers entered
# ✅ Should print the mean of all valid numbers entered
# ✅ Should print the count of negative vs positive numbers 

def calculate_len(nums: List[int]) -> int:
    return len(nums)


def calculate_sum(nums: List[int]) -> int:
    sum = 0
    for num in nums:
        sum += num
    return sum


def calculate_mean(nums: List[int]) -> int:
    sum = calculate_sum(nums)
    mean = sum / len(nums)
    return mean


def calculate_polarity(nums: List[int]) -> Dict[str, int]:
    negative = 0
    positive = 0
    for num in nums:
        if num < 0:
            negative += 1
        else:
            positive += 1
    return {
        "negative": negative,
        "positive": positive
    }


numbers = list()

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    try:
      user_input = int(input('Number:'))
    except:
        print("Invalid input. Please enter an integer")
        continue

    if user_input == 0:
        length = calculate_len(numbers)
        sum = calculate_sum(numbers)
        mean = calculate_mean(numbers)
        polarity = calculate_polarity(numbers)
        print(f"Numbers typed in {len(numbers)}")
        print(f"The sum of the numbers is {sum}")
        print(f"The mean of the numbers is {mean}")
        print("Positive numbers ", polarity["positive"])
        print("Negative numbers ", polarity["negative"])
        break
    numbers.append(user_input)

print(numbers)