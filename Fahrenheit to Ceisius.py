    # This code has been developed as a means of practicing. Feel free to do whatever you want with it. 
    # Its purpose is to take a Fahrenheit value from user and convert it to Celsius. Nothing complicated, 
    # You can find a converter simply just by searching in google. 

import math

while True:
    data = input("Write the degree in Fahrenheit: ")

    try: # Validating user input
        fah = float(data)  # Try to convert the input to a float

        def converter(fah):
            celsius = (fah - 32) / 1.8
            return celsius

        result = converter(fah)  # Call the function on the given Fahrenheit and save the result in 'result'

        if result < 0:
            result = math.ceil(result)  # If the degree is negative, round it towards 0.
        else:  # Round up the degree if the decimal point is >= 0.5, round it down if < 0.5
            decimalPoint = result - int(result)  # Take out the integer part of the number, leaving only the decimal point
            if decimalPoint >= 0.5:
                result = math.ceil(result)
            else:
                result = math.floor(result)

        answer = f'{fah} Fahrenheit equals to {result} Celsius. We have rounded the number for the purpose of ease of reading.'
        print(answer)

    except ValueError:
        print('Input is not valid. Please only insert numeric values.')

    UserChoice = input("Would you like to continue? (y/n): ") # Asking if user wants to quit or continue

    if UserChoice.lower() == 'n':
        print("Thanks for using the converter. closing the program")
        break
    elif UserChoice.lower() == 'y':
        pass
    else: # Exiting the program if user tries to be funny or just testing the program's felxibility 
        print('input was neither y or n. closing the program')
        exit()