import random
import time

def choose_level():
    while True:
        level = input("Izvēlies līmeni, Easy, Normal, Hard: ").lower()
        if level == "easy":
            return random.randint(1, 10)
        elif level == "normal":
            return random.randint(1, 100)
        elif level == "hard":
            return random.randint(1, 1000)
        else:
            print("Nēesi izvēlējies līmeni. \nIzvēlies Easy, Normal, vai Hard.")

def get_guesses():
    guess1 = int(input("Spēlētājs 1, ievadi skaitli: "))
    guess2 = int(input("Spēlētājs 2, ievadi skaitli: "))
    return guess1, guess2

def winner(number, guess1, guess2):
    if guess1 == number:
        print("Malacis, Spēlētājs 1 uzminēja skaitli!")
        return
    elif guess2 == number:
        print("Malacis, Spēlētājs 2 uzminēja skaitli!")
        return
    
    win1 = abs(guess1 - number)
    win2 = abs(guess2 - number)
    print(f"Spēlētājs 1 = {win1}, Spēlētājs 2 = {win2}")
    time.sleep(2)
    print("Neviens no jums neuzminēja skaitli.")
    time.sleep(2)
    print("Domāju kurš uzvarēja...")
    time.sleep(4)

    if win1 < win2:
        print("Spēlētājs 1 uzvarēja!")
        print(f"Minētais cipars bija {number}, un tuvākā vērtība bija {guess1}.")
    elif win2 < win1:
        print("Spēlētājs 2 uzvarēja!")
        print(f"Minētais cipars bija {number}, un tuvākā vērtība bija {guess2}.")
    else:
        print("Draudzība uzvarēja!")
        print(f"Minētais cipars bija {number}.")

def main():
    number = choose_level()
    guess1, guess2 = get_guesses()
    winner(number, guess1, guess2)
    time.sleep(3)
    print("Paldies ka spēlēji!")

main()
