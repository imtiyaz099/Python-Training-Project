import random

# Rock
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# Paper
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
print()
wel='''----------------------------------------------------------------------------------------------------------------------------
---------------------------------------|WELCOME TO IMTIYAZ'S ROCK PAPER SCISSORS GAME|--------------------------------------
----------------------------------------------------------------------------------------------------------------------------'''
print(wel)

user_score=0
computer_score=0
ro=0
t=1

user_name=input("Please Enter Your Name To Play The Game : ")
user_name=user_name.capitalize()

while(t==1):

    

    ro=ro+1
    # print()
    print("--------------------------------------------------------- ROUND -",ro,"-------------------------------------------------------")
    

    def print_score():
        print("\n",user_name+"'s Score : ",user_score,end="\t")
        print("Computer's Score : ",computer_score)

    def user_score_track(user_score):
        if user_score==0:
            user_score=1
            return user_score
        else:
            user_score+=1
            return user_score
    
    def computer_score_track(computer_score):
        if computer_score==0:
            computer_score=1
            return computer_score
        else:
            computer_score+=1
            return computer_score

    print()
    print("Enter Your Choice ",user_name," : Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors.  ")

    user_choice=int(input())

    if user_choice >2 or user_choice<0:
        print("You Entered a Invalid Option, You Loose.")
        print()
        
    else :

        print(game_images[user_choice])
        
        computer_choice=random.randint(0,2)
        print("Computer's Choice :\n",computer_choice)

        print(game_images[computer_choice])
        
        if computer_choice == user_choice:
            print("Result : It's a Draw....")

            print_score()

            
        elif computer_choice == 0 and user_choice ==2 :

            computer_score=computer_score_track(computer_score)

            print("Result : You Lost....",end="")
            print(" Better Luck Next Time....")

            print_score()
            
        elif user_choice ==0 and computer_choice == 2 :

            user_score=user_score_track(user_score)

            print("Result : You Win....")

            print_score()
            
        elif computer_choice > user_choice :

            computer_score=computer_score_track(computer_score)

            print("Result : You Lost....",end="")
            print(" Better Luck Next Time....")

            print_score()
 
        elif computer_choice < user_choice :

            user_score=user_score_track(user_score)

            print("Result : You Win....")

            print_score()

        print()
    x=int(input("Please Enter 1 to Play Again or 0 to exit : "))
    t=x
    # print()
    if x>1 or x<0:
        print("\nOops!! You Entered a wrong choice You Are Out of the Game.")
    print()

print("It was a wonderful Experience playing with You",user_name,".")
print()