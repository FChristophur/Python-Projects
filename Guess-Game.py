#Creating a list
mylist = [' ','O',' ']

#Shuffling the list
from random import shuffle

def shuffled(mylist):
    shuffle(mylist)
    return mylist 

#Getting the user's input
def player():
    guess = ''
    while guess not in ['0','1','2']:
        guess = (input("Guess the number!!"))
        print('Enter number 0 or 1 or 2')
    return int(guess)

#check the result
def logic(mylist,Guess):
    if mylist[Guess] == 'O':
        print("Found it!")
        return (mylist)
    
    else:
        print("Oops, Try again!")
        print (mylist)

#Building the game!
print('Guess the "O"!!')

#the list
mylist = [' ','O',' ']

#assigning the shuffled list
shuffled_list = shuffled(mylist)

#getting the guess
while True:
    user_guess = player()
    if user_guess == True:
        print(mylist)
        break
    else:
        print(mylist)

#check the result
    result = logic(shuffled_list,user_guess)