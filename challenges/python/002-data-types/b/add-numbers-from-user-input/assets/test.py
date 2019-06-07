import answer
from random import randint

a = randint(-100,100)
b = randint(-100,100)
print(f'Add {a} and {b}')

assert answer.add_user_input() == a + b
print('Well done! All tests passed')