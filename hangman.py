

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6


print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
        
            
          
          
          
    if guess not in chosen_word:
      lives=lives-1
      print(stages[lives])
      if lives>1:
          print(f"you have {lives} lives left. Think again :)")
      elif lives==1:
        print(f"This is your last chance. Think again :)")
      elif lives==0:
        print(""""          
           , * * * ,                    
       , *           *,                  
      *____      ____  *,             
     *, |__0__| |__0__|  , Sorry              
     *,                  ,            
     *,     ========    ,               
      *,               *             
        *>>>>>><<<<<<<<  """)  
    
    

   
    print(f"{' '.join(display)}")

    #Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives==0:
        end_of_game= True
        print("You lose.")

    
      
    
      
   

   