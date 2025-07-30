str1 = "hello My Name is Tejas"

str2 = "1234"

str3 = "9380  Tejas M"


# print(str1.capitalize())  # 	Converts the first character to upper case
# print(str1.casefold())    # Converts string into lower case
# print(str1.count('e'))   # Returns the number of times a specified value occurs in a string
# print(str1.encode())     # Returns an encoded version of the string
# print(str1.endswith('s')) #Returns true if the string ends with the specified value
# print(str1.expandtabs())  # Sets the tab size of the string
# print(str1.find('My'))   #Searches the string for a specified value and returns the position of where it was found
# print(str1.format(10))    # 	Formats specified values in a string



print("Nano123".isalnum())     # True
print("Nano 123".isalnum())    # False (contains space)
print("123!".isalnum())        # False (contains punctuation)

print(str1.isalpha())  # Returns True if all characters in the string are in the alphabet
print(str1.isascii())   #  Returns True if all characters in the string are ascii characters
print(str1.isdecimal())  #  	Returns True if all characters in the string are decimals
print(str1.isdigit())    #  Returns True if all characters in the string are digits
print(str1.islower())    # Returns True if all characters in the string are lower case
print(str1.isnumeric())  # 	Returns True if all characters in the string are numeric
space = " "
print(space.isspace())  # Returns True if all characters in the string are whitespaces
print(str1.isupper())    # Returns True if all characters in the string are upper case

myTuple = ("John", "Peter", "Vicky")

x = " noob, ".join(myTuple)  # Joins the elements of an iterable to the end of the string
print(x)

txt = "banana"

print(txt.ljust(10), "is my favorite fruit.")     # Returns a left justified version of the string
print(str1.lower())

pada = "       tejas       "
print(pada.lstrip(), "M")     # Remove spaces to the left of the string:

splitt = "welcome to the jungle"

print(splitt.split())    # Split a string into a list where each word is a list item:


string = "NanoPython123"
print(string)
print("index('Python') =", string.index('Python'))               # Found at index 4
print("index('Python', 0, 10) =", string.index('Python', 0, 10)) # Found within range
#print("index('xyz') =", string.index('xyz'))                     # Raises error


samples = ["Python", "Nano123", "Python3", "", "Nano Python"]

print("\nTesting str.isalpha()\n")
for s in samples:
    print(f"{s!r} : {s.isalpha()}")      # Check if all the characters in the text are letter



samples = ["12345", "Nano123", "007", "12.5", "", " "]

print("\nTesting str.isdigit()\n")
for s in samples:
    print(f"{s!r}: {s.isdigit()}") # Check if all the characters in the text are digits:


samples = ["123", "½", "²", "4.5", "abc", ""]

print("\nTesting str.isnumeric()\n")
for s in samples:
    print(f"{s!r}: {s.isnumeric()}")# True if all characters in the string are numeric characters—including digits (0–9), fractions (¼), superscripts (²), and other Unicode numeric characters. It’s broader than

samples = ["hello", "Hello", "123abc", "abc!", "ABC", ""]

print("\nTesting str.islower()")
for s in samples:
    print(f"{s!r}: {s.islower()}")
