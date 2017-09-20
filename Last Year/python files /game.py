x = False 
print ("Welcome to the littest game ever made")
def keep_going():
    join = raw_input("Do you want to continue")
    if join == 'yes':
        x = True
    else:
        x == False
        print "You have chosen to exit the program"
        quit()
keep_going()

def main():
    options = ["text adventure","nothing"]
    if x == True:
        print("which game would you like to play"),options
    else:
        print("yes")
    journey = ["Adventure","Play it Safe"]
    print("Welcome to my text adventure game")
    ask = input("Please select an journey"), journey
    while ask == "Adventure":
        print ("Good")
    
           

main()

