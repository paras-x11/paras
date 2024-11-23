import random

q = ["\n-> 1. What is the chemical symbol for water?\n A. H2O \t B. CO2\n C. NaCl\t D. O2",
     "\n-> 2. What is the capital city of France?\n A. Rome\t B. Berlin\n C. Paris\t D. Madrid",
     "\n-> 3. Who is known as the 'Father of the Nation' in India?\n A. Jawaharlal Nehru\t B. Mahatma Gandhi\n C. Sardar Patel\t D. Subhas Chandra Bos",
     "\n-> 4. Who wrote the famous Harry Potter series?\n A. J.R.R. Tolkien\t B. George R.R. Martin\n C. J.K. Rowling\t D. C.S. Lewis",
     "\n-> 5. Who was the first woman Prime Minister of India?\n A. Indira Gandhi\t B. Sarojini Naidu\n C. Pratibha Patil\t D. Sushma Swaraj",
     "\n-> 6. Which planet is known as the 'Red Planet'?\n A. Earth\t B. Mars\n C. Jupiter\t D. Saturn",
     "\n-> 7. Who invented the telephone?\n A. Alexander Graham Bell\t B. Thomas Edison\n C. Nikola Tesla\t D. Albert Einstein",
     "\n-> 8. Which continent is known as the 'Dark Continent'?\n A. Africa\t B. Asia\n C. South America\t D. Antarctica",
     "\n-> 9. What is the national sport of Japan?\n A. Football\t B. Sumo Wrestling\n C. Cricket\t D. Baseball",
     "\n-> 10. What is the hardest natural substance on Earth?\n A. Gold\t B. Iron\n C. Diamond\t D. Silve",
]

a = ['a', 'c', 'b', 'c', 'a', 'b', 'a', 'a', 'b', 'c']

w = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

print("\n------------------------ KBC ------------------------\n")

print("-> Instructions: ")
print("1. Press 's' for Start The Game.")
print("2. Press 'q' While Ansering The Question to Quit The Game.")

ch = input("\nEnter Your Choice: ").lower()

if ch == 'q':
    print("-> Exited.")

elif ch == 's':
    for i in range(len(q)):
        print(f"\n\nThe {i+1}th Que for {w[i]}rs: \n{q[i]}")
        ans = input("Enter ans: ").lower()

        if ans == a[i]:
            print("\n-> Correct Answer.")
            print(f"-> You Win {w[i]} rs.")

        elif ans == 'q':
            print("\n-> Quit.")
            if i > 0:
                print(f"\n\n--> Congratulations, You Got {w[i-1]} rs.")
            break
        
        else:
            print("\n-> Wrong Answer, Better Luck Next Time!")
            if i > 0:
                print(f"\n\n--> Congratulations, You Got {w[i-1]} rs.")
            break

else:
    print("-> Invalid Choice.")




