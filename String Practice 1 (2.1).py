studentMajor = input("What is your major?")
majorLength = len(studentMajor)
print("Length of " + studentMajor + ' is ' + str(majorLength) + " characters.")

lastIndex = majorLength - 1
print("Last character of your major is " + studentMajor[lastIndex] + ".")
