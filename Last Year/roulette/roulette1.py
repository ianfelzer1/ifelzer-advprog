# Roulette
# MZ and class
# Nov. 2016
# needs roulette2.py

from random import *
from roulette2 import *

def main():
    directions()
    balance=100
    while balance>0:
        option=menu()
        if option=="4":
            directions()
        print "you have a balance of",balance
        bet=input("bet? ")
        if option=="1":
           balance=singleNumber(balance,bet)
        elif option=="2":
           balance=oddsEvens(balance,bet)
        elif option=="3":
            balance=thirds(balance,bet)
        elif option=="5":
            balance=0
        print "Balance: ",balance
    print
    print "Thanks for playing!"

main()
