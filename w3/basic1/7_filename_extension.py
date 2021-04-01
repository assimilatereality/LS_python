file = input("What is the filename? ")
parts = file.split('.')
print("The extension of the file is " + parts[-1])

print ("The extension of the file is : " + repr(parts[-1]))

huh = parts[-1]
print(type(huh))