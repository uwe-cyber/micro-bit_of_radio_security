from microbit import *
import radio

# Initialize variables to store the three numbers
config_numbers=[0,0,0]
current_digit = -1
current_index = 0

radio.on()

# Function to update the display based on the current digit
def update_display():
    display.scroll(convert_to_integer(config_numbers))

def convert_to_integer(numbers):
    return int(''.join(map(str, numbers)))

def on_data_received():
    
    received_data = radio.receive()

    if received_data is not None:

        display.scroll(received_data)
        
        # HANDLE EMPTY DATA
        if received_data == "":
            pass  # Do nothing

while True:
    on_data_received()
    
    # Check if button A is pressed
    if button_a.was_pressed():
        # Increment the current digit
        current_digit = current_digit + 1
        if current_digit > 9:
            current_digit = 0
        display.show(current_digit)

    # Check if button B is pressed
    if button_b.was_pressed():
        config_numbers[current_index] = current_digit
        current_index += 1
        
        # Update the display
        update_display()

    # Check if both buttons A and B are pressed
    if pin_logo.is_touched():
        # Set the radio group using the three numbers
        radio.config(group=(convert_to_integer(config_numbers)))
        display.show("OK")
        sleep(1000)  # Display "OK" for 1 second

        update_display()