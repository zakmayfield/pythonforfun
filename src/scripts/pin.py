# PIN validator

number_of_attempts = 3
user_pin = "1234"

def validate_pin(user_pin):
    if len(user_pin) < 4:
        print('Invalid PIN length.')
        return False

    return True

while number_of_attempts > 0:
    is_validated = validate_pin(user_pin)

    pin = input('Please enter your PIN:')

    if is_validated and pin == user_pin:
        success = True
        break
        
    number_of_attempts -= 1

    if number_of_attempts == 0:
        success = False
        break

    print(f'Incorrect... you have {number_of_attempts} attempt(s) left.')

if success:
    print('Correct PIN entered!')
else:
    print('Too many attempts...')