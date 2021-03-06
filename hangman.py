# import random_word
# from random_word import RandomWords
# r = RandomWords()
# rand_word = r.get_random_word()


import random 
from words import word_list


def round():
   word = random.choice(word_list)
   return word.upper()

def play(word):
   # round rules
   tries = 7
   survived = False
   length_hint = "_" * len(word)
   attempted_letters = []
   attempted_words = []

   # user instructions
   print("Let's play!")
   print(display_hangman(tries))
   print(length_hint + "\n")

   while not survived and tries > 0:
      guess = input("Guess a letter or, if you're feeling like taking a risk, the entire word.").upper()
      if len(guess) == 1 and guess.isalpha():
         if guess in attempted_letters:
            print("Oops! That letter was already attempted.")
         elif guess not in word:
            print("PSYCH... not even close, brah.")
            attempted_letters.append(guess)
            tries -= 1
         else:
            print("Totally in da word!")
            attempted_letters.append(guess)
            length_hint_list = list(length_hint)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               length_hint_list[index] = guess
            length_hint = "".join(length_hint_list)
            if "_" not in length_hint:
               survived = True
      elif len(guess) == len(word) and guess.isalpha():
         if guess in attempted_words:
            print("Oops! That word was already attempted.")
         elif guess != word:
            tries -= 1
            print("Not the word...")
         else:
            survived = True
            length_hint = word
      else:
         print("Not a valid guess :s")
      
      print(display_hangman(tries))
      print(length_hint)
   if survived:
      print("Congrats you have guessed the word! You win!")
   else:
      print("You have run out of words.  The word was " + word)

def display_hangman(tries):
    drawings = [  # other leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # rope
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # pole
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return drawings[tries]
      
def main():
   word = round()
   play(word)
   while input('Enter "again" to play again or "quit" to exit').lower() == "again":
      word = round()
      play(word)      
      

if __name__ == "__main__":
   main()
