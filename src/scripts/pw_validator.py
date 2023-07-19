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