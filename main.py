import random

def read_dict():
  with open('five_letter_words.csv', 'r') as file:
    words = file.read().split('\n')
  return words

def get_input():
  while True:
    answer = input('Enter a 5-letter word: ')  
    if len(answer) != 5:
      print('Word must be 5-letters long')
    else:
      return answer

def guess(accuracy):
  return ""

def play():
  words = read_dict()
  answer = get_input()
  turns = 0
  guess = random.choice(words)
 
  while turns < 6:
    print('Guess ' + str(turns) + '= ' + guess)
    if guess == answer:
      return (True, turns)
    accuracy = []
    for i in range(0, len(guess)):
      if guess[i] == answer[i]:
        accuracy.append(1) # green
      elif guess[i] in answer:
        accuracy.append(0) # yellow
      else:
        accuracy.append(-1) # gray
    turns = turns + 1
    guess = random.choice(words)
   # guess = guess(words, accuracy)

  if guess == answer:
    print('Hoorah! Answer = ' + answer)
    return (True, turns)
  else:
    print('No! Answer = ' + answer)
    return (False, turns)
    

play()
