import random 

def main():
    directions()
    balance=100
    while balance>0:
        option=menu()
        if option=="4":
            directions()
        print "You have a balance of",balance
        bet=input("bet? ")
        if option=="1":
           balance=singleNumber(balance,bet)
        elif option=="2":
           balance=oddsEvens(balance,bet)
        elif option=="3":
            balance=thirds(balance,bet)
        elif option=="5":
            balance=0
        print "Balance: ", balance
        print
        print"Thanks for playing!"
    print "Welcome to the Best Internet Arcade in the World"
    print
    print "Game Choices:"
    print "Craps"
    print "Guessing Game"
    print "In Between"
    
def gamemenu():
    ans="0"
    while ans not in "12345":
        print "1) Craps"
        print "2) Guessing Game"
        print "3) In between"
        print "4) Instructions"
        print "5) Quit"
        ans=raw_input()
        return ans

    from random import *

def main1():
   num = randint(1,1000)
   low=1
   high=1000
   guess = 0
   numOfGuesses = 0
   while guess != num:
      numOfGuesses=numOfGuesses+1
      prompt="Guess a # between "+str(low)+" and "+str(high)+": "
      guess = input(prompt)
      if guess < num:
         print("Higher!")
         if guess>low:
            low=guess
      if guess > num:
         print("Lower!")
         if guess<high:
            high=guess
   print "Correct!  It took you",numOfGuesses,"tries."

main1()






    
    
    
    
