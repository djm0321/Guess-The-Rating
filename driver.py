import pandas as pd
import random

def main():
    file = "movie_metadata.csv"
    movies = pd.read_csv(file)
    rows = movies.shape[0]
    randMovie = random.randint(0,5042)
    print(str(movies.values[randMovie][11]) + ", " + str(movies.values[randMovie][25]))
    movie = movies.values[randMovie][11]
    movieRating = movies.values[randMovie][25]
    guess1 = float(input("Guess the rating: "))

    while not isinstance(guess1, float):
        input("Please input a number u idiot: ")

    guess2 = float(input("Guess the rating: "))

    while not isinstance(guess1, float):
        input("Please input a number u idiot: ")

    guess1Accuracy = abs(movieRating - guess1)
    guess1Accuracy = round(guess1Accuracy, 1)
    print(guess1Accuracy)
    guess2Accuracy = abs(movieRating - guess2)
    guess2Accuracy = round(guess2Accuracy, 1)
    print(guess2Accuracy)

    if guess1Accuracy < guess2Accuracy:
        print("Player 1 wins! They were " + str(guess1Accuracy) + " points off.")
    elif guess2Accuracy < guess1Accuracy:
        print("Player 2 wins! They were " + str(guess2Accuracy) + " points off.")
    else:
        print("It's a draw. Y'all are equally bad.")
     
main()