''' 
Description: this program asks user for multiple inputs that are stored into
specific variables which are later used in a formula that helps a person to calculate
the total number of grapevines that can be cultivated in one row.
'''

lengthOfRow = float(input("Enter the length of the row, in feet:\n"))
amountOfSpace = float(input("Enter the amount of space, in feet, used by an end-post assembly:\n"))
distanceBetweenVines = float(input("Enter the distance, in feet, between each vine:\n"))

numberOfGrapevines = (lengthOfRow - 2*amountOfSpace)/distanceBetweenVines

print("You have enough space for", "{:.1f}".format(numberOfGrapevines), "grapevine(s) only.")
