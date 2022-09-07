from random import randint
pc_choice = randint(1,100) # I imported this

playing = True

while playing:
  user_choice = int(input("Choose number 1-100 == "))
  if user_choice == pc_choice:
    print("You won !")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")
