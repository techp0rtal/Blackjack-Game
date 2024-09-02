#This is a simplified version of Blackjack.
#Rule differences are
import art
import random
print(art.logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def display():
    print(f"Your cards: {your_cards}, current score: {your_score}")
    print(f"Computer's first card: {comp_first_card}")
    # use parameters for this? your_f_hand, your_f_score, comp_f_hand, comp_f_score


# this will draw a card for whichever player we specify. we specify it through the "whose_score" parameter.
# it tells the function who it is drawing a card for/which score to compare the ace to
def draw_card(whose_score):
    new_card = random.choice(cards)
    if new_card == cards[0] and new_card + whose_score > 21:
        new_card = 1
    return new_card
    # now we gotta add the computer part. have draw card do both? or just for one player?

def game_end(your_f_hand, your_f_score, comp_f_hand, comp_f_score, outcome):
    print(f"Your final hand: {your_f_hand}, final score: {your_f_score}")
    print(f"Computer's final hand: {comp_f_hand}, final score: {comp_f_score}")
    if outcome == "d":
        print("Draw 🙃")
    elif outcome == "w" :
        print("Opponent went over. You win 😁")
    else:
        print("You went over. You lose 😭")

# def check_score(input_score):

# def clear_console():
#     print("\n" * 20)
#     blackjack_game()

#main
continue_playing = True
while continue_playing == True:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "n":
        break

    your_cards = []  # important
    your_selected_cards = random.sample(cards, 2)
    your_first_card = your_selected_cards[0]

    your_cards.extend(your_selected_cards)
    your_score = sum(your_cards)  # important

    computers_cards = []  # important
    comp_selected_cards = random.sample(cards, 2)
    # check if over 21?
    computers_cards.extend(comp_selected_cards)
    comp_first_card = computers_cards[0]
    computer_score = sum(computers_cards)  # important

    display()
    # first priority is to check if we got a blackjack
    if comp_first_card == cards[0] and computers_cards[1] == 10:
        print(f"Computer's cards: {computers_cards}, Computer's score: {computer_score}")
        print("Computer got a Blackjack. You lose 😭")
        break
    elif your_first_card == cards[0] and your_cards[1] == 10:
        display()
        print("You got a Blackjack. You win! 😁")
        break
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        # ^^^ This was the end of turn 1, which happens no matter what. From now on it will depend on
    if another_card == "y":
        your_cards.append(draw_card(your_score)) # this draws a third card for you. The player goes first which is a disadvantage since you can go bust first
        your_score = sum(your_cards)

    computers_cards.append(draw_card(computer_score)) #now let's draw a third card for computer. adding it to list.
    computer_score = sum(computers_cards) # now add that card's value to computer's score by re-sum

    #now we run our checks on the three cards
    if your_score > 21:
        game_end(your_cards, your_score, computers_cards, computer_score, "l")
        break
    elif computer_score > 21:
        game_end(your_cards, your_score, computers_cards, computer_score, "w")
        break
    display()
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    #if we say no, we let the computer continue drawing
    if another_card == "n":
        while computer_score < 16:
            computers_cards.append(draw_card(computer_score))
            computer_score = sum(computers_cards)
            if computer_score > 21:
                game_end(your_cards, your_score, computers_cards, computer_score, "w")
                break

        if your_score > computer_score:
            game_end(your_cards, your_score, computers_cards, computer_score, "w")
            break
        elif computer_score == your_score:
            game_end(your_cards, your_score, computers_cards, computer_score, "d")
            break
        else:
            game_end(your_cards, your_score, computers_cards, computer_score, "l")
            break
    else:
        your_cards.append(draw_card(your_score))  # this draws another card for you.
        your_score = sum(your_cards)

        computers_cards.append(draw_card(computer_score))  # now let's draw a third card for computer. adding it to list.
        computer_score = sum(computers_cards)  # now add that card's value to computer's score by re-sum
        display()
        if your_score > 21:
            game_end(your_cards, your_score, computers_cards, computer_score, "l")
            break
        elif computer_score > 21:
            game_end(your_cards, your_score, computers_cards, computer_score, "w")
            break

#to make it cleaner I would have a "check score" function that takes in the scores. would be much cleaner code. Will do it next time when I feel like it.
#I also realize there's no way to repeat the game without restructuring some of the code....but I also don't feel like doing that now. Will come back to it in later versions
