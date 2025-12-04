'''
Docstring for Day10.exercises.Exercise02
Temperature Converter

Task:

Create a function convert_temperature(value, to_scale="C").

value is the temperature to convert.

to_scale is either "C" for Celsius or "F" for Fahrenheit (default "C").

The function should return the converted temperature.
'''
def convert_temperature(value, to_scale="C"):
    if to_scale.upper() == "F":
        return (value * 9/5) + 32
    elif to_scale.upper() == "C":
        return (value - 32) * 5/9
    else:
        return "Invalid Scale! Use 'C' or 'F'."
    
print(convert_temperature(100,"F"))
print(convert_temperature(50,"C"))