#Built-in Types
#Booleans
print(" Python program to demonstrate boolean type")
  
print(type(True))
print(type(False))
print("----------------------------------------")
x=False
y=True
x or y       # if x is False then y otherwise x
print(type(x))
print(x)
x and y      # if x is False then x otherwise y
print(type(y),x)
not x        # if x is True then False, otherwise True
print(type(x),x)

print("boolean values are used in arithmetic operations(1 and 0 for True and False)")
a=True + False == 1   # 1 + 0 == 1
b=True * True == 1    # 1 * 1 == 1
print(a)
print(b)
print("----------------------------------------")
# Python program to demonstrate numeric value
  
a = 5
print("Type of a: ", type(a))
  
b = 5.0
print("\nType of b: ", type(b))
  
c = 2 + 4j
print("\nType of c: ", type(c))
print("----------------------------------------")
# Creating a String

# with single Quotes 
String1 = 'hello world'
print("String with the use of Single Quotes: ") 
print(String1) 
    
# with double Quotes 
String1 = "H'eello"
print("\nString with the use of Double Quotes: ") 
print(String1) 
print(type(String1))
    
# with triple Quotes 
String1 = '''hi'My name is"Apurva"'''
print("\n String with the use of Triple Quotes: ") 
print(String1) 
print(type(String1))
  
# Quotes allows multiple lines 
String1 = '''My 
            Name is
            Apurva'''
print("\nCreating a multiline String: ") 
print(String1) 
