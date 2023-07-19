# PIN validator debugging with print()

number_of_attempts = 3
user_pin = "1234"

def validate_pin(user_pin):
    print('validator:user_pin', user_pin)
    print('validator:conditional', len(user_pin) < 4)
    if len(user_pin) < 4:
        print('Invalid PIN length.')
        return False

    return True

while number_of_attempts > 0:
    print('-----begin while loop-----')

    is_validated = validate_pin(user_pin)
    print('loop:is_validated', is_validated)

    pin = input('Please enter your PIN:')

    print('loop:conditional1', is_validated and pin == user_pin)
    if is_validated and pin == user_pin:
        success = True
        break
        
    number_of_attempts -= 1

    print('loop:conditional2', number_of_attempts == 0)
    if number_of_attempts == 0:
        success = False
        break

    print(f'Incorrect... you have {number_of_attempts} attempt(s) left.')

if success:
    print('Correct PIN entered!')
else:
    print('Too many attempts...')