def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter == 'a' or letter == 'e'or letter == 'i' or letter == 'o' or letter == 'u':
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate('omar'))