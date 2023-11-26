from microbit import *
import display_text
import type
import speech

print("Starting...")
display_text.display_text("W2SUR")
speech.say("Welcome to sure Oh Es")
while 1==1:
    if button_a.was_pressed() or button_b.was_pressed():
        type.type()

