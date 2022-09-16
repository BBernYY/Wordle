import random # import random module
inputwords = open('allowed_words.txt', 'r').read().split("\n") # download allowed words
words = open("words.txt", "r").readlines() # download answer words
word = random.choice(words).replace("\n", "").upper() # pick a word
def checker(guess, answer): # return a list showing which letters are in the correct or wrong place, and if they are in the answer
    result = [] # initialize result list
    for i in range(5): # with each letter
        if guess[i] == answer[i]:
            result.append("V") # add check mark if necessary
        elif guess[i] in answer:
            result.append("~") # add tilda if necessary
        else:
            result.append("X") # add cross mark if necessary
    return result # return the result
guessing = True
guesses = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]
inputs = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]
guessnum = 0
while guessing: # gameloop
    text = open("ASCII.txt", "r").read() # download the ascii text
    for i in range(30): # fill in the values
        text = text.replace(f"${str(i)}$", [k for j in inputs for k in j][i])
    for i in range(30):
        text = text.replace(f"$R{str(i)}$", [k for j in guesses for k in j][i])
    print(text) # print output
    insert = input("").upper()
    while not insert in inputwords: # error message loop
        print("SORRY I [DONT] SEEM TO [UNDERSTAND]\n\nTRY [AGAIN]:\n")
        insert = input("").upper()
    inputs[guessnum] = list(insert)
    guess = checker(insert, word)
    guesses[guessnum] = guess
    if guess == checker("aaaaa", "aaaaa"): # if won
        print("gg ez")
        guessing = False
        break
    elif guessnum > 4: # if loss
        print(f"YOU [FOOL] THE WORD WAS [{word}]")
        guessing = False
        break
    guessnum += 1
print("YOUR [SCORE] IS:\n\n")
for i in guesses: # print score
    print(i)