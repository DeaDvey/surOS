from microbit import *

def display_text(text):
	global chars
	which_letter = 0
	for letter in text:
		print(letter)
		output = ""
		if letter.upper() in chars:
			print(chars.index(letter.upper()))
		    output = output + bin(chars.index(letter.upper()))[2:]
            while len(output) < 5:
                output = '0' + output
			print(output)

		which_bit = 0
		for bit in output:
			if bit == "1":
				print(which_bit, which_letter, 9)
			which_bit+=1
		which_letter+=1

chars = [" ",
    "1",
    "2",
    "3",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "R",
    "S",
    "T",
    "U",
    "W",
    "Y",
    "/",
    "~"]
