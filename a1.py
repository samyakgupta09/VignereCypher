#----------------------------------------------------
# Assignment1 1: Vignère cipher
# Purpose of program: decrypt files with unknown keys
#
# Author: Samyak Gupta
# Collaborators/references: CMPUT 175 team(encrypt function), stack overflow(splitting text by nth character)
#----------------------------------------------------

from math import log2

def get_ALPHABET():
    """
    get_ALPHABET() - returns the extended alphabets provided to us
    returns - ALPHABET(str) - extended alphabets as a string
    """
    ALPHABET = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ALPHABET

def encrypt(text, key):
    """
    encrypt(text, key) - takes a ciphertext (encrypted text) and a short key,
    and deciphers it using vigenere's cipher
    text - Some text as a str. All characters must be in ALPHABET
    key - Some text as a str. All characters must be in ALPHABET
    returns - encrypted(str) - encrypted text from given text and key
    """
    ALPHABET = get_ALPHABET()
    encrypted = ""
    
    # iterates over text and changes each char
    for position in range(len(text)):
        text_character = ALPHABET.index(text[position])
        key_character = ALPHABET.index(key[position % len(key)])
        encrypted_char = (text_character + key_character) % len(ALPHABET)
        encrypted += ALPHABET[encrypted_char]
    return encrypted

def decrypt(text, key):
    """
    encrypt(text, key) - takes a ciphertext (encrypted text) and a short key,
    and deciphers it using vigenere's cipher
    text - Some text as a str. All characters must be in ALPHABET
    key - Some text as a str. All characters must be in ALPHABET
    returns - decrypted(str) - decrypted text from given text and key
    """
    ALPHABET = get_ALPHABET()
    decrypted = ""
    
    # iterates over text and changes each char
    for position in range(len(text)):
        text_character = ALPHABET.index(text[position])
        key_character = ALPHABET.index(key[position % len(key)])
        decrypted_char = (text_character - key_character)%len(ALPHABET)
        decrypted += ALPHABET[decrypted_char]
    return decrypted

def get_frequencies(text):
    """
    get_frequencies(text) - takes a text and returns the relative frequencies 
    of each alphabet in the text
    text - some text as a str. All characters must be in ALPHABET
    returns - freq(dict) - dictionary for relative frequency of each letter in given text
    """
    # iterates over each character and increments frequencies
    freq = {}
    for char in text:
        if char not in freq.keys():
            freq[char] = 1
        else:
            freq[char] += 1
    for key in freq.keys():
        freq[key] /= len(text)
    return freq
            
def cross_entropy(freq1,freq2):
    """
    cross_entropy(float) - takes two letter frequency dictionaries and returns the
    cross entropy
    freq1 - some frequency distribution of letters as a dict
    freq2 - some frequency distribution of letters as a dict
    returns - total(float) - cross_entropy of given two frquencies
    """
    
    # makes a list of common characters
    common_chars = []
    for value in freq1.keys():
        common_chars.append(value)
    for value in freq2.keys():
        if value not in common_chars:
            common_chars.append(value)
            
    # calculates total
    total = 0.0
    min_freq1 = min(freq1.values())
    min_freq2 = min(freq2.values())
    for char in common_chars:
        if char in freq1.keys() and char not in freq2.keys():
            total -= freq1[char]*log2(min_freq2)
        elif char in freq2.keys() and char not in freq1.keys():
            total -= min_freq1*log2(freq2[char])
        else:
            total -= freq1[char]*log2(freq2[char])
    return total

def get_english_freq():
    """
    get_english_freq() - returns the frequency dict by reading frank.txt
    returns - english_freq(dict) - frequency dict of frank.txt
    files used = frank.txt
    """
    
    # opens file and reads its contents
    with open('frank.txt','r') as file:
        english_text = file.read()
        
    english_freq = get_frequencies(english_text)
    return english_freq

def guess_key(encrypted):
    """
    guess_key(encrypted) - guesses the key of the given encrypted text usinng frequency analysis
    encrypted - some encypted text as str.
    returns key(str) - guessed key 
    """
    ALPHABET = get_ALPHABET()
    N_KEY = 3
    # splits the text according to which letter is encrypted by which key 
    split_encrypted = [encrypted[index:index+N_KEY] for index in range(0,len(encrypted),N_KEY)]     # splits text by every nth chracter, here n is the number of keys
    key_encrypted = {}
    for key_num in range(N_KEY):
        key_encrypted['key%d_encrypted'%key_num] = []
    for word in split_encrypted:
        for key_num in range(len(word)):
            key_encrypted['key%d_encrypted'%key_num].append(word[key_num])
    
    # creates a list of each key and calculates cross entropy for each letter in alphabet
    cross_entropy_keys = {}
    for key_num in range(N_KEY):
        cross_entropy_keys['cross_entropy_key%d'%key_num] = []
    for index in range(len(ALPHABET)):
        for key_num in range(N_KEY):
            cross_entropy_keys['cross_entropy_key%d'%key_num].append(cross_entropy(get_english_freq(), get_frequencies(decrypt(''.join(key_encrypted['key%d_encrypted'%key_num]),ALPHABET[index]))))
    
    # forms key by finding the minimum entropy for each alphabet 
    key = ''
    for key_num in range(N_KEY):
        key += ALPHABET[cross_entropy_keys['cross_entropy_key%d'%key_num].index(min(cross_entropy_keys['cross_entropy_key%d'%key_num]))]
        
    return key

def crack(encrypted_text):
    """
    crack(encrypted_text) - decrypts the encrypted_text by guessing it's key and using decrypt function
    encrytped_text - some encrypted text as str to decrypt
    returns - decrypted(str) - decrypted text from given text
    """
    
    # guesses key and decrypts the given text
    key = guess_key(encrypted_text)
    decrypted = decrypt(encrypted_text, key)
    return decrypted

def get_encrypted_text(file_name):
    """
    get_encrypted_text(file_name) - returns content of given file_name
    file_name - some file name as str.
    returns - encrypted_text(str) - encrypted text in given file
    files used - file_name
    """
    
    # opens and reads given file name
    with open(file_name,'r') as file:
        encrypted_text = file.read()

    return encrypted_text

def main():
    """
    main() - controls the main flow of the program
    """
    file_name = input('Enter file name to decrypt: ')
    encrypted_text = get_encrypted_text(file_name)
    print(crack(encrypted_text))
    
if __name__=="__main__":
    main()