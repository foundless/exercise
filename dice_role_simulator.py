import random
from time import sleep


##welcome print for human understanding
print('Welcome to dice role simulator... \n')
sleep(2)
print('If you want to play with us, please choose one of the following options... \n')
sleep(2)
print('<Yes> if you want to play or  <No> if you dont want to play \n')

#defining global variable for control the loop
total = 0

#defining counter for loop control
def count():
    global total
    total +=1
    return total
#defining func for case then wrong input entered
def count_neg():
    global total
    total =0
    return total

#list of valid entries for human inputs
positive = [1, 'Yes','YES','yes','y']
negative = [0, 'No','NO','no', 'n']

#def main function for easy add of some unit tests,
#or to use functions or classes from other modules
def main():
    while True:
        #start of human interacting
        if total == 0:
            user = (input('Do you want to start ? \n'))
        
        sleep(2)
        # first loop
        if total == 0 and user in positive:
            print('Ok. Alea Iacta Est')
            sleep(2)
            print('Spinning...')
            sleep(1)
            print('.')
            sleep(1)
            print('...')
            sleep(1)
            print('......')
            sleep(1)
            number = random.randint(1,6)        
            print('You got number ',number, ' !!! ')
            sleep(2)
            print('Bravo !!! ')
            sleep(1)
            restart  = input('Do you want to try again ? \n')
            sleep(1)
            if restart in positive:
                count()
                continue
            elif restart in negative:
                print('Thank you for your time, see ya later aligater ...')
                break
            else:
                print('You havent specified yes or no, can you please try again ? ')
                count_neg()
                continue

        #second loop
        elif total > 0 and user in positive:
            sleep(1)
            print('Ok. Alea Iacta Est')
            sleep(2)
            print('Spinning ...')
            sleep(1)
            print('.')
            sleep(1)
            print('...')
            sleep(1)
            print('......')
            number = random.randint(1,6)
            print('You got number ',number, ' !!! ')
            sleep(1)
            
            print('Bravoo !! ')
            sleep(1)
            restart2  = input('Do you want to try again ? \n')
            if restart2 in positive:
                count()
                continue
            elif restart2 in negative:
                print('Thank you for your game, see ya later aligater ...')
                break
            else:
                print('You havent specified yes or no, can you please try again ? ')
                count_neg()
                continue

        #third case loop            
        elif total > 0 and user in negative or total == 0 and user in negative:
            sleep(1)
            print('Thank you for your game, see ya later aligater ...')
            break
        else:
            print('You havent specified yes or no, can you please try again ? ')
            count_neg()
            continue

#calling the main function to start the program
if __name__ == "__main__":
    main()
        

