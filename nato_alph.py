#!/usr/bin/python

import sys

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
  }


letters = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
  }


additional_letters = {
    " ": "space",
    "-": "dash",
    ".": "dot",
    ",": "comma",
    ":": "colon",
    ";": "semicolon",
    "@": "at"
  }

def convert_to_nato(phrase):
    res = ""
    for l in phrase:
        res = res + " " + convert_nato_letter(l)
    return res


def convert_nato_letter(letter):
    if letter.upper() in letters:
        return letters[letter.upper()].upper()
    elif letter in additional_letters:
        return additional_letters[letter]
    elif letter in numbers:
        return numbers[letter].upper()
    else:
        return letter

def main(argv):
    data = argv
    for phrase in data:
        print convert_to_nato(phrase)

if __name__ == "__main__":
    main(sys.argv[1:])

