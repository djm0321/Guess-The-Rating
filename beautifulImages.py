import gameFunctions
from bs4 import BeautifulSoup
import requests
import pandas as pd

x = 0
movies = gameFunctions.openFile()
rows = movies.shape[0]
columns = movies.shape[1]

while x < rows:
    oldURL = movies.values[x][28]
    temp = oldURL[:-27:] + '.jpg'
    if temp[-8:] == '_V1_.jpg':
        movies.replace(oldURL, temp, inplace = True)
        if x == 0:
            print('yes')
    if (x == 0):
        print(movies.values[x][28])
        input()
    print(x)
    x += 1


movies.to_csv('movie_metadata.csv', index = False)

# posterURLs = []
# used to create column for movie poster URLs
# while x < rows:
#     url = movies.values[x][17]
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     try:
#         poster = soup.find('div', class_='poster').img['src']
#     except AttributeError:
#         movies.drop(x, inplace = True)
#         print("yes")
#         x -= 1
#         rows = movies.shape[0]
#     else:
#         posterURLs.append(poster)
#     print(x)
#     x += 1



