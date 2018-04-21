''' Fill In The Blanks
    This game will allow a user to select a game difficulty level, a number of maximum attempts,
    and then provide the user with a block of text with several blank words that they must guess
    to fill in.

    Written by: Louis Magdaleno
    Date: 4/18/2018
'''
banner_length = 30
attempts = 1
difficulty = 'easy'


madlibs = {
    'easy' : 'Dr. (__1__) is best known for his books The (__2__) in the (__3__) and How the (__4__) stole (__5__).',
    'medium' : '(__1__) is a (__2__) typed language. It utilizes an (__3__) instead of a compiler. /nThe kind of snake in its logo represents the name of the (__4__)./nIt is a very (__5__) language to type. ',
    'hard' : 'Jurassic (__1__) was a 1993 movie about (__2__). /nThe plot of the movie was about a dinosaur (__3__) park gone wrong. /nThe final scene pitting a (__4__)-rex against veloci(__5__) was very cool.'
}

easy_answers = {
    '(__1__)' : 'suess',
    '(__2__)' : 'cat',
    '(__3__)' : 'hat',
    '(__4__)' : 'grinch',
    '(__5__)' : 'stole'
    }
medium_answers = {
    '(__1__)' : 'python',
    '(__2__)' : 'dynamically',
    '(__3__)' : 'interpreter',
    '(__4__)' : 'language',
    '(__5__)' : 'easy'
    }
hard_answers = {
    '(__1__)' : 'park',
    '(__2__)' : 'dinosaurs',
    '(__3__)' : 'park',
    '(__4__)' : 't',
    '(__5__)' : 'raptor'
    }
    

#Select Difficulty
def select_difficulty():
    game_difficulty = ''
    game_difficulty = input('What difficulty would you like to play? \nSelect either easy, medium, or hard.\n').lower()
    while game_difficulty not in madlibs.keys():
        difficulty = input('Please enter easy, medium, or hard.\n')
    print('Okay! \nYour game will be in ' + game_difficulty + ' mode.')
    print('*' * banner_length)
    return game_difficulty


#Select Number of Attempts
def select_number_of_attempts():
    number_of_attempts = int(0)
    number_of_attempts = input('How many attempts would you like?\nEnter a number greater than 0!.\n')
    while not number_of_attempts.isdigit() or int(number_of_attempts) < 1:
        number_of_attempts = input('Please enter a number greater than 0.\n')
    print('Okay! \nYou will have ' + number_of_attempts + ' attempts to win.')
    print('*' * banner_length)
    return number_of_attempts

#Welcome Message
def welcome_message():
    print('*' * banner_length)
    print('Hello! Welcome to Fill In The Blanks V1.0.')
    print('In this game, you will be asked to choose a \ndifficulty level and a number of guess attempts.')
    print('After that, you will be given a text passage \nwith several blank words to fill in.')
    print('*' * banner_length)

#Display Madlib
def display_madlib(diff):
    print(madlibs[diff])
#Ask for Answer
def ask_for_answer(diff):
    answer = input('What replaces ' 

#Check Answer
def check_answer(possible, guess):
    for answer in possible:
        if guess.lower() == answer.lower():
            return True
    return False

#Answer Question
def answerquestion(index, quiz):
        print('in answer question')
#Unit Tests

#Play Game
def play_game_func():
        welcome_message()
        difficulty = select_difficulty()
        attempts = select_number_of_attempts()
        display_madlib(difficulty)
        print('')
        print('')
        print('')
        print('out of number of attempts')

#Main
if __name__ == "__main__":
    play_game = True
    while play_game == True:
        play_game_func()
        
