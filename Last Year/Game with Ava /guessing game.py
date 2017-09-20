from random import *

def main():
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

main()
