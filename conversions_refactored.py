# -*- coding: utf-8 -*
#Part IV
class ConversionNotPossibleexception(Exception):
    """Conversion not possible class."""
    pass

def convert(fromUnit, toUnit, value):
    temperature = ["K", "C", "F"]
    distance = ["Miles", "Yards", "Meters"]
    if fromUnit in temperature and toUnit in temperature:
        #Conversion to Kelvin
        toK = {'K': lambda val: val,
               'C': lambda val: val + 273.15,
               'F': lambda val: (val + 459.67)*5/9,
              }
        #Conversion from Kelvin
        fromK = {'K': lambda val: val,
                 'C': lambda val: val - 273.15,
                 'F': lambda val: val*9/5 - 459.67,
                }
             
        if fromUnit == toUnit:
           # No conversion needed!
            return value
        #Convert fromUnit  to K.
        temp = toK[fromUnit](value) 
        # Now convert it from K to toUnit and return its value.
        return fromK[toUnit](temp)
    
    elif fromUnit in distance and toUnit in distance:
        #Conversion to Meters
        toMeters = {'Meters': lambda val: val,
               'Yards': lambda val: val * 0.9144,
               'Miles': lambda val: val * 1609.344,
              }
        #Conversion from Meters
        fromMeters = {'Meters': lambda val: val,
                 'Yards': lambda val: val / 0.9144,
                 'Miles': lambda val: val / 1609.344,
                }
             
        if fromUnit == toUnit:
           # No conversion needed!
            return value
        #Convert fromUnit  to Meters .
        temp = toMeters[fromUnit](value) 
        # Now convert it from Meters to toUnit and return its value.
        return fromMeters[toUnit](temp)
        
    else:
        raise ConversionNotPossibleexception('Conversion not possible from unit {} to to {}.'.format(fromUnit, toUnit))

