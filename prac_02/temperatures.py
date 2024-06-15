def main():
    celsius_temp = float(input("Enter temperature in Celsius: "))
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_temp}°F")
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is {celsius_temp}°C")

def celsius_to_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9

main()
