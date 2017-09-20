def crap():
    raw_input="Enter a number and see if you win"
    die1=radint(1,6)
    die2=radint(1,6)
    print die1+die2
    num=input("Enter a number from 1-6")
    print "Now Roll the dice"
    print
    print "You got...",ball
    print
    if die1+die2==num:
        print "You won!"
        balance=balance+bet*36
    else:
        print "Good Job, You Lost!"
        balance=balance-bet
    return balance
