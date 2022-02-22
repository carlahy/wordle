import csv 

with open("words.csv", "r") as file:
  words = file.read().split('\n')
five_letter_words = [w for w in words if len(w) == 5]

open("five_letter_words.csv", "w").close() # delete file contents

with open("five_letter_words.csv", "w", encoding='UTF8') as file:
  writer = csv.writer(file)
  for w in five_letter_words:
    writer.writerow([w])

file.close()

