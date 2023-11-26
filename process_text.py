import display_text

def process(binary_text):

    print("Processing text")
    chars_counter = len(binary_text)
    print(binary_text)
    actual_text = ""
    while chars_counter >= 5:
        # Extract the current section
        char = binary_text[:5]
        
        # Print or do something with the current section
        print(char)
        
        # Update the starting index for the next iteration
        binary_text = binary_text[5:]

        print(int(char, 2))
        actual_text = actual_text + display_text.chars[int(char, 2)]
        print(actual_text)
        
        # Decrease the character counter
        chars_counter -= 5
    print("input was: ", actual_text)