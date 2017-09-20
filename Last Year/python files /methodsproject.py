# shell program to practice using methods/functions
# fill this out completely, then change this comment!
# Also, change the name of the program
# Note:  this is INTENTIONALLY incomplete!
# your name
# date

def directions():
    # give directions here, ask for name, return name
    x=raw_input("Enter your name")
    return x

def lowHigh(a,b):
    print "currently:",a,b
     #write code here to put a and b in order
    # should you return those values?
    print "currently:",a,b
    if a>b:
        return a,b
    if b>a:
        return b>a

def triTest():
    # write code here to test whether 3 numbers can form the sides of a triangle
    # what sort of return statement should be here?
    if a+b>c:
         return "True"
    if b+c>a:
        return "True"
    if a+c>b:
        return "True"
     
def heron(x,y,z):
    #look up Heron's formula
    
def main():
    name=directions()
    print "Hi there,",name
    # have the user enter 2 numbers, x and y
    # go to lowHigh and compare them
    # print the numbers from low to high
    print "The numbers from low to high are: ",x,y
    x,y,z=input("Enter 3 numbers and I'll tell you whether they can form a triangle: ")
    if triTest(x,y,z):
        print "The area of the triangle is: ", # print area here
    else:
        print "Those 3 sides can't form a triangle."
    

# Extra:  write a program or method to find all odd cubes between 10,000 and 20,000


main()
