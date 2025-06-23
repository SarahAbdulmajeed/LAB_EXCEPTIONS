# Temperature Converter

def celsius_to_fahrenheit(celsius:float) -> float:
    fahrenheit:float = (celsius * 9/5) + 32
    return round(fahrenheit,2)

def fahrenheit_to_celsius(fahrenheit:float) -> float:
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,2)

def main():
    while True:
        try:
            user_input:str = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
            values:list = user_input.split()
            if len(values) != 2 : 
                raise ValueError("Invalid input, Please enter like '25 C' or '77 F'.")
            else:
                if values[1].upper() == "F":
                    result = fahrenheit_to_celsius(float(values[0]))
                    print(f"Temperature in Celsius: {result} C")
                    break
                elif values[1].upper() == "C":
                    result = celsius_to_fahrenheit(float(values[0]))
                    print(f"Temperature in Fahrenheit: {result} F")
                    break
                else:
                    raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except Exception as e:
            print(e)
    
main()

print("Thank you for using Temperature Converter")

