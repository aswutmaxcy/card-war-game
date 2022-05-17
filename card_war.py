import random

deck1 = [str(i) + "H" for i in range(2,15)]
deck2 = [str(i) + "D" for i in range(2,15)]
deck3 = [str(i) + "C" for i in range(2,15)]
deck4 = [str(i) + "S" for i in range(2,15)]
deck = deck1 + deck2 + deck3 + deck4
plyrDeck = []
cpuDeck = []
# print(deck)
random.shuffle(deck)
plyrDeck = deck[0:26]
cpuDeck = deck[26:]
# print(len(plyrDeck))
# print(len(cpuDeck))

while True:
    choice = input("Would you like to go to war? Y/N? ")
    choice = choice.lower()
    if choice == "y":
        print("===Here's your deck===\n", plyrDeck)
        print("\n======CPU's deck======", "\n", cpuDeck)
        break
    elif choice == "n":
        break
    else:
        print('Please choose "y" or "n"')

def war(p_card, cpu_card):
    print("\n This means war!")
    if len(plyrDeck) < 4 or len(cpuDeck) < 4:
        return too_few_cards(p_card, cpu_card)
    cpu = cpuDeck.pop(3)
    plyr = plyrDeck.pop(3)
    print("Your war card:", plyr,"\nCPUs war card:", cpu)
    if int(cpu[:-1]) > int(plyr[:-1]):        
        cpuDeck.append(cpu)
        cpuDeck.append(plyr)
        x = 0
        while x <= 2:
            win = plyrDeck.pop(0)
            cpuDeck.append(win)
            x+=1
        cpuDeck.append(cpu_card)
        cpuDeck.append(p_card)
        print("CPU wins", cpuDeck[-5:-2], plyr, p_card)
    elif int(cpu[:-1]) < int(plyr[:-1]):
        plyrDeck.append(plyr)        
        plyrDeck.append(cpu)
        x = 0
        while x <= 2:
            win = cpuDeck.pop(0)
            plyrDeck.append(win)
            x+=1
        plyrDeck.append(cpu_card)
        plyrDeck.append(p_card)
        print("You won", plyrDeck[-5:-2], cpu, cpu_card)
    elif int(cpu[:-1]) == int(plyr[:-1]):
        print("2nd war is being called")
        stash = []
        stash.append(p_card)
        stash.append(cpu_card)
        stash.append(cpu)
        stash.append(plyr)
        if len(plyrDeck) > 7 or len(cpuDeck):
            too_few_cards(p_card, cpu_card)
        p2_card = plyrDeck.pop(6)
        cpu2_card = cpuDeck.pop(6)
        print("2nd War\nYour card:",p2_card,"\nCPUs card:",cpu2_card)
        if int(p2_card[:-1]) > int(cpu2_card[:-1]):
            stash.append(p2_card)
            stash.append(cpu2_card)
            x = 0
            while x <= 6:
                stash.append(cpuDeck.pop(0))
                x+=1
            print("You won the 2nd war! Here's your spoils:", stash)
            plyrDeck.extend(stash)
        elif int(p2_card[:-1]) < int(cpu2_card[:-1]):
            stash.append(p2_card)
            stash.append(cpu2_card)
            x = 0
            while x <= 7:
                stash.append(plyrDeck.pop(0))
                x+=1
            print("You lost the 2nd war! Here's your losses:", stash)
            cpuDeck.extend(stash)

def too_few_cards(p_card, cpu_card):
    stash = []
    stash.append(p_card)
    stash.append(cpu_card)
    if plyrDeck == []:
        cpuDeck.append(p_card)
        cpuDeck.append(cpu_card)
        print("You don't have enough cards to war, you have lost. CPU wins!\n CPUs Cards:", cpuDeck)
    elif cpuDeck == []:
        plyrDeck.append(p_card)
        plyrDeck.append(cpu_card)
        print("CPU doesn't have enough cards to war, CPU loses, You win!\n Your Cards:",plyrDeck)
    elif len(plyrDeck) < 4 or len(plyrDeck) < 7:
        x=0
        while x < int(len(plyrDeck)):
            win = plyrDeck.pop(x)
            cpuDeck.append(win)
            x+=1
        cpuDeck.extend(stash)
        print("You don't have enough cards to war, you have lost. CPU wins!\n CPUs Cards:", cpuDeck)
    elif len(cpuDeck) < 4 or len(cpuDeck) < 7:
        x=0
        while x < int(len(cpuDeck)):
            win = cpuDeck.pop(x)
            plyrDeck.append(win)
            x+=1
        plyrDeck.extend(stash)
        print("CPU doesn't have enough cards to war, CPU loses, You win!\n Your Cards:", plyrDeck)
                      
def roundWinner(p_card, cpu_card):
    if int(p_card[:-1]) > int(cpu_card[:-1]):
        plyrDeck.append(cpu_card)
        plyrDeck.append(p_card)
        print("You won", cpu_card)
    elif int(p_card[:-1]) < int(cpu_card[:-1]):
        cpuDeck.append(p_card)
        cpuDeck.append(cpu_card)
        print("CPU wins", p_card)
    elif int(p_card[:-1]) == int(cpu_card[:-1]):
        war(p_card, cpu_card)

rndCounter = 1
while True:
    # This was a debugging tool to check if I was losing cards somewhere
    if len(plyrDeck) + len(cpuDeck) != 52:
        print("\nSOMETHING IS WRONG!\n\nSOMETHING IS WRONG!\n\nSOMETHING IS WRONG!\n\nSOMETHING IS WRONG!\n\nSOMETHING IS WRONG!\n\nSOMETHING IS WRONG!\n\nSOMETHING IS WRONG!\n")
    if plyrDeck == []:
        print("You have Lost. CPU Wins!")
        break
    elif cpuDeck == []:
        print("You have Won. CPU Loses!")
        break
    print("\nWelcome to War, round",rndCounter)
    nround = input('Press "Enter" for next round or "n" to quit: ')
    nround.lower()
    if nround == "":
        p_card = plyrDeck.pop(0)
        cpu_card = cpuDeck.pop(0)
        print("Your Card:", p_card, "\nCPUs card:",cpu_card)
        roundWinner(p_card, cpu_card)
        rndCounter += 1
        print("===Here's your deck===\n", plyrDeck)
        print("\n", "===This is the CPU's deck===", "\n", cpuDeck)
    elif nround == "n":
        break
    else:
        print('Choose "Enter" or "n": ')


#pygame implementation
#too few cards to declare war means you lose
#classes to clean up append
#tie in war need to repeat the war function correctly, for more than two wars

#class card
#   holds atrributes of a suite, value (but then do you have to create a class for each value?)
#   method is that it goes to war it it's equal to another (another card of the same value class?)
        #then I need to make 13 classes, matching them and pulled a war method build into each when equal
        #you'd individually assign 52 cards? No, you'd assign 13 classes to 4 suites of cards?
            #with classes you could assign value to the actual card names, Jack, Queen, King, Ace
            #solves multiple war issues? 
            # it's a check of position in the deck, use a parameter to denote the card position pulled.
            # or pull 4 cards each time and include the "too few cards" function, use the 4 card as the comparative
            # you can only have 5 wars total in a perfect senario where each player has 26 cards           
            #     ---how can you make this infinite? multiple n by 4

            
