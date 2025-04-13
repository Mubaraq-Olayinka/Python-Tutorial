import math
#String Data type 

#literal assignment 
first = "Mubaraq"
last = "Olayinka"

# print(type(last))
# print(type(last) == str)
# print(isinstance(last, str))


#constructor function
# pizza = str("pepperoni")

# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting number to string
decade = str(1980)

print(type(decade))
print(decade)

statement = "I like the rock music from " + decade + "s"
print(statement)

#multiline 
multiline = '''
Hey, how are you                              

I was just checking in.          
                            All good?
'''

print(multiline)

# escaping special characters 

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#string methods

print(first)
print(first.upper())
print(first.lower())
print(first)

print(multiline.title())
print(multiline.replace("good", "okay"))
print(multiline)

print(len(multiline))
multiline += "                            "
multiline = "            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print('')

#Build a menu

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print('')

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some methods return boolean data 
print(first.startswith('D'))
print(first.endswith('q'))

# Boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric data types 
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

# float type 
gpa = 3.14 
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers 
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting string to number 
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#error if you attempt to cast incorrect data
# zip_value = int("New York")