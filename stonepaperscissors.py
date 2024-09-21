import random

# Displaying Rules
print("We are starting the Stone Paper & Scissors game .")
input()
print("Whoever gets 5 points first wins this game.")



# Creating the game function here
player1 = 0
comp_score = 0
while player1 < 5 and comp_score < 5:
    print("Choose one of the following ")
    list = ["Stone", "Paper", "Scissors"]
    for i in range(len(list)): print(list[i])
    inp = int(input("Type 1 for Stone, 2 for Paper and 3 for Scissors : "))
    comp = random.choice(list)
    print(f"You have chosen {list[inp-1]}")
    print("Computer has chosen", comp)
    input()
    if comp == list[inp-1] :
        print("The game is Draw")
    elif (inp == 1 and comp == "Scissors") or (inp == 2 and comp == "Stone") or (inp == 3 and comp == "Paper"):  
        print("Well done, You have won this round.")
        player1 += 1
    elif (inp == 2 and comp == "Scissors") or (inp == 3 and comp == "Stone") or (inp == 1 and comp == "Paper"):
        print("Oh no!!!, You have lost, Computer has won this round.") 
        comp_score += 1
    print("Player Score :", player1)
    print("Computer Score :", comp_score)
    input()
    if player1<5 and comp_score<5 : print("Moving on to the Next Round")

    # Checking Who Won
if player1 == 5: print("Congratulations, You have won the game")
else: print("Player 2 wins")

