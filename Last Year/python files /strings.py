
# Program to demonstrate operations with strings
# Matt Z
# November, 2015

# Useful string functions:  len, ord, chr, str

def main():
    line = raw_input ("Enter a string: ")
    print line
    print "This line has",len(line),"characters."
    for i in range (0,len(line)):
        print line[i]
    raw_input("\nPress <return> to continue") #\n is newline character  
    print
    for i in line:
        print i #this does the same thing as the FOR loop above
    raw_input("\nPress <return> to continue")     
    line2 = line +"hello"       #this appends to the end of a string
    print line2
    # remember, counting begins at 0
    print (line2[1:4])    #prints characters 1, 2 and 3
    print line2[:6]     #prints from beginning of string to character 5
    print line2[2:]     # from character 3 to end
    print line2[-1]     #last character
    line3=""
    print line3
    for i in range (1,len(line2)-3):
        line3=line3+line2[i*-1]   #creates line3 from end back to 3rd character  
    print line3
    lenLine = len(line) #easier to create a separate variable if using several times
    for i in range (0,lenLine):

        # note use of ord and chr below
        
        if ord(line[i]) < 65:
            print line[i],"is not a letter"
    nonLetters = ""         #create a null variable
    for i in range (0,lenLine):
        if ord(line[i]) < 65:
            if ord(line[i])==32:        #ASCII 32 is a space
                nonLetters=nonLetters+"space"   
            else:
                nonLetters=nonLetters+line[i]
    print nonLetters
    x = input("Enter a number between 40 and 127: ")
    if x>0 and x<128:
        print "That character is: ",chr(x)
    x=input("\nType a number between 100 and 1000")
    print ("hi"*x)  #prints "hi" x times
main()
