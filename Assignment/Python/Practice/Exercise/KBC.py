import random as r

q = [
    {
        "question": "\n-> What is the chemical symbol for water?\n A. H2O \t B. CO2\n C. NaCl\t D. O2",
        "answer": "a"
    },
    {
        "question": "\n-> What is the capital city of France?\n A. Rome\t B. Berlin\n C. Paris\t D. Madrid",
        "answer": "c"
    },
    {
        "question": "\n-> Who is known as the 'Father of the Nation' in India?\n A. Jawaharlal Nehru\t B. Mahatma Gandhi\n C. Sardar Patel\t D. Subhas Chandra Bos",
        "answer": "b"
    },
    {
        "question": "\n-> Who wrote the famous Harry Potter series?\n A. J.R.R. Tolkien\t B. George R.R. Martin\n C. J.K. Rowling\t D. C.S. Lewis",
        "answer": "c"
    },
    {
        "question": "\n-> Who was the first woman Prime Minister of India?\n A. Indira Gandhi\t B. Sarojini Naidu\n C. Pratibha Patil\t D. Sushma Swaraj",
        "answer": "a"
    },
    {
        "question": "\n-> Which planet is known as the 'Red Planet'?\n A. Earth\t B. Mars\n C. Jupiter\t D. Saturn",
        "answer": "b"
    },
    {
        "question": "\n-> Who invented the telephone?\n A. Alexander Graham Bell\t B. Thomas Edison\n C. Nikola Tesla\t D. Albert Einstein",
        "answer": "a"
    },
    {
        "question": "\n-> Which continent is known as the 'Dark Continent'?\n A. Africa\t B. Asia\n C. South America\t D. Antarctica",
        "answer": "a"
    },
    {
        "question": "\n-> What is the national sport of Japan?\n A. Football\t B. Sumo Wrestling\n C. Cricket\t D. Baseball",
        "answer": "b"
    },
    {
        "question": "\n-> What is the hardest natural substance on Earth?\n A. Gold\t B. Iron\n C. Diamond\t D. Silver",
        "answer": "c"
    }
]

w = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]


print("\n------------------------ KBC ------------------------\n")

print("-> Instructions: ")
print("1. Press 's' for Start The Game.")
print("2. Press 'q' While Ansering The Question to Quit The Game.")

ch = input("\nEnter Your Choice: ").lower()

if ch == 'q':
    print("-> Exited.")

elif ch == 's':
    r.shuffle(q)

    for i in range(len(q)):
        print(f"\n\nThe {i+1}th Que for {w[i]}rs: \n{q[i]['question']}")
        ans = input("Enter ans: ").lower()

        if ans == q[i]['answer']:
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




