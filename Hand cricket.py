import random 
sides=["odd","even"]
after_toss=["bat","bowl"]
runs=[1,2,3,4,5,6,0]
again='y'
user_score=[]
comp_score=[]
batting_or_bowling=['bat','bowl']
totalscore_user=0
totalscore_comp=0
toss=input("Choose odd or even:").lower()
toss_num_user=int(input("Enter a number for toss (0 to 6):"))
toss_num_comp=random.choice(runs)
print("Computer's number for toss:",toss_num_comp)
toss_decision=toss_num_user + toss_num_comp

if toss_decision%2==0:
    print("You have won the tosss!!!")
    user_choice=input("You choose to Bowl or Bat first :").lower()
else:
    print("Sorry you lost the toss!")

def game():
    run_batting=int(input("Enter your run:"))
    ball_batting=random.choice(runs)
    print("The number bowled by computer:",ball_batting)
    return run_batting,ball_batting

def batting(target):
    
    while(1):
        user_run,comp_ball=game()
        if user_run == comp_ball:
            print("You're out!")
            print("Your final score:",totalscore_user)
            break
        else:
            user_score.append(user_run)
            totalscore_user=sum(user_score)
            print("Your run:",totalscore_user)
            if totalscore_user==target:
                print("You've successfully chased")

def comp_game():
    ball_batting=random.choice(runs)
    print("The number by computer:",ball_batting)
    run_batting=int(input("Enter opposing number:"))
    return run_batting,ball_batting

def bowling(target):
    
    while(1):
        user_run,comp_ball=comp_game()
        if user_run == comp_ball:
            print("You got a wicket !")
            print("Your final score:",totalscore_comp)
            break
        else:
            comp_score.append(user_run)
            totalscore_comp=sum(user_score)
            print("Computer's final score:",totalscore_comp)
            if totalscore_comp==target:
                print("Computer have chased the target")


if user_choice == "bat":
    batting()
    target=sum(totalscore_user)+1
    print("It is ur turn to bowl!")
    bowling(target)
else:
    bowling()
    target=sum(totalscore_comp)+1
    print("It is your turn to bat!")
    batting(target)

if totalscore_user<totalscore_comp:
    print("Sorryy! You've lost!")
elif totalscore_user==totalscore_comp:
    print("It's a draw!")
else:
    print("Congrats! You've won!!!")


again=input("Do you wanna play again y/n:")

