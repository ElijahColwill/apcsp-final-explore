from random import randrange
import input
import time

def score_ai(score, history):
    score = 0
    change = 0
    hold = 0
    dice_left = 6
    while hold == 0:
        five_or_one = False
        threeofakind = False
        which3 = 0
        dice = []
        num_of_dice = 0
        while num_of_dice < dice_left:
            dice.append(randrange(1, 7))
            num_of_dice += 1
        repeats = []
        count = 1
        while count < 7:
            repeats.append(0)
            count += 1
        for x in dice:
            if x == 1:
                repeats[0] += 1
            elif x == 2:
                repeats[1] += 1
            elif x == 3:
                repeats[2] += 1
            elif x == 4:
                repeats[3] += 1
            elif x == 5:
                repeats[4] += 1
            elif x == 6:
                repeats[5] += 1
        element = -1
        for y in repeats:
            element += 1
            if y > 2:
                threeofakind = True
                which3 = element + 1

        print "Computer's roll is: %r.\n" % (dice)
        if threeofakind:
            print "Computer rolled three of a kind!.\n"
            score += (which3 * 100)
            dice_left -= 3
            history.append(1)
        if which3 == 5 or which3 == 1:
            five_or_one = True
        if repeats[0] > 0 and not five_or_one:
            print "Computer rolled at least one one!"
            score += (repeats[0] * 100)
            dice_left -= repeats[0]
            history.append(0.75)
        if repeats[4] > 0 and not five_or_one:
            print "Computer rolled at least one five!"
            score += (repeats[4] * 100)
            dice_left -= repeats[4]
            history.append(0.75)

        print "Computer's score is %d." % (score)

        if dice_left == 0:
            print "No dice left, rolling again. Press enter to continue."
            input.scan()
            dice_left = 6
            hold = 0
            history.append(1.25)
        elif score == change:
            print "Uh oh! Farkle. Score for this turn is 0, and the turn is over."
            score = 0
            hold = 1
            history.append(0)
        else:
            print "Computer has %d dice left." % (dice_left)
            print "Deciding wether to roll again. (press enter to continue)"
            hold = input.scan()
            risk_setting = randrange(0, 7)
            average_luck = sum(history)/float(len(history))
            if risk_setting > 5 or average_luck > 0.9:
                hold = 0
                print "Decided to roll! \n"
            else:
                hold = 1
                print "Decided to hold! Turn over. \n"
    return score, history

def score_player(score):
    score = 0
    change = 0
    hold = 0
    dice_left = 6
    while hold == 0:
        five_or_one = False
        threeofakind = False
        which3 = 0
        dice = []
        num_of_dice = 0
        while num_of_dice < dice_left:
            dice.append(randrange(1, 7))
            num_of_dice += 1
        repeats = []
        count = 1
        while count < 7:
            repeats.append(0)
            count += 1
        for x in dice:
            if x == 1:
                repeats[0] += 1
            elif x == 2:
                repeats[1] += 1
            elif x == 3:
                repeats[2] += 1
            elif x == 4:
                repeats[3] += 1
            elif x == 5:
                repeats[4] += 1
            elif x == 6:
                repeats[5] += 1
        element = -1
        for y in repeats:
            element += 1
            if y > 2:
                threeofakind = True
                which3 = element + 1

        print "Your roll is: %r.\n" % (dice)
        if threeofakind:
            print "You rolled three of a kind!.\n"
            score += (which3 * 100)
            dice_left -= 3
        if which3 == 5 or which3 == 1:
            five_or_one = True
        if repeats[0] > 0 and not five_or_one:
            print "You rolled at least one one!"
            score += (repeats[0] * 100)
            dice_left -= repeats[0]
        if repeats[4] > 0 and not five_or_one:
            print "You rolled at least one five!"
            score += (repeats[4] * 100)
            dice_left -= repeats[4]

        print "Your score is %d." % (score)

        if dice_left == 0:
            print "No dice left, must roll again. Press enter to continue."
            input.scan()
            dice_left = 6
            hold = 0
        elif score == change:
            print "Uh oh! Farkle. Score for this turn is 0, and the turn is over."
            score = 0
            hold = 1
        else:
            print "You have %d dice left." % (dice_left)
            print "Do you want to roll again? Type 'y' for Yes or anything else for No and press enter."
            hold = input.scan()
            if hold == "Yes" or hold == "yes" or hold == "y" or hold == "Y":
                hold = 0
            else: hold = 1
    return score


def turn(total, turn, history):
    print "Start turn!"
    hold = 0
    if turn == False:
        total = score_player(total)
    else:
        total, history = score_ai(total, history)
    return total, history


def game():
    history = []
    print "Welcome to Two Player Farkle!\n"
    print """Farkle is a dice game in which players attempt to reach 10,000 in score
    by rolling six 6-sided die. Points are scored by rolling ones, fives,
    or three-of-a-kind. Ones are worth 100 points, fives are worth 500, and three-of-a-kind is worth
    100 times the face value.\n """
    player_score = 0
    computer_score = 0

    while player_score < 10000 and computer_score < 10000:
        print "Press enter when ready to start player turn."
        input.scan()
        player_score = turn(player_score, False, history)
        print "\nPlayer score: %d" % player_score
        print "\nPress enter when ready to start computer turn."
        input.scan()
        computer_score, history = turn(computer_score, True, history)
        print "\nComputer score: %d" % computer_score

    if player_score >= 10000:
        print "\nPlayer wins!"
    else: print "\nComputer wins!"

    print "\nHere are the scores:"
    print "Player score: %d" % player_score
    print "Computer score: %d" % computer_score


game()
