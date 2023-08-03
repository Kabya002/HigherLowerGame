import art
import game_data as g
import clear
import random
print(art.logo)

end_of_game= False
score=0
while not end_of_game:
    a= random.randint(0,len(g.data)-1)
    b= random.randint(0,len(g.data)-1)
    if a!=b:
        x=g.data[a]
        y=g.data[b]
    
    A1= print(f"Compare A: {x['name']}, a {x['description']}, from {x['country']}.\n")
    print(art.vs)
    B1= print(f"\nCompare B: {y['name']}, a {y['description']}, from {y['country']}.\n")
    print(x['follower_count'])
    print(y['follower_count'])

    guess= input("Who has more followers? Type 'A' or 'B': ")
    countA= x['follower_count']
    countB= y['follower_count']
    
    if guess=='B' and countA > countB:
        print(f"Game Over.{x['name']} has {x['follower_count']} followers.Your score is {score}")
        end_of_game= False
    if guess=='A' and countA < countB:
        print(f"Game Over.{y['name']} has {y['follower_count']} followers. Your score is {score}")
        end_of_game= False

    if (guess=='A'and countA > countB) or  (guess=='B' and countA < countB):
        clear.clear()
        score+=1
    
            
           
    
