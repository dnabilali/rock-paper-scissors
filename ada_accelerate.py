import random

def generate_code():
    letters_dict = {
        1: "R",
        2: "Y",
        3: "G",
        4: "B",
        5: "I",
        6: "V"
    }
    code = []
    for i in range(4):
        code.append(letters_dict[random.randrange(1,7)])
    return code

# print(generate_code())

def validate_guess(guess):
  guess_options = ["R", "Y", "G", "B", "I", "V"]
  for letter in guess:
    if letter.upper() not in guess_options:
      return False
    if len(guess) != 4:
      return False
  return True


# print(validate_guess(['R','I','Y','G','B']))


def check_win_or_lose(guess, code, num_guesses):
  if num_guesses > 8:
    return False
  if guess == code and num_guesses <= 8:
    return True
  elif guess != code and num_guesses > 8:
    return False

# print(check_win_or_lose(['R','M','Y','G'],['R','R','R','R'],3))

def create_dict(list):
  dictionary = {}
  for i in range(4):
    if list[i] in dictionary:
      dictionary[list[i]] += 1
    else:
      dictionary[list[i]] = 1
  return dictionary

def create_dict(list):
  dictionary = {}
  for i in range(4):
    if list[i] in dictionary:
      dictionary[list[i]] += 1
    else:
      dictionary[list[i]] = 1
  return dictionary

def color_count(guess, code):
  correct_colors_count = 0
  # guess_dict = {}
  # code_dict = {}
  
  # for i in range(4):
  #   if guess[i] in guess_dict:
  #     guess_dict[guess[i]] += 1
  #   else:
  #     guess_dict[guess[i]] = 1
  guess_dict = create_dict(guess)
      
  # for i in range(4):
  #   if code[i] in code_dict:
  #     code_dict[code[i]] += 1
  #   else:
  #     code_dict[code[i]] = 1
  code_dict = create_dict(code)
  
  for color in code_dict:
    if color in guess_dict:
      if code_dict[color] > guess_dict[color]:
        correct_colors_count += guess_dict[color]
      else:
        correct_colors_count += code_dict[color]
  return correct_colors_count


# print(color_count(['R','I','Y','G'],	['G','Y','I','R']))

def correct_pos_and_color(guess, code):
  correct_pos_color = 0 
  for i in range (4):
    if guess[i] == code[i]:
      correct_pos_color += 1
  return correct_pos_color

# print(correct_pos_and_color(['R','R','R','B']	,['R','I','B','B']))


def check_guess(guess, code):
  correct_col_wrong_pos = color_count(guess,code) - correct_pos_and_color(guess,code)
  check_guess_tuple = (correct_pos_and_color(guess,code) , correct_col_wrong_pos)
  return check_guess_tuple


def get_win_percentage(wins, plays):
  if plays == 0:
    win_percentage = 0
  else:
    win_percentage = int((wins/plays) * 100)
  return win_percentage



def format_guess_stats(guess_stats):
  guess_stats_list = []
  for i in range(1,9):
    if i in guess_stats:
      num_rounds_won = guess_stats[i] * "X"
    else:
      num_rounds_won = ""
    guess_stats_list.append(num_rounds_won)
  return guess_stats_list

# print(format_guess_stats({}))



# game loop!!!!!!!!!!!!!!!!!!!!!!!

# from .game import generate_code, validate_guess, color_count, correct_pos_and_color, check_guess, check_win_or_lose, get_win_percentage, format_guess_stats

# These functions allow you to print a string s in the stated colors. Using them is NOT required
def print_red(s):
    return '\033[31m' + s + '\033[0m'

def print_yellow(s):
    return '\033[33m' + s + '\033[0m'

def print_green(s):
    return '\033[32m' + s + '\033[0m'

def print_blue(s):
    return '\033[36m' + s + '\033[0m'

def print_indigo(s):
    return '\033[34m' + s + '\033[0m'

def print_violet(s):
    return '\033[35m' + s + '\033[0m'


def mastermind():
  plays = 0
  wins = 0
  guess_stats = {}
  num_guesses = 0
  print("Welcome yto Mastermind!")

  def get_code():
    code = generate_code()
    print("the code is:", code)
    print("Generating a new code... \nNew code generated: **** \nGuess the code! Each character in the code is one of the following letters: R, Y, G, B, I, V")
    return code

  def get_guess():
    no_guess = True
    while no_guess == True:
        print("Guess the code:")
        guess_input = input("")
        guess = []
        for color in guess_input:
            guess.append(color.upper())
        if validate_guess(guess):
            print(f'You guessed: {guess_input}')
            no_guess = False
            return guess
        else:
            print("This is an invalid code. Please try again!")
            no_guess = True

#   def get_guess():
#     guess_input = input("Guess the code: ")
#     guess = []
#     for color in guess_input:
#         guess.append(color.upper())
#     if validate_guess(guess):
#         print(f'You guesses: {guess_input}')
#         return guess
#     else:
#         print("This is an invalid code. Please try again!")
  
  play = True
  while play == True:
    code = get_code()
    plays += 1

    # def get_guess():
    #     no_guess = True
    #     while no_guess == True:
    #         print("Guess the code:")
    #         guess_input = input("")
    #         guess = []
    #         for color in guess_input:
    #             guess.append(color.upper())
    #         if validate_guess(guess):
    #             print(f'You guessed: {guess_input}')
    #             no_guess = False
    #             return guess
    #         else:
    #             print("This is an invalid code. Please try again!")
    #             no_guess = True

    guess = get_guess()    
    num_guesses += 1

    while check_win_or_lose(guess, code, num_guesses+1) == None:
        print(check_guess(guess,code))
        guess = get_guess()
        num_guesses += 1

    if check_win_or_lose(guess,code,num_guesses):
        print("Congratulations! You guessed the secret code!")
        wins += 1
        if num_guesses in guess_stats:
            guess_stats[num_guesses] += 1
        else:
            guess_stats[num_guesses] = 1
        num_guesses = 0
    else:
        print("You lost \U0001F622 Better luck next time!")  
        num_guesses = 0

    print(f"STATISTICS \nGames Played:{plays} \nWin %: {get_win_percentage(wins, plays)} \nGuess Distribution:")

    for i in range (8):
      print(f"{i+1}|{format_guess_stats(guess_stats)[i]}")

    print("Should we play another round? \nEnter y to replay, and any other character to exit:")
    ask_play_again = input("")
    print("\n")
    if ask_play_again == 'y' or ask_play_again == 'Y':
        play = True
    else:
        play = False

#   print(f"STATISTICS \n Games Played:{plays} \n Win %: {get_win_percentage(wins, plays)} \n Guess Distribution:")

#   for i in range (8):
#     print(f"{i+1}|{format_guess_stats(guess_stats)[i]}")

  

#   def prompt_guess():
    #   num_guesses = 0
    # guess_input = input("Guess the code: ")
    # guess = []
    # for col in guess_input:
    #     guess.append(col.upper())
    # if validate_guess(guess):
    # print(f"You guessed: {guess_input}")
    # if check_win_or_lose(guess, code, num_guesses):
    #     print("Congratulations! You guesses the secret code!")
    #     wins += 1
        # win = True
        # if wins in guess_stats:
        # guess_stats[wins] += 1
        # else:
        # guess_stats[wins] = 1
    # else:
    #     print(check_guess(guess, code))
    # else:
    # print("This is an invalid code. Please try again!")
    # prompt_guess(num_guesses)
        
#   win = False
    
#   while (num_guesses < 8) and (not win):
#     prompt_guess()
        
#   if not win:
#     print("You lost. Better luck next time!")

#   print(f"STATISTICS \n Games Played:{plays} \n Win %: {get_win_percentage(wins, plays)} \n Guess Distribution:")

#   for i in range (8):
#     print(f"{i+1}|{format_guess_stats(guess_stats)[i]}")

mastermind()
