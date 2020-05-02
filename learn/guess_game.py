my_word = "Girish"
guess =""
guess_count=0
guess_limit=3
out_of_guess= False
while guess!= my_word and not(out_of_guess):
    if guess_count < guess_limit:
       guess = input("Enter the name:")
       guess_count+= 1
    else:
       out_of_guess= True
if out_of_guess:
    print("YOU LOSE!")
else :
    print("you win !")