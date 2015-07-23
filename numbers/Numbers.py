"""no1 = 5
no2 = 2

add = no1 + no2 #addition
sub = no1 - no2 #subtration
mul = no1 * no2 #multiplication
div = no1 / no2 #division
exp = no1 ** no2 #exponent
mod = no1 % no2 #modulo

print("Numbers: %d , %d" % (no1, no2))
print("Addition: %d" % no1 + " + %d" % no2 + "= %d" % add)
print("Subtration: %d" % no1 + " - %d" % no2 + "= %d" % sub)
print("Multiplication: %d" % no1 + " * %d" % no2 + "= %d" % mul)
print("Division: %d" % no1 + " / %d" % no2 + "= %d" % div)
print("Exponent: %d" % no1 + " ** %d" % no2 + "= %d" % exp)
print("Modulo: %d" % no1 + " %% %d" % no2 + "= %d" % mod)
"""


#format numbers
print("Number: %d" % 5)
print("Number: %3d" % 5) #this is like justified the numbers by 3 leading spaces.
print("Number: %03d" % 5) #this is like justified the numbers by 3 leading zeros.
print("Number: %f" % 5)
print("Number: %.2f" % 5)

#another method of formatting the numbers
print("\n\nNumber: {0:d}".format(5))
print("Number: {0:3d}".format(5))
print("Number: {0:03d}".format(5))
print("Number: {0:f}".format(5))
print("Number: {0:.2f}".format(5))

#the \ indicates there is continuation next line
print("\n\nThree number, First is {0:d}, \
Second is {1:d} and {2:d}".format(7,8,9))

