import pandas as pd
import random
def openFile():
    "Opens file. Duh."
    file = "movie_metadata.csv"
    movies = pd.read_csv(file, index_col = 'id')
    return movies

def randomMovie(movies):
    "Chooses a random number which coresponds to a random movie from the data set"
    rows = movies.shape[0]
    randMovie = random.randint(0,5042)
    return randMovie

def guess(movies, randMovie, scores):
    "Runs through one round of guessing for both players."
    guessed1 = False
    guessed2 = False

    # Gets Rating of the movie
    movieRating = movies.values[randMovie][25]

    # Gets guesses from both users and makes sure both values are floats
    guess1 = input("Guess the rating: ")
    while not guessed1:
        try:
            guess1 = float(guess1)
        except ValueError:
            guess1 = input("Please input a number u idiot: ")
        else:
            guessed1 = True

    guess2 = input("Guess the rating: ")
    while not guessed2:
        try:
            guess2 = float(guess2)
        except ValueError:
            guess2 = input("Please input a number u idiot: ")
        else:
            guessed2 = True

    # Checks the accuracy of both guesses and then compares them to each other to determine a winner and gives the winner a point.
    guess1Accuracy = abs(movieRating - guess1)
    guess1Accuracy = round(guess1Accuracy, 1)
    guess2Accuracy = abs(movieRating - guess2)
    guess2Accuracy = round(guess2Accuracy, 1)

    if guess1Accuracy < guess2Accuracy:
        print("Player 1 wins! They were " + str(guess1Accuracy) + " points off.")
        scores[0] += 1
    elif guess2Accuracy < guess1Accuracy:
        print("Player 2 wins! They were " + str(guess2Accuracy) + " points off.")
        scores[1] += 1
    else:
        print("It's a draw. Y'all are equally bad.")

def playAgain():
    "Check to see if the user wants to play again"
    userInput = input("Do you want to play again? Type 'no' if not. If you don't type 'no', you gotta play again anyways u scrub: ")
    if userInput == "no":
        return False
    else:
        return True

    
