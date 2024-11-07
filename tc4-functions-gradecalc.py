############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Andrew Beaver

numericGrade = 0.0

def openingMessage():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.")

def letterInput(p_course):
    return input("\nPlease enter a letter grade for " + p_course + ": ").upper()

def modifierInput():
    return input("Please enter a modifier (+, - or nothing) : ")

def calculateGrade(letterGrade, modifier):
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid entry is made
        print("You entered an invalid letter grade.")

    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3
    return numericGrade

# main() FUNCTION
def main():
    openingMessage()

    #prog calls
    progLetterGrade = letterInput("PROG1700")
    progModifier = modifierInput()

    progfinal = calculateGrade(progLetterGrade, progModifier)
    
    #NETW calls
    NetWLetterGrade = letterInput("NETW1700")
    NetWModifier = modifierInput()

    NETWFinal = calculateGrade(NetWLetterGrade, NetWModifier)

    #OSYS calls
    OSYSLetterGrade = letterInput("OSYS1200")
    OSYSModifier = modifierInput()

    OSYSFinal = calculateGrade(OSYSLetterGrade, OSYSModifier)

    #WEBD Calls
    WEBDLetterGrade = letterInput("WEBD1000")
    WEBDModifier = modifierInput()

    WEBDFinal = calculateGrade(WEBDLetterGrade, WEBDModifier)

    #COMM1700 calls
    COMMLetterGrade = letterInput("COMM1700")
    COMMModifier = modifierInput()

    COMMFinal = calculateGrade(COMMLetterGrade, COMMModifier)

    #DBAS calls
    DBASLetterGrade = letterInput("DBAS1007")
    DBASModifier = modifierInput()

    DBASFinal = calculateGrade(DBASLetterGrade, DBASModifier)

    # Output course results, with formatting
    print("\nThe final grade for PROG1700 is: {0:.1f}".format(progfinal))
    print("The final grade for NETW1700  is: {0:.1f}".format(NETWFinal))
    print("The final grade for OSYS1200  is: {0:.1f}".format(OSYSFinal))
    print("The final grade for WEBD1000  is: {0:.1f}".format(WEBDFinal))
    print("The final grade for COMM1700  is: {0:.1f}".format(COMMFinal))
    print("The final grade for DBAS1007  is: {0:.1f}".format(DBASFinal))

    #GPA math
    GPA = (progfinal + NETWFinal + OSYSFinal + WEBDFinal + COMMFinal + DBASFinal) / 6

    #Display GPA
    print("\nYour grade point average for the semester is: {0:.1f}".format(GPA))

#PROGRAM EXECUTION STARTS HERE
main()
