# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. 

#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D
import random as r

ch = ["Snake", "Water", "Gun"]

def play(com, p):
    if (com == 0 and p == 0) or (com == 1 and p == 1) or (com == 2 and p == 2):
        print("\n-> Match Draw!")
        return 0  # Draw
    elif (com == 0 and p == 1) or (com == 1 and p == 2) or (com == 2 and p == 0):
        print("\n-> You Lose, Better Luck Next Time!")
        return -1  # Computer wins
    else:
        print("\n-> You Win!")
        return 1  # Player wins

print("\n------------------------- Welcome to Snake - Water - Gun Game: ------------------------- \n")
print("Instruction:  0 for Snake \t 1 for Water \t 2 for Gun\n")

name = input("Enter your name: ")
mode = int(input("Choose Mode: 1 For No-Score Game \t 2 For Score-Based Game: "))

if mode == 1:
    print("Press '3' to exit the game anytime.")

    while True:
        print("--------------------------------------------------------")
        p = int(input("Enter Your choice: "))
        
        if p == 3:
            print("\n-> Exiting game. Goodbye!")
            break
        elif p not in [0, 1, 2]:
            print("\n-> Invalid choice. Please enter 0, 1, 2, or 3 to exit.")
            continue

        com = r.randint(0, 2)
        print(f"\n-> You Selected {ch[p]}")
        print(f"-> Computer Selected {ch[com]}")
        play(com, p)

elif mode == 2:
    print("\nThere are 5 rounds. Try to score higher than the computer!")
    com_score = 0
    p_score = 0

    for i in range(5):
        print("--------------------------------------------------------")
        p = int(input("\nEnter Your choice: "))

        if p not in [0, 1, 2]:
            print("\n-> Invalid choice. Please enter 0, 1, or 2.")
            continue

        com = r.randint(0, 2)
        print(f"\n-> You Selected {ch[p]}")
        print(f"-> Computer Selected {ch[com]}")

        result = play(com, p)
        
        if result == 1:
            p_score += 1
        elif result == -1:
            com_score += 1

    print(f"\n\nFinal Scores: {name} - {p_score} | Computer - {com_score}")
    if p_score > com_score:
        print(f"\n-> Congratulations {name}, You Win the Game!")
    elif p_score < com_score:
        print(f"\n-> Computer Wins the Game. Better Luck Next Time.")
    else:
        print("\n-> It's a Tie!")

else:
    print("\n-> Enter a valid mode choice.")
