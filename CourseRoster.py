###################################################################################
# CourseRoster.py: CMP131 Final Project                                           #
# This program manages course rosters for two sections of CMP131.                 #
# It reads enrollment data from text files, allows adding/removing students,      #
# combining rosters, and searching for students.                                  #
# Authored by: Ryan Koblentz                                                      #
# CMP131-20237: Fundamentals of Programming (Python)                              #
# Spring 2026                                                                     #
# Professor Tirrito                                                               #
# County College of Morris                                                        #
# Date Modified: 05/06/2026                                                       #
###################################################################################

def main():
    #Variable Initializations Area
    symbol = ''
    roster23130=[]
    roster20237=[]
    userChoice=0
    sentinel=-1
    
    symbol = input("Enter a Symbol to use for your Border Lines ==> ")
    roster23130=readSectionRoster(symbol, "Enrollments23130.txt")
    roster20237=readSectionRoster(symbol, "Enrollments20237.txt")
    #Starting the while loop to continuously execute program until user exits
    while userChoice!=sentinel:
        #Display the welcome banner
        welcomeBanner(symbol)

        #Calling the Main Menu
        userChoice=displayMainMenu(symbol)

        #Setting up Match Case to evaluate user choice
        match userChoice:
            case 1:
                #Calling the displayRoster function to open and read from the text file
                displayRoster(symbol, roster23130, "23130")

            case 2:
                displayRoster(symbol, roster20237, "20237")

            case 3:
                roster23130=addEnrollments(symbol,roster23130,"23130")
                writeSectionRoster(symbol,roster23130,"Enrollments23130.txt")
            case 4:
                roster20237=addEnrollments(symbol,roster20237,"20237")
                writeSectionRoster(symbol,roster20237,"Enrollments20237.txt")
            case 5:
                roster23130=processWithdrawals(symbol,roster23130,"23130")
                writeSectionRoster(symbol,roster23130,"Enrollments23130.txt")
            case 6:
                roster20237=processWithdrawals(symbol,roster20237,"20237")
                writeSectionRoster(symbol,roster20237,"Enrollments20237.txt")
            case 7:
                combineSectionRosters(symbol,roster23130,roster20237)
            case 8:
                searchForStudent(symbol,roster23130,roster20237)
            case 9:
                roster23130 = sortRoster(symbol,roster23130,"23130")
                roster20237 = sortRoster(symbol,roster20237,"20237")
            case 10:
                userChoice=int(input("You have selected Exit Program! If this was a mistake, " +
                                     "enter 0 to abort. Otherwise, enter -1 now to exit ==> "))

            case _:
                pass

        #End of match case
    




    #Calling the ClosingBanner function
    closingBanner(symbol)
    ### END OF THE MAIN FUNCTION ###

### START OF ALL OTHER PROGRAMMER-DEFINED FUNCTIONS ###
    
def welcomeBanner(symbol):
    borderLine = ""

    for i in range(80):
        borderLine += symbol

    print(borderLine)
    welcome = f'Welcome to the CMP131 Course Roster App'
    print(symbol + f"{welcome:^78}" + symbol)
    print(symbol + f"{'Written by: Ryan Koblentz':^78}" + symbol)
    print(symbol + f"{'Date Modified: Wednesday May 6th, 2026':^78}" + symbol)
    print(borderLine)
    print()
    print()
    print()

def closingBanner(symbol):
    borderLine = ""

    for i in range(80):
        borderLine += symbol

    print(borderLine)
    thanks = f'Thank You for Using the CMP131 Course Roster App'
    print(symbol + f"{thanks:^78}" + symbol)
    print(symbol + f"{'Written by: Ryan Koblentz':^78}" + symbol)
    print(symbol + f"{'Date Modified: Wednesday May 6th, 2026':^78}" + symbol)
    print(borderLine)
    print()

def displayMainMenu(symbol):
    borderLine = ""
    choice=0
    
    for i in range(80):
        borderLine += symbol

    print(borderLine)
    print(f"{'CMP131 Course Roster Main Menu':^80}")
    print(borderLine)
    print(f"{'1. Display Current Roster: Section 23130':<80}")
    print(f"{'2. Display Current Roster: Section 20237':<80}")
    print(f"{'3. Add Enrollments: Section 23130':<80}")
    print(f"{'4. Add Enrollments: Section 20237':<80}")
    print(f"{'5. Process Withdrawals: Section 23130':<80}")
    print(f"{'6. Process Withdrawals: Section 20237':<80}")
    print(f"{'7. Combine Section Rosters':<80}")
    print(f"{'8. Search for a Student':<80}")
    print(f"{'9. Sort a Section Roster':<80}")
    print(f"{'10. Exit the Program':<80}")
    print(borderLine)
    choice=int(input("Make A Selection Now ==> "))
    print(borderLine)
    print()
    print()
    print()
    return choice
#End of displayMainMenu function

#Start of defined functions
def readSectionRoster(symbol, filename):
    borderLine=symbol*80
    roster=[]
    print(borderLine)
    print(f"{'Reading Section Roster from File:':^80}")
    print(borderLine)
    try:
        file=open(filename, "r")
        for line in file:
            line=line.strip()
            record=line.split(",")
            roster.append(record)
        file.close()
        print(f"File '{filename}' loaded successfully!")
    except FileNotFoundError:
        print(f"Error! '{filename}' was not found. Make sure the file is in the same folder as your program.")
    print(borderLine)
    print()
    return roster
def displayRoster(symbol, roster, section):
    borderLine=symbol*80
    counter=1
    print(borderLine)
    print(f"{'Current Roster for Section ' + section + ':':^80}")
    print(borderLine)
    for record in roster:
        print(str(counter)+". "+record[0]+", "+record[1]+", "+record[2]+", "+record[3]+", "+record[4])
        counter+=1
    print(borderLine)
    print(f"{'End of Roster for Section '+section:^80}")
    print(borderLine)
    print()
def addEnrollments(symbol,roster,section):
    borderLine=symbol*80
    print(borderLine)
    print(f"{'Add New Enrollment for Section ' + section + ':':^80}")
    print(borderLine)
    lastName=input("Enter Student Last Name --> ")
    firstName=input("Enter Student First Name --> ")
    email=input("Enter Student Email --> ")
    date=input("Enter Enrollment Date (MM/DD/YYYY) --> ")
    newRecord=[lastName, firstName, section, email, date]
    roster.append(newRecord)
    print(borderLine)
    print(f"{'Student Added Successfully!':^80}")
    print(borderLine)
    print()
    return roster
def writeSectionRoster(symbol, roster, filename):
    borderLine = symbol * 80
    print(borderLine)
    print(f"{'Writing Updated Roster to File:':^80}")
    print(borderLine)
    try:
        file=open(filename,"w")
        for record in roster:
            file.write(record[0]+","+record[1]+","+record[2]+","+record[3]+","+record[4]+"\n")
        file.close()
        print(f"Updated Roster successfully saved to {filename}!")
    except FileNotFoundError:
        print(f"Error! Could not write to {filename}.")
    print(borderLine)
    print()
def processWithdrawals(symbol,roster,section):
    borderLine=symbol*80
    print(borderLine)
    print(f"{'Process Withdrawals for Section ' + section + ':':^80}")
    print(borderLine)
    #Display the roster so the user knows who they want to pick
    displayRoster(symbol, roster, section)
    #Ask the user which student they want to remove
    itemNumber=int(input("Enter the number of the student you want to withdraw --> "))
    itemNumber-=1
    withdrawnStudent=roster[itemNumber]
    #Write the withdrawn stuent to the withdrawals text file
    withdrawalFile="Withdrawals"+section+".txt"
    try:
        file=open(withdrawalFile, "a")
        file.write(withdrawnStudent[0]+","+withdrawnStudent[1]+","+withdrawnStudent[2]+","+withdrawnStudent[3]+","+withdrawnStudent[4]+"\n")
        file.close()
        print(f"Student added to {withdrawalFile} successfully!")
    except FileNotFoundError:
        print(f"Error! Could not write to {withdrawalFile}.")
    del roster[itemNumber]
    print(borderLine)
    print(f"{'Student Successfully Withdrawn!':^80}")
    print(borderLine)
    print()
    return roster
        
def combineSectionRosters(symbol,roster23130,roster20237):
    borderLine=symbol*80
    print(borderLine)
    print(f"{'Combine Section Rosters:':^80}")
    print(borderLine)
    #Combine both of the lists into one list
    combinedRoster=roster23130+roster20237
    #Write the combined roster to a file
    try:
        file=open("CombinedRoster.txt", "w")
        for record in combinedRoster:
            file.write(record[0]+","+record[1]+","+record[2]+","+record[3]+","+record[4]+"\n")
        file.close()
        print(f"{'Combined roster written to CombinedRoster.txt successfully!':^80}")
    except FileNotFoundError:
        print("Error! Could not write to CombinedRoster.txt")
    #Display the combined roster
    print(borderLine)
    counter=1
    for record in combinedRoster:
                print(str(counter)+". "+record[0]+", "+record[1]+", "+record[2]+", "+record[3]+", "+record[4])
                counter+=1
    print(borderLine)
    print(f"{'End of Combined Roster':^80}")
    print(borderLine)
    print()

def searchForStudent(symbol,roster23130,roster20237):
    borderLine=symbol*80
    print(borderLine)
    print(f"{'Search for a Student:':^80}")
    print(borderLine)
    searchName=input("Enter the Last Name of the Student you want to Search For --> ")
    #Combine both of the rosters so we can search for everyone at once 
    combinedRoster=roster23130+roster20237
    found=False
    for record in combinedRoster:
        if record[0].lower()==searchName.lower():
            print("Student Found!")
            print(record[0]+", "+record[1]+", "+record[2]+", "+record[3]+", "+record[4])
            found=True
    if found==False:
        print("No student found with that last name.")
    print(borderLine)
    print()
def sortRoster(symbol,roster,section):
    borderLine=symbol*80
    print(borderLine)
    print(f"{'Sorting Roster for Section'+section+':':^80}")
    print(borderLine)
    roster.sort()
    print(f"{'Roster sorted successfully!':^80}")
    print(borderLine)
    print()
    return roster
main() #Testing purposes
### THIS IS THE END OF THE COURSE ROSTER PROGRAM ###
#P.S. Thank you so much Professor Tirrito, this was a bit of a challenging class for me as I had no prior
#coding experience but I am now feeling motivated to try out some personal projects on my homelab
#Have a great summer! :D