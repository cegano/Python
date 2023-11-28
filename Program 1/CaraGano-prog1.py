# Cara Gano- Program 1

temperature = input("Enter a temperature value to convert: ")
temperature = int(temperature)
convert = input("Convert to Fahrenheit or Celsius? Enter F or C: ")

if convert == "F" or convert == "f":
    degC = round(1.8 * temperature + 32, 1)
    print(str(temperature) + " degrees C" + " = " + str(degC) + " degrees F")
elif convert == "C" or convert == "c":
    degF = round((temperature - 32) / 1.8, 1)
    print(str(temperature) + " degrees F" + " = " + str(degF) + " degrees C")
else:
    print("You did not enter an F or C. Goodbye.")
    quit()

