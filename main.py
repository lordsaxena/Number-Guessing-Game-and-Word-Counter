import random
from collections import Counter
def guessing_game():
    levels={"1":(10,4),"2":(50,7),"3":(100,10)}
    print("1. Easy (1-10)\n2. Medium (1-50)\n3. Hard (1-100)")
    level=input("Pick a level: ").strip()
    if level not in levels:
        level="2"
    high,chances=levels[level]
    secret=random.randint(1,high)
    print(f"I'm thinking of a number between 1 and {high}. You have {chances} tries.")
    for attempt in range(1,chances+1):
        try:
            guess=int(input(f"Guess {attempt}: "))
        except ValueError:
            print("That's not a number, you lost a try.")
            continue
        if guess==secret:
            print(f"Correct! You got it in {attempt} tries.")
            return
        print("Too low." if guess<secret else "Too high.")
    print(f"Out of tries. The number was {secret}.")
def word_counter():
    path=input("Enter the file path: ").strip()
    try:
        with open(path,"r",encoding="utf-8") as f:
            text=f.read()
    except FileNotFoundError:
        print("File not found.")
        return
    words=[w.strip(".,!?;:\"'()[]{}-").lower() for w in text.split()]
    words=[w for w in words if w]
    print("Total words:",len(words))
    print("Unique words:",len(set(words)))
    print("Lines:",len(text.splitlines()))
    print("Characters:",len(text))
    print("Top 5 words:")
    for word,count in Counter(words).most_common(5):
        print(f"  {word}: {count}")
def main():
    while True:
        print("\n--- Game & Word Counter ---")
        print("1. Number Guessing Game\n2. Word Counter\n3. Exit")
        choice=input("Choose: ").strip()
        if choice=="1":
            guessing_game()
        elif choice=="2":
            word_counter()
        elif choice=="3":
            break
        else:
            print("Invalid option.")
main()
