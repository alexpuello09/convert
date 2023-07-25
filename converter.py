import re
user_input = input("\n\tEnter a temperature in the format 30°F or 30°C: ")
celsius = 0
fahrenheit =  0

pattern = re.compile(r'^([-+]?\d+)\.?(\d+)?([CF])$',re.IGNORECASE) 
validation_input = user_input
result = re.match(pattern,validation_input)

if result:
    if result.group(3) == "C" or result.group(3) == "c":
        if result.group(2):
            celsius = float(result.group(1) +"."+ result.group(2))
            fahrenheit = (celsius * (9/5) + 32)

        else:
            celsius = int(result.group(1))
            fahrenheit = (celsius * (9/5) + 32)
        print(f" \nYour temperature in Fahrenheit is {fahrenheit:.2f}°F\n")

    else:
        if result.group(2):                 
            fahrenhiet = float(result.group(1) +"."+ result.group(2))
            celsius = 5/9 * (fahrenheit - 32)
            
        else:       
            fahrenheit = int(result.group(1))
            celsius = 5/9 * (fahrenheit - 32)

        print(f" \nYour temperature in celsius is {celsius:.2f}°C\n")
else:
    print("\nInvalid input. Please enter a number")