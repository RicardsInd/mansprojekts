# Spēle ciparu minēšana
import random
import time

Choose = input("Izvēlies līmeni, Easy, Normal, Hard: ")
if Choose == "Easy".lower():
    Number = random.randint(1,10)

elif Choose == "Normal".lower():
    Number = random.randint(1,100)
    
elif Choose == "Hard".lower():
    Number = random.randint(1,1000)

else:
    print("Nēesi izvēlējies līmeni.\nEasy, Normal, Hard")

Guess1 = int(input("Ievadi skaitli: "))
if Guess1 == Number:
    print("Malacis tu uzminēji to skaitli")
    exit()

Guess2 = int(input("Ievadi skaitli: "))
if Guess2 == Number:
   print("Malacis tu uzminēji to skaitli")
   exit()

win1 = abs(Guess1-Number)
win2 = abs(Guess2-Number)

print({win1},{win2})

print("Neviens no jums neuzminēja skaitli.")
time.sleep(2)
print("Domāju kurš uzvarēja...")
time.sleep(4)

if win1>win2:
    print(f"Spēlētājs 1. Uzvarēja!")
    time.sleep(2)
    print(f"Minētais cipars bija {Number}, un uzvērētājs ievadija {Guess1}")
    
elif win2>win1:
    print(f"Spēlētājs 2. Uzvarēja!")
    time.sleep(2)
    print(f"Minētais cipars bija {Number}, un uzvērētājs ievadija {Guess2}")

else:
    print("Draudzība uzvarēja!")
    print(f"Minētais cipars bija {Number}!")

time.sleep(5)
print("Paldies ka spēlēji!")