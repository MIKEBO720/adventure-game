#choose your own adventure but its my own version
#so for this game i the main story is you're running away from bandits and theres two path to escape left or right
#if you go right youll given two choices cross the bridge or go back and get killed by the bandits or cross the bridge meet a stranger the stranger offers you a salvation accept his offer or decline turns out it was jesus now your actions will have consquences he said will you come with me or decline and run across the bridge but end up being eaten by a lion or accept and teleport you to his kingdom

#if you choose left theres a lake either you swam or go around but it does have no end so you must swim and you will be eaten by an alligator
welcome=input("welcome to the game your objective is to meet your savior,click enter to continue ")
name=input("please type your name to enter the game: ")
print(f"welcome to the game {name}")
#now lets input the objective
objective=input("first objective,your objective is to escape from the bandits thats trying to rob and kill you,please click enter to continue ")

answer=input("are you ready to play yes/no? ").lower()
if answer=="no":
    quit 
else:
    print("lets go")



objective=input("now those two bandits are chasing you,you have reached the end of the city and you went to the deep forest and come across a two path ways left/right you choose! click enter to continue ")
answer=input("will you take the right path or the left path ").lower()

if answer=="left":
    answer=input("you came across a lake nested with crocodiles do you want to swim or head back ").lower()
    if answer  == "swim":
        print("you are eaten by a crocodile you lose you die ")
    elif answer == "head back":
        print("the bandits killed you and robbed all of you things you lose bye")
    else:
        print ("invalid options")
        quit 

elif answer == 'right':
    answer=input("you came across a bridge you cross and get to the end or nope ").lower()
    if answer=='nope':
        print("the bandits got you you die xd stupid")
    elif answer == "cross":
        print("you crossed the bridge but you met a stranger")
        answer=input("the stranger offers you to cross the bridge or accept his offer to come with him and jump from the bridge he said yes/no ")
        if answer =="yes":
            print(f"turns out it was jesus you agreed and he teleports you to his kingdom You wON THE GAME AND MET YOUR SAVIOR {name}")
            print("thanks for playing PRAISE THE LORD AMEN")
        elif answer=="no":
            print("you run to the edge of the bridge but you got eaten by the lion that was waiting and hiding at the end of the bridge you lose")

    else:
        print("invalid option")




