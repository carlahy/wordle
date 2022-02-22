import random
import numpy as np

def err(msg):
  print('Error: ' + msg)

def read_dict():
  with open('five_letter_words.csv', 'r') as file:
    words = file.read().split('\n')
  return words

def get_input(words):
  while True:
    answer = input('Enter a 5-letter word: ')  
    if len(answer) != 5:
      err('word must be 5-letters long')
    elif answer not in words:
      err('word must exist in dictionary')
    else:
      return answer

# Returns a 2D, 5x26 array to store the state of letters in the words
# 0 means unknown, 1 means letter is elsewhere in word, 
def get_init_letter_map():
  return np.zeros((5,26), dtype=int)

def guess(strategy, words):
  match strategy:
    case 1: 
      return guess_random(words)
    case 2: 
      return guess_elimination(words)
    case 3: 
      return guess_multistart(words)
    case 4: 
      return guess_vowels(words)
    case 5: 
      return guess_frequency(words)
    case _: 
      return guess_random(words)

def guess_random(words):
  return random.choice(words)

def guess_elimination(words, criteria):
  return update_words(words, criteria)

# Updates the list of words by removing words that do not fit the criteria
# Criteria is a list of lists with the form (char l, int i, int s):
# l is a letter in the word, i is the position of c within the word, and s is the state of the letter.
# This can be 0: not in word, 1: in word but not at index i, 2: in word at index i
def update_words(words, criteria):
  filtered = []
  for c in criteria:
    l = c[0]
    i = c[1]
    s = c[2]
    if s == 0:
      filtered = filter(lambda word: l not in word, words)
    elif s == 1:
      filtered = filter(lambda word: l in word and word[i] != l, words)
    elif s == 2:
      filtered = filter(lambda word: word[i] == l, words)
    else:
      err('unknown criteria \'s\' value')
    words = list(filtered)
  if len(words) == 0:
    err('there are no more words to choose from')

  return words

def play_strategy(strategy):
  all_words = read_dict()
  words = all_words
  answer = get_input(words)
  turns = 1
  guess = guess_random(words)
  progress = get_init_letter_map()
 
  while turns <= 6:
    print('Guess ' + str(turns) + '= ' + guess)
    if guess == answer:
      print('Hoorah! Answer = ' + answer + ' Turns = ' + str(turns))
      return
    accuracy = []
    criteria = []
    for i in range(0, len(guess)):
      letter = guess[i]
      if letter == answer[i]: # green
        accuracy.append(1)
        criteria.append([letter, i, 2])
      elif letter in answer: # yellow
        accuracy.append(0)
        criteria.append([letter, i, 1])
      else: # gray
        accuracy.append(-1)
        criteria.append([letter, i, 0])
    words = update_words(words, criteria)
    turns = turns + 1
    guess = random.choice(words)

  if guess == answer:
    print('Hoorah! Answer = ' +answer)
    return (True, turns)
  else:
    print('No! Answer = ' + answer)
    return (False, turns)
    
def play():
  strategy = int(input("""
	Select a strategy:
	1. Random: randomly guesses words with no strategy
	2. Elimination: after each turn, remove words that did not match the criteria
	3. Multi-start: the first two words are random words from the list. Subsequent strategy is elimination
	4. Vowels: the first word maximises the vowels (3+ vowels)
	5. Frequency: guess words by their frequency of usage. First word is random
"""))
  play_strategy(strategy)

play()
