from microbit import *
import process_text

def type():
    print("Typing")
    display.clear()
    enter_pressed = False
    position_x = 0
    position_y = 0
    binary_word = ""
    while enter_pressed == False:
        if button_a.was_pressed():
            display.set_pixel(position_x,position_y,9)
            position_x+=1
            binary_word = binary_word + "1"
            if position_x == 5:
                position_y+=1
                position_x = 0
            if position_y == 5:
                display.clear()
                position_x = 0
                position_y = 0
            print(position_x,position_y)
            
        if button_b.was_pressed():
            display.set_pixel(position_x,position_y,1)
            position_x+=1
            binary_word = binary_word + "0"
            if position_x == 5:
                position_y+=1
                position_x = 0
            if position_y == 5:
                display.clear()
                position_x = 0
                position_y = 0
            print(position_x,position_y)

        if binary_word[-5:] == "11111" and position_x == 0:
            enter_pressed = True
            process_text.process(binary_word)
            


    
        