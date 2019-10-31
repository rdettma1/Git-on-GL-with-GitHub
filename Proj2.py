#Imports the class information from the cashRegister class
import CashRegister

ADD_MONEY = "a"

REMOVE_MONEY = "r"

TRANSFER_MONEY = "t"

LOCK_REGISTER = "l"

UNLOCK_REGISTER = "u"

DISPLAY_STATE = "s"

CLOSE_STORE = "c"

OPTION_LIST = [ADD_MONEY,REMOVE_MONEY,TRANSFER_MONEY,LOCK_REGISTER,UNLOCK_REGISTER,DISPLAY_STATE,CLOSE_STORE]

REG_1 = 1

REG_2 = 2

LIST_REG_1 = 0

LIST_REG_2 = 1

#name: menuOptions
#input: none
#output: displays the corresponding meaning behind every menu option
def menuOptions():
    print("Menu Options:")
    print("A - Add money")
    print("R - Remove money")
    print("T - Transfer money")
    print("L - Lock register")
    print("U - Unlock register")
    print("S - Display register state")
    print("C - Close the store and quit")


#Name: mainMenu
#input: myRegList; a list of registers
#Output: runs the program in an apropriate manner for the user
def mainMenu(myRegList):

    #gets an initial menu choice from the user,
    #ensuring both upper and lowercase entries work
    menuOptions()

    choice = input("Enter option (A, R, T, L, U, S, C): ")

    choice = choice.lower()

    #goes through each option as long as the user does not close the store
    while(choice != CLOSE_STORE):


        #ensures valid input from the user
        while(choice not in OPTION_LIST):

            print("\nInvalid menu option. Please try again. \n")

            choice = input("Enter option (A, R, T, L, U, S, C): ")

            choice = choice.lower()


        #adds money to the register desired
        if(choice == ADD_MONEY):

            addMoney(myRegList)


        #removes money from register desired
        elif(choice == REMOVE_MONEY):

            removeMoney(myRegList)


        #moves money from one register to the other
        elif(choice == TRANSFER_MONEY):

            transferMoney(myRegList)


        #lockes a register
        elif(choice == LOCK_REGISTER):

            lockRegister(myRegList)


        #unlocks a register
        elif (choice == UNLOCK_REGISTER):

            unlockRegister(myRegList)


        #displays the state of the register
        elif(choice == DISPLAY_STATE):

            displayRegState(myRegList)


        #gets a new choice from the user if they didn't close the store,
        #ensuring both upper and lowercase entries work
        if(choice != CLOSE_STORE):

            menuOptions()

            choice = input("Enter option (A, R, T, L, U, S, C): ")

            choice = choice.lower()


    #closes the store; gets the total money out of each register
    print("Store Closing")

    totalCash = 0;

    for x in range(len(myRegList)):

        totalCash += myRegList[x].calcTotal()

    print("Total amount removed: $", totalCash , "\n")


    #removes the money from each register and locks them for the night

    for y in range(len(myRegList)):

        myRegList[y].close()

        print("Register ", y + 1 )

        myRegList[y].displayState()

        print()

    print("Thank you for using this application! Have a good evening")








#name: getRegChoice()
#input: none
#output: a number; the corresponding list index for the chosen register
def getRegChoice():

    #gets a register choice from the user, ensuring valid input
    choice = int(input("Register number (1 or 2): "))

    while((choice != REG_1) and (choice != REG_2)):
        print(choice, " is not a valid register number \n")

        choice = int(input("Register number (1 or 2): "))


    #returns the corresponding list value for the register chosen
    if(choice == REG_1):

        return LIST_REG_1

    else:

        return LIST_REG_2



#name: displayRegState()
#input: myRegList; a list of registers
#output: the state of the register is displayed to the user
def displayRegState(myRegList):

    #gets the valid register choice from the user, displays it properly
    myItem = getRegChoice()

    myRegList[myItem].displayState()



#name: addMoney()
#input: myRegList; a list of registers
#output: changes the value of the register the user asked for
def addMoney(myRegList):

    #gets the valid register choice from the user, adds money to it properly
    myItem = getRegChoice()

    myRegList[myItem].addMoney()


#name: removeMoney()
#input: myRegList; a list of registers
#output: changes the value of the register the user asked for
def removeMoney(myRegList):

    # gets the valid register choice from the user, removes money to it properly
    myItem = getRegChoice()

    myRegList[myItem].removeMoney()



#name: transferMoney()
#input: myRegList
#output: moves money from one register to another
def transferMoney(myRegList):


    #gets the register the user wants to move money from
    print("Enter register to transfer money from.")

    myItem = getRegChoice()

    if(myItem == LIST_REG_1):

        otherReg = LIST_REG_2

    else:

        otherReg = LIST_REG_1


    #transfers money accordingly
    myRegList[myItem].transferMoney(myRegList[otherReg])



#name: lockRegister()
#input: myRegList; a list of registers
#output: changes the locked status of a register
def lockRegister(myRegList):


    #gets the register choice, proceeds to lock it
    myItem = getRegChoice()

    myRegList[myItem].lock()



#name: unlockRegister()
#input: myRegList; a list of registers
#output: changes the locked status of a register
def unlockRegister(myRegList):

    # gets the register choice, proceeds to unlock it
    myItem = getRegChoice()

    myRegList[myItem].unlock()


#name: initRegList()
#input: none
#output: initializes the list of registers
def initRegList():

    myRegList = []

    print("Good Morning! Please initialize your registers:")

    #gets the number of each bill the user wants the registers to start with
    myOnes = int(input("Number of 1s: "))
    myFives = int(input("Number of 5s: "))
    myTens = int(input("Number of 10s: "))
    myTwenties = int(input("Number of 20s: "))

    #constructs two registers with the desired amount of money, appends both to a list of registers
    myRegister1 = CashRegister.cashRegister(myOnes,myFives,myTens,myTwenties)
    myRegister2 = CashRegister.cashRegister(myOnes,myFives,myTens,myTwenties)

    myRegList.append(myRegister1)
    myRegList.append(myRegister2)

    return myRegList



#name: main()
#input: none
#output: initializes the list of registers and
#proceeds to run the program for the user to change them as they please
if __name__ == "__main__":

    #initializes registers
    myRegisterList = initRegList()

    #runs mainMenu on the registers
    mainMenu(myRegisterList)



