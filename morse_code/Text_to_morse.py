import json
from pprint import pprint as pp
import re


def covert_morse_code(dict,key):
    """ 
        Convert the Value the given user 

    Args:
        dict: Dictionary from is Value will be coverted
        key: the key we want to obtain
    """        
    if key in dict.keys():
        return dict[key]
    else:
        return f"{key}" 


def get_code(text):
    """ 
        Get the text from user and all the dict that are in json file

    Args:
        text: Text that we want to convert to the morse code
    """        
    with open("morse.json", "r") as morse_file:
        data = json.load(morse_file)
        alphabet = (data["alphabet"][0])
        numbers = (data["numbers"][0])
        characters = (data["Characters"][0])
        big_alphabet = {v[1]:k for (k,v) in alphabet.items()}
        small_alphabet = {v[0]:k for (k,v) in alphabet.items()}
        numbers_key1 = {v[0]:k for (k,v) in numbers.items()}
        characters_key  = {v[0]:k for (k,v) in characters.items()}
        all_characters = list(text)
        string = ''
        for i in all_characters:
            if re.match(r'[A-Z]',i) is not None:
                str1 =covert_morse_code(big_alphabet,i)
            elif re.match(r'[a-z]',i) is not None:
                str1= covert_morse_code(small_alphabet,i)
            elif re.match(r'[0-9]',i) is not None:
                str1=covert_morse_code(numbers_key1,i)
            elif re.match(r'[A-Za-z0-9]',i) is None:
                str1=covert_morse_code(characters_key,i)
            string = string + str1
        return string


def get_text():
    text = input("Please enter the text You Want to convert into Morse code: ")
    print(get_code(text))


def  main():
    get_text()


if __name__ == "__main__":
    main()
