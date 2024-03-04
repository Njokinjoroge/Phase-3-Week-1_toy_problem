import string
import random

def solution(n):
    # Calculate the number of times each letter should appear
    num_letters = n // 26 if n >= 26 else n
    remainder = n % 26 if n >= 26 else n

    # Generate the string of letters
    letters = list(string.ascii_lowercase)[:num_letters]
    if remainder > 0:
        letters += letters[:remainder]
        letters = letters[:n]
    elif num_letters == 26:
        # If N is a multiple of 26, use only 15 letters instead of 26
        letters = letters[:15]

    # Shuffle the letters to get a random combination
    random.shuffle(letters)

    return ''.join(letters)