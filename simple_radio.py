from microbit import *
import radio

# Radio configuration
radio.config(group=157)
radio.on()

# Handle all potential data incoming from the radio
def on_data_received():
    
    received_data = radio.receive()

    if received_data is not None:

        display.scroll(received_data)
        
        # HANDLE EMPTY DATA
        if received_data == "":
            pass  # Do nothing

       
    
# Main function
def main():

    # Handle pairing procedure
    # Clears buffer
    radio.send("")

    messages = ["Hello", "Goodbye", "How are you?", "Shhh! it's secret"]
    current_message_index = 0
   

    # Main loop
    while True:
        on_data_received()

        message_sent = False

        if button_a.is_pressed():
            display.scroll(messages[current_message_index], wait=False)
            sleep(500)  # Adjust as needed

            while not message_sent:
                if button_a.is_pressed():
                    current_message_index = (current_message_index + 1) % len(messages)
                    display.scroll(messages[current_message_index], wait=False)
                    sleep(500)  # Adjust as needed
    
                if button_b.is_pressed():
                    display.clear()
                    selected_message = messages[current_message_index]
                    radio.send(selected_message)
                    message_sent = True

    
                
# Call the main function if the script is run directly
if __name__ == "__main__":
    main()