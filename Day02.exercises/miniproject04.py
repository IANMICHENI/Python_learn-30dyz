#Ask the user for temperature in Celsius and convert it to Fahrenheit and Kelvin.
celsius = float(input("Enter Celsius:"))
fahrenheit = ( celsius * 9/5) + 273.15
kelvin = celsius + 273.15

print(f"celsius {celsius} = fahrenheit:{fahrenheit:.2f}f = Kelvin {kelvin:.2f}k")