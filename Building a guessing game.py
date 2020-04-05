secret_word = "giraffe"

while(True):
    guess = input('Insert the secret word: ')
    if secret_word == guess:
        break

print('Congratulations! You entered the secret word!')