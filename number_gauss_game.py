# from random import randint

# print('Welcome to the Number Guessing Game!')
# print("I'm thinking  of a number  between 1 and 100")
# level=input("choose a difficulty.Type 'easy' or 'hard'" )
# hard_attempt=10
# easy_attempt=5
# def levels(level):
#     if level=='easy': 
#         return hard_attempt
#     else:  
#         return easy_attempt
    
# attempt=levels(level)

# answer=randint(1,100)
# def play():
    
#     global attempt
#     while attempt>0:
#         attempt-=1
#         guess=int(input('Make a guess '))
#         if guess==answer:
#             print(f'you win .{attempt} attempts')
#         elif guess>answer:
#             print(f'Too high .{attempt} attempts')
#         elif guess<answer:
#             print(f'Too Low .{attempt} attempts')
# play()
# play_again=input("Do You went to  play again ? Type 'Y' or 'N' ")
# while play_again=='y':
#     play()