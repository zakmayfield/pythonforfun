# PIN and attempt tracker

# If user submits correct PIN first try the program should print "Correct! It only took you one single attempt!"

# The program should track the number of attempts it took to correctly input the PIN, and print "Correct! It took you {attempt_number} attempts" 

user_pin = "4321"
attempts = 1

while True:
    pin = input('PIN:')

    if attempts == 1 and pin == user_pin:
        print("Correct! It only took you one single attempt!")
        break

    if not pin == user_pin:
        print("Wrong")
        attempts += 1
    else:
        print(f"Correct! It took you {attempts} attempts")
        break

