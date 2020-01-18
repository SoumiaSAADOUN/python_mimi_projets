import random
import string
long = int(input(" How long you want your password to be ( min 6 characters) ? "))
numbers = int(input(" How many numbers you want in your password? "))
letters = int(input(" How many letters you want in your password? "))
if (numbers+letters<6):
    print('Password should be minimum 6 characters')
    exit()
else:
    generated_num = ''.join(random.choice(string.digits) for i in range(numbers))
    generated_let = ''.join(random.choice(string.ascii_letters) for j in range(letters))
    generated_pwd = random.sample(generated_let+generated_num, len(generated_let+generated_num))
    result = ''.join(generated_pwd)
    print('Your password is :', result)

