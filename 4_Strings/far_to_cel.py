# Convert input farenheit to celsius
# Formula farenheit minus 32 multiplied by 5 divided by 9

farenheit: float = float(input('Please enter degrees in farenheit\t > '))
print(f'{farenheit} degrees Farenheit is equal to {round(
      (farenheit - 32) * 5 / 9, 4)} degrees Celsius')
