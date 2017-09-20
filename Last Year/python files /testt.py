import random

# Defines initial amounts of money and losses
money = 50
losses = 0


# Asks user how much to bet
def roulette_sim():
    print "How much do you want to bet?"
    bet = raw_input("> ")
    if bet > money:
        bet_too_much()
    else:
        red_or_black()


# Prevents one from betting more money than one has
def bet_too_much():
    print "You do not have all that money. Please bet again." 
    raw_input("Press ENTER to continue> ")
    roulette_sim()

# Asks user to select red or black, starts the sim, modifies money/losses
def red_or_black():
    print "OK, you bet %r" %  (bet)
    print "Red or black?"
    answer = raw_input("> ")
    number = random.randint(1, 2)
    if number == 1 and answer == "red":
        print "You win!"
        money += bet
        print "You now have %r money" % (money)
        print "Your losses are %r" % (losses)
        replay()
    elif number == 2 and answer == "black":
        print "You win!"
        money += bet
        print "You now have %r money" % (money)
        print "Your losses are %r" % (losses)
        replay()
    else:
        print "You lost!"
        money -= bet
        losses += bet
        print "You now have %r money" % (money)
        print "Your losses are %r" % (losses)
        replay()

# Asks user whether he/she wants to play again
def replay():
    print "Do you want to play again?"
    play_again = raw_input("y/n> ")
    if play_again == "y":
        roulette_sim()
    else:
        print "OK, bye loser!"


roulette_sim()
