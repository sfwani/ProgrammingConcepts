'''
Description: This program defines a class called Retail_Item that contains data and methods for retail items such as type, amount in inventory, and price. The program also includes a main function that prompts the user to enter information for two items and displays the information in a neat table format.
'''

class Retail_Item:
    def __init__(self, item_type, inventory_amount, price):
        self.__item_type = item_type
        self.__inventory_amount = inventory_amount
        self.__price = price

    def __str__(self):
        return f"{self.__item_type.ljust(15)} {str(self.__inventory_amount).rjust(8)} {f'${self.__price:.2f}'.rjust(15)}"

def main():
    print("Enter information for two retail items:")
    print()
    
    item1_type = input("Name of item 1: ")
    item1_amount = int(input("Amount of item 1: "))
    item1_price = float(input("Price of item 1: "))

    item2_type = input("Name of item 2: ")
    item2_amount = int(input("Amount of item 2: "))
    item2_price = float(input("Price of item 2: "))

    item1 = Retail_Item(item1_type, item1_amount, item1_price)
    item2 = Retail_Item(item2_type, item2_amount, item2_price)

    print("\nHere is a summary of the items you added:")
    print("Item".ljust(15) + "Amount".rjust(10) + "Price".rjust(15))
    print("-" * 40)
    print(item1)
    print(item2)

if __name__ == "__main__":
    main()
