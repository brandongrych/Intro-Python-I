# Write a function is_even that will return true if the passed-in number is even.



# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def oddEven(n):
    if int(n) % 2 == 0:
        print("even!")
    else:
        print("odd!")
oddEven(num)

