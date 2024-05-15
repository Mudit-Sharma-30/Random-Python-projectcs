import requests
import random
import os
import time
from dotenv import load_dotenv

def clean_movie_name(movie_name):
    # Remove all special characters and punctuation marks except spaces
    movie_name_cleaned = ''.join(char for char in movie_name if char.isalnum() or char.isspace())
    return movie_name_cleaned

def guessed_word(movie_name, already_guessed):
    unguessed_name = ""
    for i in movie_name:
        if i in already_guessed:
            unguessed_name += i
        elif i == ' ':
            unguessed_name += '/'
        else:
            unguessed_name += "_"
    print("\n\n\nAll the Words that you have guessed are :- ",already_guessed)
    return unguessed_name

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Linux, Unix, or macOS
    else:
        _ = os.system('clear')

def print_hollywood(chances,movie_name):
    
        
    alphabet = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCCC", "C    ", "C    ", "C    ", " CCCC"],
        'D': ["DDD  ", "D  D ", "D   D", "D  D ", "DDD  "],
        'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
        'F': ["FFFFF", "F    ", "FFFFF", "F    ", "F    "],
        'G': [" GGGG", "G    ", "G  GG", "G   G", " GGGG"],
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'I': ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
        'J': ["JJJJJ", "   J ", "   J ", "J  J ", " JJ  "],
        'K': ["K  K ", "K K  ", "KK   ", "K K  ", "K  K "],
        'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
        'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        'Q': [" QQQ ", "Q   Q", "Q Q Q", "Q  QQ", " QQQQ"],
        'R': ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"],
        'S': [" SSSS", "S    ", " SSS ", "    S", "SSSS "],
        'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
        'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
        'W': ["W   W", "W W W", "W W W", "WW WW", "W   W"],
        'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
        ' ': ["     ", "     ", "     ", "     ", "     "]
    }
    
    if(chances == 0):
        # clear_screen()
        sclied_word = "YOU LOSE"
        print(f"The correct movie name was {movie_name}")

    else:
        word = 'HOLLYWOOD'
        sclied_word = word[9-chances:9]
        # clear_screen()
    
    
    for row in range(5):  # Loop through each row of the ASCII art
        for letter in sclied_word:  # Loop through each letter in the word
            print(alphabet[letter][row], end='  ')  # Print the corresponding row of each letter
        print()  # Move to the next line for the next row
        
def movie_name_random():
    random_number = random.randint(100,1000)


    while(True):
        load_dotenv()
        key = os.getenv('key')
        # response = requests.get(
        #         f'https://api.themoviedb.org/3/movie/{}?api_key={key}&language=en-US'.format(random_number))
        response = requests.get(f'https://api.themoviedb.org/3/movie/{random_number}?api_key={key}&language=en-US')
        if response.status_code == 200:
            data = response.json()
            movie_name = data['title']
            break
        else:
            random_number = random.randint(100,5000)
    return (movie_name)

def game():
    movie_name = movie_name_random().lower()
    chances = 9
    already_guessed = ['a', 'e', 'i', 'o', 'u']  # Exclude vowels from this list
    
    cleaned_movie_name = clean_movie_name(movie_name)  # Clean movie name
    movie_name = cleaned_movie_name
    
    
    while chances != -1:
        print_hollywood(chances, movie_name)
        print(f"\n\nNumber of chances left: {chances}")
        
        unguessed = guessed_word(movie_name, already_guessed)
        print("\n\n\nGuess the Movie:- ",unguessed)

        guess = input("\n\nGuess a letter: ").lower()
        
        if guess in already_guessed:
            print(f"You've already guessed '{guess}'. Try another letter.")
        elif guess in movie_name:
            print(f"Correct! '{guess}' is in the movie name.")
            already_guessed.append(guess)
            unguessed_name = guessed_word(cleaned_movie_name, already_guessed)
            print("\n\n\nAfter the correct guess :- ", unguessed_name)
            if "_" not in unguessed_name:
                print("Congratulations! You guessed the movie name correctly.")
                print("\nMoving onto the next round")
                time.sleep(3)
                return 1
        else:
            print(f"Incorrect! '{guess}' is not in the movie name.")
            already_guessed.append(guess)
            chances -= 1
        
        

        if chances == 0:
            print(f"You ran out of chances. The correct movie name was '{movie_name.title()}'.")
            return 0
        time.sleep(1)
        clear_screen()
    
if __name__ == '__main__':
    clear_screen()
    
    name = input("Enter you name :- ")
    score = 0
    
    while(game()):
        clear_screen()
        score +=1
    
    
    time.sleep(1+2)
    clear_screen()
    print(f"{name} your Final score is {score}")
    
    