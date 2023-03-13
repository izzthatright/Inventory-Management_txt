#verified working with python 3.6.1
import os     
import csv   #added this because original file was not saving to the txt file.
clear =lambda: os.system('cls')

def main():
    clear()
    print("INVENTORY MANAGEMENT")
    print("--------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Add Items To Inventory")
    print("2 - View Inventory")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            addItemsToInventory()
            break
        elif userChoice == '2':
            viewInventory()
            break

def addItemsToInventory():
    clear()
    print("ADD ITEMS TO INVENTORY")
    print("----------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Add Multiple Items")
    print("2 - Add Single Item")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice in ['1','2']:
            break
    if userChoice == '1':
        print()
        while True:
            numItems = input("Enter The Number Of Items To Be Added: ")
            if numItems.isdigit():
                break
        numItems = int(numItems)
        userItems = {}
        for i in range(1, numItems+1):
            while True:
                print()
                user_item = input("Item Name: ")
                if user_item != '':
                    break

            while True:
                item_amount = input("Item Amount: ")
                if item_amount.isdigit():
                    break
            userItems.update({user_item: int(item_amount)})

        addItemsToFile(userItems, clear=False)
        returnToMainMenu("Item Have Been Added")

    elif userChoice== '2':
        print()
        while True:
            user_item = input("Item Name: ")
            if user_item != '':
                break
        while True:
            item_amount = input("Item Amount: ")
            if item_amount.isdigit():
                break
        addItemsToFile({user_item: int(item_amount)}, clear=False)
        returnToMainMenu("Item Has Been Added")
    

def viewInventory():
    clear()
    print("VIEW INVENTORY")
    print("--------------")
    print()
    print()
    invItems= getInvItems()
    print("Items")
    print("-----")
    print()
    for item in invItems:
        print(f"{item}:{invItems[item]}")

    print()
    print("Available Options:")
    print("1 - Edit Item")
    print("2 - Delete Item")
    print("B - To Go Back: ")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == 'b':
            main()
            break
        elif userChoice == '1':
            editInventoryItem()
            break
        elif userChoice== '2':
            deletInventoryItem()
            break

def editInventoryItem():
    clear()
    print()
    print("EDIT INVENTORY ITEM")
    print("-------------------")
    print("Press (B) To Go Back")
    print()
    print("Available Options:")
    print()
    print("1 - Edit Item Name")
    print("2 - Edit Item Amount")
    print()
    while True:
        userChoice = input("Choose An Option: ").lower()
        if userChoice in ['1','2','b']:
            break
    if userChoice == 'b':
        main()

    invItems= getInvItems()
    if userChoice == '1':
        print()
        while True:
            itemToChange = input("Enter The Name of the Item to Edit: ")
            if itemToChange in invItems:
                break
            else:
                print("That Item Does Not Exist")
                print()
        while True:
            newItemName= input("Enter The New Item Name: ")
            if newItemName != '':
                break
        invItems.update({newItemName: invItems[itemToChange]})
        del invItems[itemToChange]

        addItemsToFile(invItems, clear=True)
        returnToMainMenu("Item Name Has Been Changed")

    elif userChoice == '2':
        print()
        while True:
            itemToChange = input('Enter the Name Of The Item To Edit: ')
            if itemToChange in invItems:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newAmountName = input("Enter the New Item Amount: ").lower()
            if newAmountName != '':
                break

        invItems.update({itemToChange: newAmountName})
        addItemsToFile(invItems, clear = True)
        returnToMainMenu("Item Amount Has Been Changed")

def deleteInventoryItems():
    print("DELETE INVENTORY ITEM")
    print("---------------------")
    print()
    invItems = getInvItems()
    while True:
        itemToDelete = input("Enter The Name of the Item To Delete: ")
        if itemToDelete in invItems:
            break
        else:
            print("That Item Does Not Exist")
            print()

    while True:
        confirmation = input("CONFIRMATION: Are You Sure You Want To Delete This Item?").lower()
        if confirmation in ['yes','no']:
            break
    if confirmation == 'yes':
        del invItems[itemToDelete]
        addItemsToFile(invItems, clear= True)
        returnToMainMenu("Item Has Been Deleted")
    else:
        main()      


def addItemsToFile(userItems: dict, clear: bool):
    if clear:
        with open('userItems.txt', 'w') as f:
            f.truncate()
    with open('userItems.txt', 'a') as f:
        writer = csv.writer(f)
        for item, amount in userItems.items():
            writer.writerow([item, amount])


'''  removed this because was not writing to txt file        
def addItemsToFile(userItems: dict, clear: bool):
    if clear:
        with open('userItems.txt', 'a') as file:
            for item in userItems:
                file.write(f"{item}: {userItems[item]}")
                file.write('\n')
        return
    invItems = getInvItems()

    for item in userItems:
        #CHECK IF THE ITEM HAS ALREADY BEEN ADDED
        if item in invItems:
            invItems[item] += userItems[item]
    with open('userItems.txt', 'a') as file:
        for item in invItems:
            file.write(f"{item}: {invItems[item]}")
            file.write('\n')

def getInvItems():
    invItems = {}
    with open('userItems.txt','r') as file:
        for line in file:
            line = line.replace('\n','').split(':')
            itemName, itemAmount = line[0], line[1].strip()
            invItems.update({itemName: int(itemAmount)})
    return invItems
'''
def getInvItems():
    items = {}
    with open('userItems.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) >= 2:
                    itemName, itemAmount = parts[0], parts[1].strip()
                    items[itemName] = int(itemAmount)
    return items

def returnToMainMenu(message):
    while True:
        print()
        back = input(f"{message}. Press (M) To Return To Main Menu: ").lower() if message != None else input("Press (M) To Return To Main Menu: ").lower()
        if back == 'm':
            main()
            break

main()
