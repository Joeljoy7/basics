import random as rd

print("WELCOME TO RANDOM NUMBER GUESSING GAME>>")
ch=input("\n1.PLAY THE GAME(play)\n2.EXIT THE GAME(exit)")
if ch.lower()=="exit" or ch=="2":
    print("SEE YOU SOON>>>>>>")
    quit()


n = int(input("enter the limit of guess.\n"))
comp_guess = rd.randint(0, n)

while ch=='1' or ch.lower=='play':

    user_guess=int(input("Enter your guess..(numbers only) or quit(q)"))
    if user_guess not in range(n):
        print("!!!!!!!!!!Enter numbers in given range only!!!!!!\n")
        continue
    elif user_guess ==comp_guess:
        print("CONGOOO..YOU'VE WON>>\n")
        c= input("DO YOU WANNA CONTINUE(continue)/ OR QUIT (quit)\n")
        if c.lower()=="c":
            continue
        elif c.lower()=="quit":
            print("THANK YOU FOR JOINING ")
            break
    elif user_guess!=comp_guess:
        print("SO CLOSE>>>\n")
        c = input("DO YOU WANNA CONTINUE(c)/ OR QUIT (quit)\n")
        if c.lower() == "c":
            continue
        elif c.lower() == "quit":
            print("THANK YOU FOR JOINING ")
            break
