import random
import time
from gtts import gTTS
import os 

language = 'en' # the application can be developed to be used by people speaking languages other than English

def difficulty_multiplier(now, rating): # function changes the word's rating based on how difficult the child found reading the word.
    change = 0
    if now >= 50:
        if rating == 1:
            change = -30
        elif rating == 2:
            change = -10
        elif rating == 3:
            change = 20
 # there are 2 options based on the 'now' score so the score can never be in the negative - which would be really demotivating for the child.      
    else:
        if rating == 2:
            change = 10
        elif rating == 3:
            change = 20
        
    new = now + change
    return new

def check_100(array): # returns the array
    for i in range(len(array)-1):
        if array[i][1] >= 100:
            del array[i]
    return array

# with my_mic as source: # can be developed to get the user to record the child reading the sentence out loud and AI would be used to compare rate how well it was read as a decimal between 0 and 1
#    print("Read the sentence out loud.")
#    r.adjust_for_ambient_noise(source)
#    audio = r.listen(source)

year_group = int(input("Enter your year group. > "))

if year_group == 2: # This application could be developed to find a year 2 text from a file of year 2 texts 
    file = open("C:\\Users\\24muriy01\\Downloads\\year_2.txt", "r")
    print(file.readline())
if year_group == 3:
    pass # a text from a file of year 3 texts would be printed out and so on for all the year groups between grades 1 to 8.

difficult = int(input("How many words do you find hard? > ")) # In the actual website, the user will be able to select the words but for the purpose of the demo we get them to be inputed by the user
words = []
individual = [] 
for i in range (difficult):
    word = input("Enter one word that you find difficult. > ")
    individual.append(word)
    individual.append(0)
    words.append(individual)
    individual = []

print(words)

print("Hi! Would you like to read some words from your word bank?") # In the website, the user would click a word bank icon to practice the words
ready = input("Please enter Y or N: ")
# not validating this, since on real website, would be a button to push, not a keyboard
count = 0

while ready == "Y":
    pos = random.randint(0, len(words)-1)
    print()
    print()
    print("Please read the following word: {}".format(words[pos][0]))
    time.sleep(5)
    myobj = gTTS(text=words[pos][0], lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")

    print("How did you find that word?")
    difficulty = int(input("Please enter a number between 1 and 3 (1 being that you found it difficult and 3 being that you found it easy): "))
    # not validating, since on real app is 3 different colours (red,orange,green)
    words[pos][1] = difficulty_multiplier(words[pos][1], difficulty)
    words = check_100(words)
    count += 1
    print()
    print("Do you want to continue?")
    ready = input("Please enter Y or N: ")

print("That was awesome! You read {} words!".format(count))
for i in words:
    print(i)

