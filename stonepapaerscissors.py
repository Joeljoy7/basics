lis=["rock","paper","scissors"]
import random
r_num=random.randint(0,3)
comp_guess=lis[r_num]
while True:

    user_guess = input("Enter rock/paper/scissors or quit").lower()

    if user_guess=="rock" and comp_guess=="scissors":
        print("YOU'VE WON>>>>")

    if user_guess=="paper" and comp_guess=="rock":
         print("you've won")

    if user_guess=="scissors" and comp_guess=="paper":
        print("you've won>>>")
    elif user_guess=="quit":
        print("see you soon")
        quit()
    else:
        print("you lose..")

    ch=input("DO you wanna exit or continue(exit/c)").split()
    if ch=="c":
        continue
    elif ch=="exit":
        print("thank you for playing with us..")
        break