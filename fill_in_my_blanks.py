''' Fill In The Blanks
This game will allow a user to select a game difficulty level, a number of
 maximum attempts, and then provide the user with a block of text with
several blank words that they must guess to fill in.

Written by: Louis Magdaleno
Date: 4/23/2018
'''

import sys


def play_game():
    '''play fill in the blank.'''

    attempts = 1
    difficulty = 'easy'
    alive = True
    madlibs = {
        'easy': '''Dr. (__1__) is best known for his books \nThe (__2__)
            in the (__3__) and How the \n(__4__) stole (__5__).''',
        'medium': '''(__1__) is a (__2__) typed language. It utilizes an\n
            (__3__) instead of a compiler. \nThe kind of snake in its\n
            logo represents the name of the (__4__).\nIt is a very (__5__)
            language to type.''',
        'hard': '''Jurassic (__1__) was a 1993 movie about (__2__).\n
            The plot of the movie was about a dinosaur (__3__) park
            gone wrong. The final scene pitting a T (__4__)-rex\n
            against veloci(__5__) was very cool.'''}
    easy_answers = {
        '(__1__)': 'seuss',
        '(__2__)': 'cat',
        '(__3__)': 'hat',
        '(__4__)': 'grinch',
        '(__5__)': 'christmas',
        }
    medium_answers = {
        '(__1__)': 'python',
        '(__2__)': 'dynamically',
        '(__3__)': 'interpreter',
        '(__4__)': 'language',
        '(__5__)': 'easy',
        }
    hard_answers = {
        '(__1__)': 'park',
        '(__2__)': 'dinosaurs',
        '(__3__)': 'park',
        '(__4__)': 't',
        '(__5__)': 'raptor',
        }

    display_welcome()
    difficulty = get_difficulty(madlibs)
    attempts = int(get_attempts())
    display_madlib(difficulty, madlibs)
    answer_dict = difficulty + '_answers'
    win_condition = int(5)
    correct = int(0)
    blank_start = 1
    blank_end = 6
    for i in range(blank_start, blank_end):
        current_blank = '(__' + str(i) + '__)'
        answer = get_answer(current_blank)
        if check_answer(answer, current_blank, easy_answers):
            print('Correct!')
            madlibs[difficulty] = update_madlib(madlibs, difficulty,
                                                current_blank, answer)
            display_madlib(difficulty, madlibs)
            correct += 1
            if correct == win_condition:
                game_won()
        else:
            while not check_answer(answer, current_blank, easy_answers):
                print('Incorrect!')
                attempts = update_attempts(attempts)
                if dead(attempts):
                    print('You are out of attempts. Nice Try!')
                    if play_again() == 'yes':
                        play_game()
                    else:
                        sys.exit('Good bye')
                answer = get_answer(current_blank)


def game_won():
    '''Congratulate player for winning the game.'''

    print('Congratulations! You have won!')
    if play_again() == 'yes':
        play_game()
    else:
        print('Good bye!')


def print_stars():
    '''Print stars across the screen.'''

    banner_length = 30
    print('*' * banner_length)


def display_welcome():
    '''Display welcome message to user.'''

    print_stars()
    print('')
    print('Fill in the Blank V1.0')
    print('''A simple game where you select a difficulty level \n
        and a number of guesses to fill in a blank.''')
    print ('''You will then be presented with a text passage containing several
        missing words.\nYou will be asked to enter a word that fills in
        a missing word. \nFill all the blanks to win!''')
    print_stars()


def get_difficulty(madlibs):
    '''Prompt user to enter difficulty level. Return difficulty level as str.


    Keyword Arguments:
    madlibs - dictionary containing valid difficulty levels as keys
    '''

    diff = input('''Please select a game difficulty level.\n
        Enter easy, medium, or hard.\n''').lower()
    while diff not in madlibs.keys():
        diff = input('Enter easy, medium, or hard.\n').lower()
    return diff


def get_attempts():
    '''Prompt user to enter number of attempts. Return int > 0.'''

    attempts = input('''How many attempts would you like?\n
        Enter a number greater than zero.\n''')
    while attempts.isdigit() is False and int(attempts) <= 0:
        attempts = input('Enter a number greater than zero.\n')
    print('Okay! You will have ', attempts,
          ' attempts to solve this challenge.')
    return attempts


def dead(att):
    '''Check if dead or alive based on number of attempts left.
    Return bool, True if alive and False is dead.

    Keyword Arguments:
    att - number of attempts as int
    '''

    if att == 0:
        return True
    else:
        return False


def display_madlib(diff, lib_dict):
    '''Dislpay madlib based on difficulty level.

    Keyword Arguments:
    diff - difficulty level as string
    lib_dict - madLib dictionary
    '''

    print_stars()
    print(lib_dict[diff])
    print('')


def get_answer(blank):
    '''Prompt user to enter answer to blanks. Return answer as str.

    Keyword Arguments:
    blank - the blank word the user is trying to solve, ie (__1__)
    '''

    answer = input('What goes in ' + str(blank) + ' ?\n').lower()
    return answer


def check_answer(ans, blank, diff):
    '''Check a user answer against answers in dictionary.
     Return True or False.

    Keyword Arguments:
    ans - answer entered by user
    blank - the blank word the user is trying to solve, ie (__1__)
    diff - dictionary containing answer for difficuilty level
    '''

    '''string name of the dictionary containing answers for
    the difficulty level the user specified.
    '''

    if ans == diff[blank]:
        return True
    else:
        return False


def update_attempts(att):
    '''Return updated number of attempts after incorrect guess.

    Keyword Arguments:
    att - number of attempts as int
    '''

    attempts_left = att - 1
    print('You have ', attempts_left, ' attempts remaining.')
    return attempts_left


def update_madlib(lib_dict, diff, blank, answer):
    '''Return updated madlib after correct guess.

    Keyword Arguments:
    lib_dict - dictionary containing mad lib
    diff - difficulty level of game
    blank - the blank word the user is trying to solve, ie (__1__)
    answer - correct user answer
    '''

    return lib_dict[diff].replace(blank, answer)


def play_again():
    '''Ask user if they want to play again. Return yes or no.'''

    answer = input('Do you want to play again? Enter yes or no.\n'
                   ).lower()
    valid_answers = ['yes', 'no']
    while answer not in valid_answers:
        answer = input('Enter yes or no.\n').lower()
    return answer


play_game()
