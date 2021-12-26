import random


def rps():
    options = ['rock' , 'paper' , 'scissors']
    rounds = 1
    pc_rounds_win = 0
    user_rounds_win = 0
    a = 'y'
    rounds_equal = 0

    while a == 'y':
        user_wins = 0
        pc_wins = 0
        reps = 0
        while reps < 3:    
            pc = random.choice(options)
            user = input('enter, rock  paper or scissors:\n').lower()
            value = True

            if pc == 'scissors' and user == 'paper':
                pc_wins += 1
                print(f'pc won with the {pc}')

            elif pc == 'scissors' and user == 'rock':
                user_wins += 1
                print(f'you won, pc had {pc}')

            elif pc == 'paper' and user == 'scissors':
                user_wins +=1
                print(f'you won, pc had {pc}')

            elif pc == 'paper' and user == 'rock':
                pc_wins += 1
                print(f'pc won with the {pc}')

            elif pc == 'rock' and user == 'scissors':
                pc_wins += 1
                print(f'pc won with the {pc}')
            
            elif pc == 'rock' and user == 'paper':
                user_wins += 1
                print(f'you won, pc had {pc}')

            elif pc == user:
                print(f'both {pc} , eaquals')     

            else:
                print(pc,user)
                print('wrong value')
                value = False

            if value == True:
                reps += 1

            print(f'pc : {pc_wins} , you {user_wins}')

        rounds += 1                  

        if user_wins > pc_wins:
            winner = 'you'
            user_rounds_win += 1
            print(winner + ' won this round')

        elif user_wins < pc_wins:
            winner = 'pc'
            pc_rounds_win += 1
            print(winner + ' won this round')

        elif user_wins == pc_wins:
            rounds_equal += 1
            print('equal')
            print('no winners this round')

    

        while True:
            a = input('you wanna go another round? y/n\n')
            if a == 'y':
                print(f'round {rounds} started')
                break
            elif a == 'n':
                print('ok bye bye')
                break
            else:
                print('wrong value, please enter y for yes or n for no')

    print(f'rounds played : {rounds - 1}')
    print(f'pc rounds won : {pc_rounds_win}')
    print(f'user rounds won : {user_rounds_win}')
    print(f'rounds equal : {rounds_equal}')           

rps()    