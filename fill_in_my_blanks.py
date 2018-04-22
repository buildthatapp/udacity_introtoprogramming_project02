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
alive = True
madlibs = {
    'easy' : 'Dr. (__1__) is best known for his books \nThe (__2__)'
        +'in the (__3__) and How the \n(__4__) stole (__5__).',
    'medium' : '(__1__) is a (__2__) typed language. It utilizes an\n'
        +'(__3__) instead of a compiler. \nThe kind of snake in its '
        +'logo represents the name of the (__4__).\nIt is a very (__5__)'
        +' language to type. ',
    'hard' : 'Jurassic (__1__) was a 1993 movie about (__2__).' 
        +'\nThe plot of the movie was about a dinosaur (__3__) park gone wrong.'
        +'\nThe final scene pitting a (__4__)-rex against veloci(__5__) was very'
        +'cool.'
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

def play_game():
    '''Call functions to play fill in the blank.'''
def display_welcome():
    '''Display welcome message to user.'''
def get_difficulty():
    '''Prompt user to enter difficulty level. Return difficulty level as str.'''
def get_attempts():
    '''Prompt user to enter number of attempts. Return int > 0.'''
def dead_or_alive(att):
    '''Check if dead or alive based on number of attempts left.
    Return bool, True if alive and False is dead.

    Keyword Arguments:
    att - number of attempts as int
    '''
def display_madlib(diff, lib_dict):
    '''Dislpay madlib based on difficulty level.

    Keyword Arguments:
    diff - difficulty level as string
    lib_dict - madLib dictionary
    '''
def get_answer():
    '''Prompt user to enter answer to blanks. Return answer as str.'''
def update_attempts(att):
    '''Return updated number of attempts after incorrect guess.
    
    Keyword Arguments:
    att - number of attempts as int
    '''
def update_madlib(lib_dict, answer):
    '''Return updated madlib after correct guess.

    Keyword Arguments:
    lib_dict - dictionary containing mad lib
    answer - correct user answer
    '''
def play_again():
    '''Ask user if they want to play again. Return yes or no.'''
def reset_game():
    '''Reset values of variables to default. '''
def clear_screen():
    '''Clear the screen of text.'''
def test_guessing_game():
    '''Perform tests on guessing game.'''
