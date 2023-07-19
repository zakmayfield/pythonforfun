# PIN validator

number_of_attempts = 4
user_pin = "1234"

def validate_pin(pin_input):
    if len(pin_input) < 4:
        print('Invalid PIN length.')
        return False

    return True

while number_of_attempts > 0:
    is_validated = validate_pin(user_pin)

    pin = input('Please enter your PIN:')

    if is_validated and pin == user_pin:
        print('Correct PIN')
        break
        
    number_of_attempts -= 1

    if number_of_attempts == 0:
        print("You've run out of attempts.")
        break

    print(f'Incorrect... you have {number_of_attempts} attempts left.')


# Repeat password validator

# Program should ask for a password, then ask for a password verify
# The program shuold verify the two password

# States: MATCH | NOT MATCH
# MATCH 'User account created!'
# NOT MATCH: 'They do not match!'

pw = input('Password:')

while True:
    repeat_pw = input('Repeat password:')

    if pw == repeat_pw:
        print('User account created!')
        break
    else:
        print('They do not match!')