def display(input):
    which_letter = 0
    for letter in input:
        output = ""
        if letter.upper() in chars:
            print(chars.index(letter.upper()))
            output = output + format(int(chars.index(letter.upper())), "b")
        print(output)
        which_bit = 0
        for bit in output:
            if bit == "1":
                led.plot(which_bit, which_letter)
                which_bit+=1
                which_letter+=1
def declare():
    global chars
    chars = [" ",
        "1",
        "2",
        "3"
        "4",
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

print("Starting...")
declare()
display("w2sur")
