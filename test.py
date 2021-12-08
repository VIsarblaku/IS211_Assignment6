# -*- coding: utf-8 -*-

import conversions 

testNumber = int(input("Number of tests: "))

for i in range(testNumber):
    celsius =  float(input("Enter float values of temperature in celsius: "))
    kelvin = conversions.convertCelsiusToKelvin(celsius)
    fahrenheit =  conversions.convertCelsiusToFahrenheit(celsius)
    print(f'{celsius} °C is {fahrenheit} °F and {kelvin} K')
    
for i in range(testNumber):
    fahrenheit =  float(input("Enter float values of temperature in fahrenheit: "))
    celsius = conversions.convertFahrenheitToCelsius(fahrenheit)
    kelvin =  conversions.convertFahrenheitToKelvin(fahrenheit)
    print(f'{fahrenheit} °F is  {celsius} °C and {kelvin} K')
    
for i in range(testNumber):
    kelvin =  float(input("Enter float values of temperature in kelvin: "))
    celsius = conversions.convertKelvinToCelsius(kelvin)
    fahrenheit =  conversions.convertKelvinToFahrenheit(kelvin)
    print(f' {kelvin} K is  {celsius} °C and {fahrenheit} °F')