# Roulette
# MZ and class
# Nov. 2016

from random import *

def directions():
    print "Welcome to Roulette"
    print
    print "Betting choices:"
    print "you can bet on a single number (36:1 payback"
    print "evens/odds (2:1)"
    print "1st, 2nd or 3rd third (3:1 payback)"
    print
    print "There are 36 possible slots, but remember, the wheel includes 0 and 00"
    
def menu():
    ans="0"
    while ans not in "12345":
        print "1) choose a single number"
        print "2) odd/evens"
        print "3) 1st, 2nd or 3rd third"
        print "4) Directions"
        print "5) Quit"
        ans=raw_input()
    return ans
    
def singleNumber(balance,bet):
    ball=randint(1,36)
    #print ball
    num=input("enter a number from 1-36: ")
    print "rolling...rolling...rolling"
    print
    print "The ball lands in...",ball
    print
    if ball==num:
        print "winner!!!"
        balance=balance+bet*36
    else:
        print "loser!  Put an L on your forehead!"
        balance=balance-bet
    return balance       

def oddsEvens(balance,bet):
    ball=randint(1,36)
   # print ball
    if ball%2==0:
        evenOdd="e"
    else:
        evenOdd="o"
    ans="a"
    while ans not in "oe":
        ans=raw_input("(o)dds or (e)vens: ")
        ans=ans.lower()       
    print "rolling...rolling...rolling"
    print
    print "The ball lands in...",ball
    print
    if evenOdd==ans:
        print "winner!!!"
        balance=balance+bet*2
    else:
        print "loser!  Put an L on your forehead!"
        balance=balance-bet
    return balance

def thirds(balance,bet):
    ball=randint(1,36)
    #print ball
    if ball<13:
        third="1"
    elif ball<27:
        third="2"
    else:
        third="3"
    ans="0"
    while ans not in "123":
        print "choose a third, 1, 2 or 3" 
        ans=raw_input()
    print "rolling...rolling...rolling"
    print
    print "The ball lands in...",ball
    print
    if third==ans:
        print "winner!!!"
        balance=balance+bet*3
    else:
        print "loser!  Put an L on your forehead!"
        balance=balance-bet
    return balance
 
