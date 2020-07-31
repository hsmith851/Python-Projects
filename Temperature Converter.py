from numpy.core import double
from pip._vendor.distlib.compat import raw_input

Celsius = double(raw_input ("Enter a temperature in Celsius: "))
Fahrenheit = 9.0 / 5.0 * Celsius + 32
print("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")
