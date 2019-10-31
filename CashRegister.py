
#Defines the class
class cashRegister:
    def __init__(self,ones,fives,tens,twenties):

        #Initialized the values for each of its data objects
        self.__locked = False
        self.__ones = ones
        self.__fives = fives
        self.__tens = tens
        self.__twenties = twenties


    #function for user to add money to a register
    def addMoney(self):

        #If the register is unlocked, it allows the user to add however much money they can to it
        if(self.__locked != True):

            myOnes = int(input("Number of 1s: "))
            myFives = int(input("Number of 5s: "))
            myTens = int(input("Number of 10s: "))
            myTwenties = int(input("Number of 20s: "))

            self.__ones += myOnes
            self.__fives += myFives
            self.__tens += myTens
            self.__twenties += myTwenties
            print("Money added successfully!")

        #denies editing of the values within a locked register
        else:
            print("You cannot add money to a locked register.")


    #function for user to remove money from a register
    def removeMoney(self):

        #if the register is unlocked, the user is allowed to take money from it
        if(self.__locked != True):

            myOnes = int(input("Number of 1s: "))
            myFives = int(input("Number of 5s: "))
            myTens = int(input("Number of 10s: "))
            myTwenties = int(input("Number of 20s: "))


            #before changing the amount of money in the register, this code checks if there are
            #enough bills of that type to remove from that register
            validMoney = True

            if(myOnes > self.getOnes()):

                validMoney = False

            if(myFives  >self.getFives()):

                validMoney = False

            if (myTens > self.getTens()):

                validMoney = False

            if (myTwenties > self.getTwenties()):

                validMoney = False


            #Removes the amount of requested money from the register if it is a valid amount
            if(validMoney == True):


                self.__ones -= myOnes
                self.__fives -= myFives
                self.__tens -= myTens
                self.__twenties -= myTwenties
                print("Money removed successfully!")


            #Tells the user if they have entered an invalid amount of bills
            else:

                print("You cannot remove more bills than the register has")

        #Tells the user if their register is locked and cannot be accessed
        else:
            print("You cannot remove money from a locked register.")


    #function used to add a set amount of money from a register
    #helper function
    def __addSetMoney(self,ones,fives,tens,twenties):
        self.__ones += ones
        self.__fives += fives
        self.__tens += tens
        self.__twenties += twenties

    #function used to remove a set amount of money from a register
    #helper function
    def __removeSetMoney(self, ones, fives, tens, twenties):
        self.__ones -= ones
        self.__fives -= fives
        self.__tens -= tens
        self.__twenties -= twenties


    #Moves a valid quantity of money to another register
    def transferMoney(self, myRegister):

        #prevents transfer if either register is locked
        if((self.__locked != True) and (myRegister.__locked != True)):

            myOnes = int(input("Number of 1s: "))
            myFives = int(input("Number of 5s: "))
            myTens = int(input("Number of 10s: "))
            myTwenties = int(input("Number of 20s: "))


            #makes sure the quantity the user wants to move is apropriate for
            #the register
            validMoney = True

            if(myOnes > self.getOnes()):

                validMoney = False

            if(myFives  >self.getFives()):

                validMoney = False

            if (myTens > self.getTens()):

                validMoney = False

            if (myTwenties > self.getTwenties()):

                validMoney = False


            #if an apropriate amount of money has been requested, this code
            #takes that money from this register and adds it to another one
            if(validMoney == True):


                self.__ones -= myOnes
                self.__fives -= myFives
                self.__tens -= myTens
                self.__twenties -= myTwenties

                myRegister.__addSetMoney(myOnes,myFives,myTens,myTwenties)
                print("Money transferred successfully!")

            #prevents transer of an invalid amount of money
            else:

                print("You cannot transfer more bills than the register has")

        #prevents access to locked registers
        else:
            print("You cannot transfer money from a locked register.")



    #displays all attributes of a register
    def displayState(self):
        print("Register State:\n")

        print("Locked Status:")

        #says whether or not the register is locked
        if(self.__locked == False):
            print("The Register is Unlocked\n")
        else:
            print("The Register is Locked\n")


        #displays the status of the amount of each bill and the total amount
        #of money in the register
        print("Register Money:")
        print("ones: ", self.getOnes())
        print("fives: ", self.getFives())
        print("tens: ", self.getTens())
        print("twenties: ", self.getTwenties())
        print("Total:", self.calcTotal())
        print("\n")


    #lockes the register
    def lock(self):
        self.__locked = True

    #unlocks the register
    def unlock(self):
        self.__locked = False

    #getter on register locked status
    def getIsLocked(self):
        return self.__locked

    #getter on register ones
    def getOnes(self):
        return self.__ones

    #getter on register fives
    def getFives(self):
        return self.__fives

    #getter on register tens
    def getTens(self):
        return self.__tens

    #getter on register twenties
    def getTwenties(self):
        return self.__twenties

    #calculates the total money in each register
    def calcTotal(self):
        myTotal = 0
        myTotal += self.__ones
        myTotal += (self.__fives * 5)
        myTotal += (self.__tens * 10)
        myTotal += (self.__twenties * 20)
        return myTotal


    #closes the register by removing all the money inside of it and locking it afterwards
    def close(self):
        ones = self.__ones
        fives = self.__fives
        tens = self.__tens
        twenties = self.__twenties

        self.unlock()

        self.__removeSetMoney(ones,fives,tens,twenties)

        self.lock()




#tester for various functions in the cashRegister class
if __name__ == "__main__":
    myRegister = cashRegister(6,7,8,9)

    myRegister.displayState()

    myRegister.lock()

    myRegister.addMoney(1,1,1,1)

    myRegister.removeMoney(1,1,1,1)

    myRegister.displayState()

    myRegister.unlock()

    myRegister.addMoney(2,4,6,8)

    myRegister.displayState()

    myRegister.removeMoney(1,2,3,4)

    myRegister.displayState()

