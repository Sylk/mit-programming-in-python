def is_palindrome(characters):
    fixed_string = characters.lower()

    if len(fixed_string) <= 1:
        return False

    if fixed_string == fixed_string[::-1]:
        return True
    else:
        return False


print is_palindrome('Racecar')
