from random import randint

print('Welcome to the Number Guessing Game!')
print("I'm thinking  of a number  between 1 and 100")

hard_attempt=10
easy_attempt=5
def levels():
    level=input("choose a difficulty.Type 'easy' or 'hard'" )
    if level=='easy': 
        return hard_attempt
    else:  
        return easy_attempt
    


answer=randint(1,100)
print(answer)
attempt=levels()
def play(attempt):
 
    while attempt>0:
        attempt-=1
        guess=int(input('Make a guess '))
        if guess==answer:
            print(f'you win .{attempt} attempts')
            attempt=0
        elif guess>answer:
            print(f'Too high .{attempt} attempts')
        elif guess<answer:
            print(f'Too Low .{attempt} attempts')
play(attempt)

while input("Do You went to  play again ? Type 'Y' or 'N' ") =='y':
   
    play(attempt)